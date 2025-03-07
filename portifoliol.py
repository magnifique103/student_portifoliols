import streamlit as st
import pandas as pd
from PIL import Image
import base64
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="My Digital Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add custom CSS for animations and styling
st.markdown("""
<style>
    .main {
        animation: fadeIn 1s ease-in;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    .project-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        transition: all 0.3s;
        background-color: white;
    }
    .project-card:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
        transform: translateY(-5px);
    }
    .timeline-item {
        border-left: 2px solid #4CAF50;
        padding-left: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    .timeline-item:before {
        content: '';
        position: absolute;
        left: -10px;
        top: 0;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: #4CAF50;
    }
    .testimonial {
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        background-color: #f9f9f9;
        border-left: 5px solid #4CAF50;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Session state initialization
if 'name' not in st.session_state:
    st.session_state.name = "UWAJENEZA Magnifique"
if 'location' not in st.session_state:
    st.session_state.location = "Ruhengeri, Rwanda"
if 'university' not in st.session_state:
    st.session_state.university = "INES-Ruhengeri"
if 'field' not in st.session_state:
    st.session_state.field = "Computer Science, Year 3"
if 'bio' not in st.session_state:
    st.session_state.bio = "I am a passionate computer science student with a keen interest in AI and machine learning. I enjoy solving complex problems and creating innovative solutions."
if 'active_section' not in st.session_state:
    st.session_state.active_section = "Home"
if 'filtered_category' not in st.session_state:
    st.session_state.filtered_category = "All Projects"

# Navigation
st.sidebar.title("Navigation")
sections = ["Home", "Projects", "Skills & Achievements", "Timeline", "Testimonials", "Customize Profile", "Contact"]
for section in sections:
    if st.sidebar.button(section):
        st.session_state.active_section = section

# Profile image (placeholder)
st.sidebar.markdown("---")
st.sidebar.title("Profile")
profile_pic = st.sidebar.file_uploader("img.jpg", type=['jpg', 'png', 'jpeg'])
if profile_pic is not None:
    st.sidebar.image(profile_pic, width=200)
else:
    st.sidebar.markdown("📷 *Upload your profile picture*")

# Display current date
current_date = datetime.now().strftime("%B %d, %Y")
st.sidebar.markdown(f"**Today's Date:** {current_date}")

# Resume download function
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{bin_file}" class="download-button">Download {file_label}</a>'
    return href

# Home Section
if st.session_state.active_section == "Home":
    st.markdown("""
    <div style='animation: fadeIn 1s ease-in;'>
        <h1 style='text-align: center;'>👋 Welcome to My Digital Portfolio</h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="profile-section">', unsafe_allow_html=True)
        # Use a placeholder image if no image is uploaded
        profile_image = Image.open("img.jpg") if 'profile_pic' not in st.session_state else st.session_state.profile_pic
        st.image(profile_image, width=200, caption="")
        

    with col2:
        st.markdown(f"# {st.session_state.name}")
        st.markdown(f"## {st.session_state.field}")
        st.markdown(f"**Location:** {st.session_state.location}")
        st.markdown(f"**University:** {st.session_state.university}")
        
    st.markdown("---")
    st.markdown("### About Me")
    st.markdown(f"{st.session_state.bio}")
    
    st.markdown("---")
    # Resume Upload and Download
    resume_file = st.file_uploader("resume.pdf", type=['pdf'])
    if resume_file is not None:
        # Save the uploaded file
        with open("resume.pdf", "wb") as f:
            f.write(resume_file.getbuffer())
        st.success("Resume uploaded successfully!")
        st.markdown(get_binary_file_downloader_html("resume.pdf", 'Resume'), unsafe_allow_html=True)
    
    
    col1, col2 = st.columns([1, 2])
    
   
   
   
    st.markdown("---")
    # Resume Upload and Download
    resume_file = st.file_uploader("resume", type=['pdf'])
    if resume_file is not None:
        # Save the uploaded file
        with open("resume.pdf", "wb") as f:
            f.write(resume_file.getbuffer())
        st.success("Resume uploaded successfully!")
        st.markdown(get_binary_file_downloader_html("resume.pdf", 'Resume'), unsafe_allow_html=True)
    else:
        st.info("Please upload your CV/Resume in PDF format")
            # Download resume button
        resume_file = "resume.pdf"  # You need to have this file in your project directory
        try:
            with open(resume_file, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(
                label="Download Resume",
                data=PDFbyte,
                file_name="resume.pdf",
                mime="application/pdf"
            )
        except:
            st.write("Resume PDF not available. Please upload your resume.")
        
        st.markdown('</div>', unsafe_allow_html=True)


# Projects Section
elif st.session_state.active_section == "Projects":
    st.markdown("""
    <div style='animation: fadeIn 1s ease-in;'>
        <h1 style='text-align: center;'>🚀 My Projects</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Project filtering
    project_categories = [ "all", "Group project", "Year 1 project","Year 2 Projects", "Individual Projects", "dessaertation"]
    selected_category = st.selectbox("Filter Projects by Category", project_categories)
    st.session_state.filtered_category = selected_category
    
    # Project data (you can modify this or load from a file)
    projects = [
        {
            "title": "Tour Guided room",
            "type": "Year 1 individual Project",
            "category": ["Year 1 Projects"],
            "description": "Developed a system that automates Tour Guide room tracking using facial recognition technology. The system uses computer vision to identify all perspn in real-time and guide to select any room and everywhere.",
            "technologies": "HTML, css",
            "github": "https://github.com/magnifique103/TourGueded_Room.git",
            "image": None
        },
        {
            "title": "subscriptionBox",
            "type": "Year 2 Individual Assignment",
            "category": ["Year 2 Projects"],
            "description": "Built a responsive subscriptionBox gifts, shopping cart, and subscribe. the service are available on time make our custome stisfied.",
            "technologies": "HTML, CSS, JavaScript, Bootstrap",
            "github": "https://github.com/magnifique103/subscriptionbox.git",
            "image": None
        },
        {
            "title": "Student_portifolio",
            "type": "Final Year Project",
            "category": ["Year 3 Projects"],
            "description": "Researching and developing an AI-powered student_potifolio. The system uses natural language processing to understand student portififolio descriptions and machine learning to predict potential conditions.",
            "technologies": "Python, TensorFlow, NLTK, Streamlit, reat",
            "github": "https://github.com/magnifique103/student_portifoliols.git",
            "image": None
        }
    ]
    
    # Filter projects based on selection
    filtered_projects = projects
    if st.session_state.filtered_category != "All Projects":
        filtered_projects = [p for p in projects if st.session_state.filtered_category in p["category"]]
    
    # Display projects
    for project in filtered_projects:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <h2>{project['title']}</h2>
                <h4>{project['type']}</h4>
                <p>{project['description']}</p>
                <p><strong>Technologies:</strong> {project['technologies']}</p>
                <p><strong>GitHub:</strong> <a href="{project['github']}" target="_blank">{project['github']}</a></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Option to add a new project
    st.markdown("---")
    st.markdown("### Add a New Project")
    new_project_title = st.text_input("Project Title")
    new_project_type = st.selectbox("Project Type", ["Individual Project", "Group Project", "Class Assignment", "Internship Project", "Dissertation"])
    new_project_category = st.multiselect("Project Categories", ["Year 1 Projects", "Year 2 Projects", "Year 3 Projects", "Group Projects", "Individual Projects", "Dissertation"])
    new_project_desc = st.text_area("Project Description")
    new_project_tech = st.text_input("Technologies Used")
    new_project_github = st.text_input("GitHub Link")
    
    if st.button("Add Project"):
        if new_project_title and new_project_desc:
            st.success("Project added successfully! (Note: This is a demo so the project won't persist after refresh)")

# Skills & Achievements Section
elif st.session_state.active_section == "Skills & Achievements":
    st.markdown("""
    <div style='animation: fadeIn 1s ease-in;'>
        <h1 style='text-align: center;'>🔧 Skills & Achievements</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Programming Skills
    st.markdown("### Programming Languages")
    col1, col2 = st.columns(2)
    
    with col1:
        python_skill = st.slider("Python", 0, 100, 85)
        javascript_skill = st.slider("JavaScript", 0, 100, 70)
        java_skill = st.slider("Java", 0, 100, 60)
    
    with col2:
        sql_skill = st.slider("SQL", 0, 100, 75)
        html_css_skill = st.slider("HTML/CSS", 0, 100, 90)
        cpp_skill = st.slider("C++", 0, 100, 55)
    
    # Technical Skills
    st.markdown("### Technical Skills")
    col1, col2 = st.columns(2)
    
    with col1:
        ml_skill = st.slider("Machine Learning", 0, 100, 70)
        web_dev_skill = st.slider("Web Development", 0, 100, 85)
        mobile_skill = st.slider("Mobile Development", 0, 100, 60)
    
    with col2:
        data_skill = st.slider("Data Science", 0, 100, 75)
        ui_ux_skill = st.slider("UI/UX Design", 0, 100, 65)
        devops_skill = st.slider("DevOps", 0, 100, 55)
    
    # Certifications and Achievements
    st.markdown("### Certifications & Achievements")
    
    certifications = [
        "Google Data Analytics Professional Certificate",
        "AWS Cloud Practitioner Certification",
        "Finalist in University Coding Competition 2023",
        "Speaker at Student Technology Conference 2024",
        "Published Research Paper in Technology Journal"
    ]
    
    for cert in certifications:
        st.markdown(f"- {cert}")
    
    # Add new certification
    st.markdown("---")
    st.markdown("### Add New Certification or Achievement")
    new_cert = st.text_input("Certification/Achievement Title")
    if st.button("Add Certification"):
        if new_cert:
            st.success(f"Added: {new_cert} (Note: This is a demo so the certification won't persist after refresh)")
            
# Timeline Section
elif st.session_state.active_section == "Timeline":
    st.markdown("""
    <div style='animation: fadeIn 1s ease-in;'>
        <h1 style='text-align: center;'>⏳ My Academic & Project Timeline</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline events
    timeline_events = [
        {"year": "2022", "event": "Started BSc in Computer Science at INES-Ruhengeri", "icon": "🎓"},
        {"year": "2022", "event": "Completed first programming assignment in Python", "icon": "💻"},
        {"year": "2023", "event": "Participated in University Hackathon", "icon": "🏆"},
        {"year": "2023", "event": "Summer Internship at Local Tech Company", "icon": "💼"},
        {"year": "2024", "event": "Started final year dissertation on AI in Healthcare", "icon": "🔬"},
        {"year": "2024", "event": "Published first research paper", "icon": "📝"},
        {"year": "2025", "event": "Expected Graduation", "icon": "🎉"}
    ]
    
    for event in timeline_events:
        st.markdown(f"""
        <div class="timeline-item">
            <h3>{event['year']} {event['icon']}</h3>
            <p>{event['event']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add new timeline event
    st.markdown("---")
    st.markdown("### Add New Timeline Event")
    event_year = st.selectbox("Year", ["2022", "2023", "2024", "2025"])
    event_desc = st.text_input("Event Description")
    event_icon = st.selectbox("Icon", ["🎓", "💻", "🏆", "💼", "🔬", "📝", "🎉", "🚀", "🌟"])
    
    if st.button("Add Event"):
        if event_desc:
            st.success(f"Added event for {event_year}: {event_desc} (Note: This is a demo so the event won't persist after refresh)")

# Testimonials Section
elif st.session_state.active_section == "Testimonials":
    st.markdown("""
    <div style='animation: fadeIn 1s ease-in;'>
        <h1 style='text-align: center;'>🗣️ Testimonials</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Sample testimonials
    testimonials = [
        {"name": "Dr. Theodore Johnson", "role": "Computer Science Professor", "message": "An exceptional student with remarkable problem-solving abilities. The final year project demonstrates innovation and technical excellence."},
        {"name": "Jane Doe", "role": "Classmate & Project Partner", "message": "Working with you on our group project was a fantastic experience. Your coding skills and project management abilities are outstanding!"},
        {"name": "John Smith", "role": "Internship Supervisor", "message": "Demonstrated exceptional skills during the internship. Quick learner, hard worker, and brings creative solutions to complex problems."}
    ]
    
    for testimonial in testimonials:
        st.markdown(f"""
        <div class="testimonial">
            <p>"{testimonial['message']}"</p>
            <p><strong>- {testimonial['name']}</strong>, {testimonial['role']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Add new testimonial
    st.markdown("---")
    st.markdown("### Add New Testimonial")
    testimonial_name = st.text_input("Uwajeneza Magnifique")
    testimonial_role = st.text_input("Software Engineering Student")
    testimonial_message = st.text_area("I' am student in software engineering, I would like to be a part of your engineering team")
    
    if st.button("Add Testimonial"):
        if testimonial_name and testimonial_message:
            st.success(f"Added testimonial from {testimonial_name} (Note: This is a demo so the testimonial won't persist after refresh)")

# Customize Profile Section
elif st.session_state.active_section == "Customize Profile":
    st.markdown("""
    <div style='animation: fadeIn 1s ease-in;'>
        <h1 style='text-align: center;'>⚙️ Customize Your Profile</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("Update your profile information. Changes will be saved for this session.")
    
    # Form for profile customization
    st.session_state.name = st.text_input("Full Name", value=st.session_state.name)
    st.session_state.location = st.text_input("Location", value=st.session_state.location)
    st.session_state.university = st.text_input("University", value=st.session_state.university)
    st.session_state.field = st.text_input("Field of Study", value=st.session_state.field)
    st.session_state.bio = st.text_area("About Me", value=st.session_state.bio)
    
    if st.button("Save Changes"):
        st.success("Profile updated successfully!")
        st.balloons()

# Contact Section
elif st.session_state.active_section == "Contact":
    st.markdown("""
    <div style='animation: fadeIn 1s ease-in;'>
        <h1 style='text-align: center;'>📬 Contact Me</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact form
    contact_col1, contact_col2 = st.columns(2)
    
    with contact_col1:
        st.markdown("### Send me a message")
        contact_name = st.text_input("Uwajeneza Magnifique")
        contact_email = st.text_input("ug2321406@inesa.ac.rw")
        contact_message = st.text_area("i do here as a software engineering student, I would like to be a part of engineering team")
        
        if st.button("Send Message"):
            if contact_name and contact_email and contact_message:
                st.success("Message sent successfully! I'll get back to you soon.")
                time.sleep(1)
                st.snow()
            else:
                st.error("Please fill out all fields.")
    
    with contact_col2:
        st.markdown("### Connect with me")
        st.markdown("""
        - 📧 **Email**: ug2321406@ines.ac.rw
        - 💼 **LinkedIn**: [linkedin.com/in/yourusername](https://linkedin.com/in/yourusername)
        - 💻 **GitHub**: [github.com/yourusername](https://github.com/yourusername)
        - 🌐 **Personal Website**: [magnifiqueiris5@gmail.com](https://yourdomain.com)
        - 📱 **Phone**: +250 787 185 621
        """)
        
        st.markdown("### Location")
        st.markdown("Musanze, Rwanda")
        # You could add a map here if you wanted to

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p>© 2025 My Digital Portfolio | Created with Streamlit</p>
</div>
""", unsafe_allow_html=True)