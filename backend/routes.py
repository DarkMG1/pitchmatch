from flask import Blueprint, request, jsonify, render_template
import utils
import database
import math

api = Blueprint("api", __name__)

@api.route("/api/signup", methods=["POST"])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not name or not email or not password or not role:
        return jsonify({"error": "All fields are required"}), 400

    # Check if user already exists
    if database.read_login({"email": email}):
        return jsonify({"error": "User already exists"}), 400

    # Hash password
    hashed_password = utils.hash_password(password)

    # Save user to database
    user = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "role": role,
    }
    database.write_login(user)

    return jsonify({"message": "User registered successfully"}), 201

@api.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Find user in database
    user = database.read_login({"email": email})
    if not user or not utils.verify_password(password, user["password"]):
        return jsonify({"error": "Invalid email or password"}), 401

#Login: Requires email in the body of the request
@api.route("/api/profile/vc", methods=["POST"])
def create_vc_profile():
    data = request.json
    user_id = data.email  # Get user ID from the token
    budget = data.get("budget")
    industry = data.get("industry")
    business_size = data.get("business_size")
    equity = data.get("equity")
    vc_location = data.get("location")
    certifications = data.get("certifications")
    tags = data.get("tags")

    if not budget or not industry or not business_size or not equity or not location:
        return jsonify({"error": "All fields are required"}), 400

    # Save VC profile to database
    profile = {
        "user_id": user_id,
        "type": "vc",
        "budget": budget,
        "industry": industry,
        "business_size": business_size,
        "equity": equity,
        "location": vc_location,
        "certifications": certifications,
    }
    database.write_vc(profile)

    return jsonify({"message": "VC profile created successfully"}), 201

#Login: Requires email in the body of the request
@api.route("/api/profile/startup", methods=["POST"])
def create_startup_profile():
    data = request.json
    user_id = data.email # Get user ID from the token
    desired_fund = data.get("desired_fund")
    equity_offered = data.get("equity_offered")
    pitch_deck = data.get("pitch_deck")
    sb_location = data.get("location")
    financials = data.get("financials")
    certifications = data.get("certifications")

    if not desired_fund or not equity_offered or not pitch_deck or not financials:
        return jsonify({"error": "All fields are required"}), 400

    # Save Startup profile to database
    profile = {
        "user_id": user_id,
        "type": "startup",
        "desired_fund": desired_fund,
        "equity_offered": equity_offered,
        "pitch_deck": pitch_deck,
        "financials": financials,
        "location": sb_location,
        "certifications": certifications,
    }
    database.write_startup(profile)

    return jsonify({"message": "Startup profile created successfully"}), 201

@api.route("/api/matchmaking", methods=["POST"])
def match_making_alg():
    sb_data, vc_data = request.json
    sb_id = sb_data.get("sb_user_id")
    sb_fund = sb_data.get("sb_desired_fund")
    sb_equity = sb_data.get("sb_equity_offered")
    sb_location = sb_data.get("sb_location")
    sb_industry = sb_data.get("sb_industry")
    vc_fund = vc_data.get("vc_investment")
    vc_equity = vc_data.get("vc_equity_desired")
    vc_location = vc_data.get("vc_location")
    vc_industry = vc_data.get("vc_industry")
    vc_id = vc_data.get("vc_user_id")
    if sb_industry == vc_industry:
        if math.abs(sb_fund-vc_fund)/max(sb_fund,vc_fund) <= 0.2:
            if sb_location == vc_location or math.abs(sb_equity-vc_equity)/max(sb_equity,vc_equity) <= 0.2:
                return jsonify({"message": f"Match has been made between {vc_id} and {sb_id}"})