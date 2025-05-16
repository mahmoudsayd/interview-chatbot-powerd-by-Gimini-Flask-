# job_descriptions.py

def get_job_description(role: str) -> str:
    role = role.lower() # Normalize role string for comparison

    # --- Existing Roles ---
    if role == "data scientist":
        return """
        We are looking for a Data Scientist to extract insights from large datasets using statistical methods and machine learning. 
        You will build predictive models, evaluate algorithms, and communicate findings to stakeholders. 
        Strong experience in Python, SQL, scikit-learn, and data visualization libraries is essential.
        Familiarity with NLP or computer vision is a plus.
        """
    elif role == "backend developer":
        return """
        We are hiring a Backend Developer responsible for designing and maintaining server-side logic, APIs, and databases. 
        You will work closely with frontend developers and DevOps to build scalable and secure systems. 
        Expertise in Python (Django/FastAPI), RESTful APIs, databases (PostgreSQL/MongoDB), and CI/CD practices is required.
        """
    elif role == "frontend developer":
        return """
        Seeking a Frontend Developer who is passionate about creating intuitive, responsive user interfaces. 
        You will work with designers and backend developers to build seamless web applications. 
        Proficiency in HTML, CSS, JavaScript, React (or Vue), and accessibility standards is required. 
        Experience with responsive design and frontend testing frameworks is a bonus.
        """
    elif role == "ai/ml engineer":
        return """
        We are looking for an AI/ML Engineer to design and deploy machine learning models for production. 
        You will work with data scientists and software engineers to bring AI solutions to real-world applications. 
        Required skills include TensorFlow or PyTorch, model optimization, data pipelines, and cloud deployment (GCP/Azure).
        Experience with LLMs or MLOps is highly valued.
        """
    elif role == "devops engineer":
        return """
        We need a DevOps Engineer to automate, monitor, and maintain scalable infrastructure for continuous integration and deployment. 
        You should have hands-on experience with Docker, Kubernetes, CI/CD pipelines (GitHub Actions/Jenkins), 
        infrastructure as code (Terraform), and cloud platforms like AWS or Azure. 
        Security, reliability, and performance optimization are critical responsibilities.
        """
    elif role == "mobile app developer":
        return """
        We're hiring a Mobile App Developer to create high-performance mobile applications for Android and iOS platforms. 
        You should be proficient in Flutter or React Native, with a good understanding of native APIs, UX principles, 
        and app store deployment. Familiarity with Firebase, push notifications, and performance testing is a plus.
        """
    elif role == "cybersecurity analyst":
        return """
        We’re seeking a Cybersecurity Analyst to protect our systems and data from unauthorized access and cyber threats. 
        Responsibilities include monitoring security alerts, conducting vulnerability assessments, and ensuring compliance with industry standards. 
        Experience with SIEM tools, incident response, penetration testing, and security frameworks (e.g., NIST, ISO 27001) is required.
        """

    # --- New Roles (30 added) ---
    elif role == "cloud architect":
        return """
        Designing and overseeing an organization's cloud computing strategy, including cloud adoption plans, cloud application design, 
        and cloud management and monitoring. Expertise in AWS, Azure, or GCP, and infrastructure as code (IaC) is crucial.
        """
    elif role == "data engineer":
        return """
        Building and maintaining scalable data pipelines, transforming and cleaning data for analysis and machine learning. 
        Proficient in ETL processes, SQL, Python/Scala, and big data technologies like Spark or Hadoop.
        """
    elif role == "ui/ux designer":
        return """
        Creating user-centered designs by understanding business requirements, user journeys, and feedback. 
        Proficient in design tools (Figma, Sketch, Adobe XD), wireframing, prototyping, and usability testing.
        """
    elif role == "product manager (tech)": # Note: keeping lowercase for matching, display name can be different
        return """
        Defining product vision, strategy, and roadmap for tech products. Works with engineering, design, and marketing 
        to launch and iterate on products. Strong analytical and communication skills needed.
        """
    elif role == "full stack developer":
        return """
        Developing both client-side and server-side software. Proficient in various languages (e.g., JavaScript, Python, Java), 
        frameworks (e.g., React, Node.js, Spring), databases, and DevOps practices.
        """
    elif role == "game developer":
        return """
        Designing and programming video games for various platforms. Expertise in game engines (Unity, Unreal Engine), 
        programming languages (C++, C#), and game design principles.
        """
    elif role == "qa engineer (software tester)":
        return """
        Ensuring software quality through manual and automated testing. Develops test plans, test cases, and executes tests 
        to identify bugs and issues before release. Familiarity with testing frameworks and bug tracking tools.
        """
    elif role == "network engineer":
        return """
        Designing, implementing, and managing an organization's network infrastructure. Includes routers, switches, firewalls, 
        and network monitoring tools. Strong understanding of TCP/IP, routing protocols, and network security.
        """
    elif role == "database administrator (dba)":
        return """
        Managing and maintaining company databases, ensuring data integrity, security, performance, and availability. 
        Expertise in specific database systems (e.g., Oracle, MySQL, SQL Server), backup, and recovery.
        """
    elif role == "solutions architect":
        return """
        Designing comprehensive technology solutions to meet specific business problems. Bridges the gap between technical 
        and business requirements, often involving multiple systems and technologies.
        """
    elif role == "marketing manager":
        return """
        Developing and executing marketing strategies to increase brand awareness and drive sales. Manages campaigns, 
        market research, content creation, and analyzes performance. Digital marketing skills are essential.
        """
    elif role == "sales representative":
        return """
        Identifying and pursuing sales leads, building client relationships, and closing deals to meet sales targets. 
        Strong communication, negotiation, and product knowledge are key.
        """
    elif role == "human resources manager":
        return """
        Overseeing all aspects of HR, including recruitment, employee relations, performance management, compensation and benefits, 
        and compliance. Requires strong interpersonal and organizational skills.
        """
    elif role == "business analyst":
        return """
        Analyzing business processes, identifying needs, and recommending solutions to improve efficiency and achieve goals. 
        Gathers requirements, creates documentation, and works with stakeholders.
        """
    elif role == "operations manager":
        return """
        Managing daily operations to ensure efficiency and productivity. Oversees production, logistics, quality control, 
        and process improvement. Strong leadership and problem-solving skills.
        """
    elif role == "project manager (general)":
        return """
        Planning, executing, and closing projects within scope, budget, and timeline. Manages resources, risks, 
        and stakeholder communication. PMP or similar certification is a plus.
        """
    elif role == "financial analyst":
        return """
        Analyzing financial data, creating financial models, and providing insights to support business decisions. 
        Prepares reports, forecasts, and evaluates investment opportunities.
        """
    elif role == "customer success manager":
        return """
        Building relationships with customers to ensure they achieve their desired outcomes while using the company's products or services. 
        Focuses on retention, satisfaction, and upselling.
        """
    elif role == "supply chain manager":
        return """
        Overseeing and managing the company's overall supply chain and logistics strategy to maximize efficiency and productivity. 
        Involves procurement, inventory management, warehousing, and transportation.
        """
    elif role == "graphic designer":
        return """
        Creating visual concepts, by hand or using computer software, to communicate ideas that inspire, inform, or captivate consumers. 
        Develops overall layout and production design for advertisements, brochures, magazines, and corporate reports.
        """
    elif role == "content writer / copywriter":
        return """
        Writing clear, compelling, and original content for various platforms like websites, blogs, social media, and marketing materials. 
        Strong research, grammar, and storytelling skills.
        """
    elif role == "video editor":
        return """
        Assembling recorded raw material into a finished product suitable for broadcasting. The material may include camera footage, 
        dialogue, sound effects, graphics and special effects. Proficiency in editing software (e.g., Adobe Premiere Pro, Final Cut Pro).
        """
    elif role == "social media manager":
        return """
        Developing and implementing social media strategies to increase online presence and improve marketing and sales efforts. 
        Creates content, manages communities, and analyzes social media metrics.
        """
    elif role == "registered nurse (rn)":
        return """
        Providing direct patient care, administering medications, educating patients and families, and collaborating with healthcare teams. 
        Requires state licensure and strong clinical skills.
        """
    elif role == "medical researcher":
        return """
        Conducting studies and experiments to advance medical knowledge, develop new treatments, or improve public health. 
        Requires a strong scientific background and analytical skills.
        """
    elif role == "lab technician":
        return """
        Performing laboratory tests and analyses on biological samples, chemicals, or other substances. Maintains lab equipment, 
        records data, and follows safety protocols. Attention to detail is crucial.
        """
    elif role == "technical writer":
        return """
        Creating clear and concise documentation for technical products or processes, such as user manuals, API guides, 
        and internal SOPs. Ability to explain complex information simply.
        """
    elif role == "recruiter / talent acquisition specialist":
        return """
        Sourcing, screening, and interviewing candidates to fill open positions within an organization. 
        Manages the hiring process and builds a talent pipeline.
        """
    elif role == "systems administrator":
        return """
        Maintaining and upgrading computer systems and networks. Responsible for server management, user support, 
        system security, and ensuring operational efficiency.
        """
    elif role == "customer support specialist":
        return """
        Assisting customers with inquiries, issues, and requests regarding products or services. Provides information, 
        troubleshoots problems, and ensures customer satisfaction via various channels.
        """
    else:
        return "No job description available for this role."