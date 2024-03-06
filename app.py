import streamlit as st

# Set the page configuration
st.set_page_config(page_title="My CV", page_icon=":briefcase:", layout="centered")

# Add a title and header
st.title("John Doe")
st.header("Software Engineer")

# Add profile information
st.subheader("Profile")
st.write("Experienced software engineer with a passion for developing high-quality, scalable applications. Skilled in Python, Java, and various web technologies. Dedicated to continuous learning and staying up-to-date with the latest industry trends.")

# Add work experience
st.subheader("Work Experience")
st.write("### Software Engineer")
st.write("XYZ Company, City, State")
st.write("June 2018 - Present")
st.write("""
- Developed and maintained web applications using Python, Flask, and React
- Implemented RESTful APIs and integrated with third-party services
- Optimized application performance and implemented caching strategies
- Collaborated with cross-functional teams to deliver high-quality software
""")

st.write("### Junior Software Engineer")
st.write("ABC Company, City, State")
st.write("August 2015 - May 2018")
st.write("""
- Participated in the development and maintenance of internal web applications
- Assisted in debugging and troubleshooting issues
- Contributed to code reviews and adhered to best coding practices
""")

# Add education
st.subheader("Education")
st.write("### Bachelor of Science in Computer Science")
st.write("University Name, City, State")
st.write("September 2011 - May 2015")

# Add skills
st.subheader("Skills")
st.write("- Python, Flask, Django")
st.write("- Java, Spring Framework")
st.write("- JavaScript, React, Angular")
st.write("- HTML, CSS")
st.write("- SQL, NoSQL databases")
st.write("- Git, Agile methodologies")

# Add interests (optional)
st.subheader("Interests")
st.write("- Open-source contributions")
st.write("- Machine learning and artificial intelligence")
st.write("- Reading technology blogs and articles")
