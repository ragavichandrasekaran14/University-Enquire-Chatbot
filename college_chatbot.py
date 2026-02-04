"""
College Enquiry Chatbot
A helpful assistant to answer student and parent queries about the college.
"""

# College information database
college_info = {
    "courses": [
        "Bachelor of Technology (B.Tech) - Computer Science",
        "Bachelor of Technology (B.Tech) - Mechanical Engineering",
        "Bachelor of Technology (B.Tech) - Electrical Engineering",
        "Bachelor of Science (B.Sc) - Physics",
        "Bachelor of Science (B.Sc) - Chemistry",
        "Bachelor of Arts (B.A) - English Literature"
    ],
    "admission": "You can apply online through our college website. Submit your application with required documents by the deadline. Admission is based on merit and entrance exam scores.",
    "eligibility": "For B.Tech: 12th pass with Math and Physics. For B.Sc and B.A: 12th pass with relevant subjects. Minimum 50% aggregate required.",
    "fees": {
        "btech": "₹5,00,000 per year",
        "bsc": "₹2,00,000 per year",
        "ba": "₹1,50,000 per year"
    },
    "hostel": {
        "availability": "Yes, separate hostels for boys and girls",
        "capacity": "500 students total",
        "facilities": ["WiFi", "Mess facility", "24/7 Security", "Sports facilities", "Study rooms"]
    },
    "timings": "Classes: 8:00 AM - 5:00 PM (Monday-Friday), Library: 7:00 AM - 9:00 PM, Hostels: Open 24/7",
    "placement": {
        "average_package": "₹6.5 LPA",
        "highest_package": "₹15 LPA",
        "companies": ["TCS", "Infosys", "Google", "Microsoft", "Amazon"],
        "placement_rate": "95%"
    },
    "contact": {
        "phone": "+91-1234-567890",
        "email": "admissions@college.edu",
        "address": "123 Education Street, City, State 000000",
        "website": "www.college.edu"
    }
}

def get_course_info():
    """Return list of courses offered"""
    courses = "\n".join([f"• {course}" for course in college_info["courses"]])
    return f"We offer the following courses:\n{courses}"

def get_admission_info():
    """Return admission process details"""
    return f"Admission Process:\n{college_info['admission']}"

def get_eligibility_info():
    """Return eligibility criteria"""
    return f"Eligibility Criteria:\n{college_info['eligibility']}"

def get_fee_info():
    """Return fee structure"""
    fees_text = "\n".join([f"• {key.upper()}: {value}" for key, value in college_info["fees"].items()])
    return f"Fee Structure:\n{fees_text}"

def get_hostel_info():
    """Return hostel facilities"""
    facilities = "\n".join([f"• {facility}" for facility in college_info["hostel"]["facilities"]])
    return f"Hostel Facilities:\nAvailability: {college_info['hostel']['availability']}\nCapacity: {college_info['hostel']['capacity']} students\n\nFacilities:\n{facilities}"

def get_timings_info():
    """Return college timings"""
    return f"College Timings:\n{college_info['timings']}"

def get_placement_info():
    """Return placement details"""
    companies = ", ".join(college_info['placement']['companies'])
    return f"Placement Details:\n• Average Package: {college_info['placement']['average_package']}\n• Highest Package: {college_info['placement']['highest_package']}\n• Placement Rate: {college_info['placement']['placement_rate']}\n• Top Recruiting Companies: {companies}"

def get_contact_info():
    """Return contact information"""
    contact_text = f"""Contact Information:
• Phone: {college_info['contact']['phone']}
• Email: {college_info['contact']['email']}
• Address: {college_info['contact']['address']}
• Website: {college_info['contact']['website']}"""
    return contact_text

def process_query(user_input):
    """Process user query and return appropriate response"""
    user_input = user_input.lower().strip()
    
    # Define keywords for different topics
    if any(word in user_input for word in ["course", "program", "degree"]):
        return get_course_info()
    
    elif any(word in user_input for word in ["admission", "apply", "application"]):
        return get_admission_info()
    
    elif any(word in user_input for word in ["eligible", "eligibility", "requirement", "qualify"]):
        return get_eligibility_info()
    
    elif any(word in user_input for word in ["fee", "fees", "cost", "price", "tuition"]):
        return get_fee_info()
    
    elif any(word in user_input for word in ["hostel", "accommodation", "room", "stay"]):
        return get_hostel_info()
    
    elif any(word in user_input for word in ["timing", "time", "schedule", "class", "when"]):
        return get_timings_info()
    
    elif any(word in user_input for word in ["placement", "job", "salary", "recruit", "company"]):
        return get_placement_info()
    
    elif any(word in user_input for word in ["contact", "call", "phone", "email", "address"]):
        return get_contact_info()
    
    elif any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
        return "Hello! Welcome to our College Enquiry Chatbot. I'm here to answer your questions about our college. How can I help you today?"
    
    elif any(word in user_input for word in ["thank", "thanks", "thankyou"]):
        return "You're welcome! If you have any more questions, feel free to ask."
    
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Thank you for your enquiry. Have a great day!"
    
    elif user_input in ["?", "help"]:
        return """I can help you with:
• Courses offered
• Admission process
• Eligibility criteria
• Fee structure
• Hostel facilities
• College timings
• Placement details
• Contact information

Feel free to ask any college-related questions!"""
    
    elif user_input == "":
        return "Please ask me a question about our college."
    
    else:
        # Check if it's a college-related but unknown question
        if any(word in user_input for word in ["college", "university", "study", "learn", "education"]):
            return "Please contact the college office for accurate information."
        else:
            return "I can only answer questions related to college enquiries. Please ask about our courses, admission, fees, hostel, placement, or other college-related topics."

def display_welcome_message():
    """Display welcome message"""
    print("\n" + "="*60)
    print("Welcome to College Enquiry Chatbot")
    print("="*60)
    print("\nHello! I'm your friendly College Enquiry Assistant.")
    print("I'm here to answer your questions about our college.")
    print("\nType '?' or 'help' for assistance with available topics.")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    print("="*60 + "\n")

def main():
    """Main chatbot function"""
    display_welcome_message()
    
    while True:
        try:
            # Get user input
            user_query = input("You: ").strip()
            
            # Check for exit commands
            if user_query.lower() in ["exit", "quit", "bye", "goodbye"]:
                print("\nChatbot: Thank you for your enquiry. Have a great day!")
                print("="*60)
                break
            
            # Skip empty input
            if not user_query:
                continue
            
            # Get response
            response = process_query(user_query)
            print(f"\nChatbot: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nChatbot: Thank you for using our service. Goodbye!")
            print("="*60)
            break
        except Exception as e:
            print(f"\nChatbot: An error occurred. Please try again.\n")

if __name__ == "__main__":
    main()
