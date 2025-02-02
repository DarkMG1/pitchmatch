from flask import Blueprint, request, jsonify
from models import users_collection, profiles_collection
from utils import hash_password, verify_password, decode_token, generate_token
from functools import wraps

api = Blueprint("api", __name__)

@api.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not name or not email or not password or not role:
        return jsonify({"error": "All fields are required"}), 400

    # Check if user already exists
    if users_collection.find_one({"email": email}):
        return jsonify({"error": "User already exists"}), 400

    # Hash password
    hashed_password = hash_password(password)

    # Save user to database
    user = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "role": role,
    }
    users_collection.insert_one(user)

    return jsonify({"message": "User registered successfully"}), 201

@api.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    # Find user in database
    user = users_collection.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        return jsonify({"error": "Invalid email or password"}), 401

    # Generate JWT
    token = generate_token(str(user["_id"]), user["role"])

    return jsonify({"message": "Login successful", "token": token}), 200

@api.route("/profile/vc", methods=["POST"])
@login_required
def create_vc_profile():
    data = request.json
    user_id = request.user_id  # Get user ID from the token
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
    profiles_collection.insert_one(profile)

    return jsonify({"message": "VC profile created successfully"}), 201

@api.route("/profile/startup", methods=["POST"])
# @login_required
def create_startup_profile():
    data = request.json
    user_id = request.user_id  # Get user ID from the token
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
    profiles_collection.insert_one(profile)

    return jsonify({"message": "Startup profile created successfully"}), 201

@api.route("/profile/startup", methods=["POST"])
def create_startup_profile():
    data = request.json
    user_id = data.get("user_id")
    desired_fund = data.get("desired_fund")
    equity_offered = data.get("equity_offered")
    pitch_deck = data.get("pitch_deck")
    financials = data.get("financials")
    certifications = data.get("certifications")

    if not user_id or not desired_fund or not equity_offered or not pitch_deck or not financials:
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
    profiles_collection.insert_one(profile)

    return jsonify({"message": "Startup profile created successfully"}), 201

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Authorization token is missing"}), 401

        # Decode and verify token
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Invalid or expired token"}), 401

        # Attach user ID and role to the request
        request.user_id = payload["user_id"]
        request.role = payload["role"]

        return f(*args, **kwargs)
    return decorated_function