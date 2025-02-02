from flask import Blueprint, request, jsonify, render_template
import utils
import database

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

    return jsonify({"message": "Login successful"}), 200

#Login: Requires email in the body of the request
@api.route("/api/profile/vc", methods=["POST"])
def create_vc_profile():
    data = request.json
    user_id = data.email  # Get user ID from the token
    budget = data.get("budget")
    industry = data.get("industry")
    business_size = data.get("business_size")
    equity = data.get("equity")
    location = data.get("location")
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
        "location": location,
        "certifications": certifications,
        "tags": tags,
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
        "certifications": certifications,
    }
    database.write_startup(profile)

    return jsonify({"message": "Startup profile created successfully"}), 201