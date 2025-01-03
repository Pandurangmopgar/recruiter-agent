import re
from typing import Dict, List, Tuple
from email_validator import validate_email, EmailNotValidError
from ..config.settings import REQUIRED_FIELDS

class DataValidator:
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        try:
            validate_email(email)
            return True, ""
        except EmailNotValidError as e:
            return False, str(e)
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        phone_pattern = re.compile(r'^\+?1?\d{9,15}$')
        if phone_pattern.match(phone):
            return True, ""
        return False, "Invalid phone number format"
    
    @staticmethod
    def validate_experience(experience: str) -> Tuple[bool, str]:
        try:
            exp = float(experience)
            if 0 <= exp <= 50:  # Reasonable range for years of experience
                return True, ""
            return False, "Experience years should be between 0 and 50"
        except ValueError:
            return False, "Experience must be a number"
    
    @staticmethod
    def validate_tech_stack(tech_stack: List[str]) -> Tuple[bool, str]:
        if not tech_stack:
            return False, "Tech stack cannot be empty"
        if len(tech_stack) > 20:  # Reasonable limit
            return False, "Too many technologies listed"
        return True, ""
    
    @staticmethod
    def validate_candidate_info(info: Dict) -> Tuple[bool, List[str]]:
        missing_fields = [field for field in REQUIRED_FIELDS if field not in info]
        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"
        
        errors = []
        
        # Validate email
        email_valid, email_error = DataValidator.validate_email(info['email'])
        if not email_valid:
            errors.append(f"Email error: {email_error}")
        
        # Validate phone
        phone_valid, phone_error = DataValidator.validate_phone(info['phone'])
        if not phone_valid:
            errors.append(f"Phone error: {phone_error}")
        
        # Validate experience
        exp_valid, exp_error = DataValidator.validate_experience(info['experience'])
        if not exp_valid:
            errors.append(f"Experience error: {exp_error}")
        
        # Validate tech stack
        tech_valid, tech_error = DataValidator.validate_tech_stack(info['tech_stack'])
        if not tech_valid:
            errors.append(f"Tech stack error: {tech_error}")
        
        return len(errors) == 0, errors 