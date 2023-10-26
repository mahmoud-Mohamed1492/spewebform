import streamlit as st
import webbrowser
import pymysql
HOST = "sql12.freesqldatabase.com"
PORT = 3306
USER = "sql12654927"
PASSWARD = "SCNABuhY2G"
DATABASE = "sql12654927"
# database connection
connection = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWARD, database=DATABASE)

cursor = connection.cursor()
# some other statements  with the help of cursor

#########################################################################
st.image('logo.png')
st.markdown("""
<style>
img{
            display: block;
            margin-left: 30px;
            margin-right: 50px;
           width:750px;
            height:200px;
           
}            
</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class = 'container1'>            
<p class = 'title'>SPE SU SC Online Recruitment</p>
</div>
          
           
<style>
.title{
        text-align: center; 
        font-family:Cooper Black;
        color:#ffffff;
        font-size: 35px; 
}
.container1{
        width : 750px;
        border: 3px solid black;
        padding: 0px 1px 0px 1px ;
        margin: 0px 10px 0px 10px;
        border-radius: 15px;
        background : black;  
}                                        
</style>         
""" , unsafe_allow_html=True)

st.markdown("""
<div class = 'container2'>                           
<p class = 'section'>Personal Information</p>
</div> 
            
<style>
.container2{
            width : 750px;
        border: 3px solid blue;
        padding: 0px 1px 0px 1px ;
        margin: 20px 10px 0px 10px;
        border-radius: 15px 15px 0 0;
        background : blue;   
} 
.section{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 40px; 
} 
</style>

""" , unsafe_allow_html=True)

st.markdown("""
<div class = 'container3'>            
<p class = 'note'>Please answer all of the following questions</p>
</div> 
            
<style>
.note{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 30px;    
}   
.container3{
            width : 750px;
        border: 3px solid lightblue;
        padding: 1px 5px 0px 1px ;
        margin: 0px 10px 30px 10px;
        border-radius: 0 0 15px 15px ;
        background : lightblue;   
} 
</style>

""" , unsafe_allow_html=True)
# -------------------------- Name --------------------------------------------------
with st.container():
    name = str(st.text_input('FULL NAME : ' , max_chars=50)).lower()
    
    

st.markdown(
        """
<style>
    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
    width: 750px;
border: 3px solid black;
padding: 25px 25px ;
margin: 5px 0px 15px 10px;
border-radius: 25px  ;
box-shadow: 5px 5px lightblue;
    }
</style>
""" , unsafe_allow_html=True)
# --------------------------------------------------------------------------------------

# -------------------------- Mobile Phone --------------------------------------------------
with st.container():
    phone = st.text_input('Mobile Phone : ' , max_chars=13)

# --------------------------------------------------------------------------------------

# -------------------------- Gmail --------------------------------------------------
with st.container():
    email = st.text_input('E-Mail : ')

# --------------------------------------------------------------------------------------

# -------------------------- Facebook Link --------------------------------------------------
with st.container():
    facebook = st.text_input('Facebook Link : \n\n https://www.facebook.com/' )

# --------------------------------------------------------------------------------------

st.markdown("""
<div class = 'container2'>                           
<p class = 'section'>Educational Information</p>
</div> 
            
<style>
.container2{
            width : 750px;
        border: 3px solid blue;
        padding: 0px 1px 0px 1px ;
        margin: 20px 10px 0px 10px;
        border-radius: 15px 15px 0 0;
        background : blue;   
} 
.section{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 40px; 
} 
</style>

""" , unsafe_allow_html=True)

st.markdown("""
<div class = 'container3'>            
<p class = 'note'>Please answer all of the following questions</p>
</div> 
            
<style>
.note{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 30px;    
}   
.container3{
            width : 750px;
        border: 3px solid lightblue;
        padding: 1px 5px 0px 1px ;
        margin: 0px 10px 30px 10px;
        border-radius: 0 0 15px 15px ;
        background : lightblue;   
} 
</style>

""" , unsafe_allow_html=True)


#--------------------------------------- University ----------------------------------------------------
with st.container():
    university = st.text_input('University : '  , 'Suez University')

st.markdown(
        """
<style>
    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
    width: 750px;
border: 3px solid black;
padding: 25px 25px ;
margin: 5px 0px 15px 10px;
border-radius: 25px  ;
box-shadow: 5px 5px lightblue;
    }
</style>
""" , unsafe_allow_html=True)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------- Faculty ----------------------------------------------------
with st.container():
    faculty = st.text_input('Faculty : ' )

#--------------------------------------------------------------------------------------------------------

#--------------------------------------- Department ----------------------------------------------------
with st.container():
    department = st.text_input('Department : ' )

#--------------------------------------------------------------------------------------------------------

#--------------------------------------- academic Year ----------------------------------------------------
with st.container():
    level = st.radio(
        "Academic Year : ",
        ["Level 0", "Level 1", "Level 2" , "Level 3" , "Level 4"])
        
#--------------------------------------------------------------------------------------------------------

st.markdown("""
<div class = 'container2'>                           
<p class = 'section'>About SPE Suez</p>
</div> 
            
<style>
.container2{
            width : 750px;
        border: 3px solid blue;
        padding: 0px 1px 0px 1px ;
        margin: 20px 10px 0px 10px;
        border-radius: 15px 15px 0 0;
        background : blue;   
} 
.section{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 40px; 
} 
</style>

""" , unsafe_allow_html=True)

st.markdown("""
<div class = 'container3'>            
<p class = 'note'>Please answer all of the following questions</p>
</div> 
            
<style>
.note{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 30px;    
}   
.container3{
            width : 750px;
        border: 3px solid lightblue;
        padding: 1px 5px 0px 1px ;
        margin: 0px 10px 30px 10px;
        border-radius: 0 0 15px 15px ;
        background : lightblue;   
} 
</style>

""" , unsafe_allow_html=True)

#------------------------------ Question --------------------------------
with st.container():
    q1 = st.text_area("Do you have previous experience to apply for volunteering work ?\n\nIf you have, please explain it in detail.")

st.markdown(
        """
<style>
    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
    width: 750px;
border: 3px solid black;
padding: 25px 25px ;
margin: 5px 0px 15px 10px;
border-radius: 25px  ;
box-shadow: 5px 5px lightblue;
    }
</style>
""" , unsafe_allow_html=True)
#------------------------------------------------------------------------

#------------------------------ Question --------------------------------
with st.container():
    q2 = st.text_area("Why are you applying for SPE Suez Student Chapter ?")


#------------------------------------------------------------------------

#------------------------------ Question --------------------------------
with st.container():
    q3 = st.text_area("Do you think that you will benefit from joining SPE and how ?")
#------------------------------------------------------------------------


st.markdown("""
<div class = 'container2'>                           
<p class = 'section'>About Committee</p>
</div> 
            
<style>
.container2{
            width : 750px;
        border: 3px solid blue;
        padding: 0px 1px 0px 1px ;
        margin: 20px 10px 0px 10px;
        border-radius: 15px 15px 0 0;
        background : blue;   
} 
.section{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 40px; 
} 
</style>

""" , unsafe_allow_html=True)

st.markdown("""
<div class = 'container3'>            
<p class = 'note'>Please answer all of the following questions</p>
</div> 
            
<style>
.note{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 30px;    
}   
.container3{
            width : 750px;
        border: 3px solid lightblue;
        padding: 1px 5px 0px 1px ;
        margin: 0px 10px 30px 10px;
        border-radius: 0 0 15px 15px ;
        background : lightblue;   
} 
</style>

""" , unsafe_allow_html=True)

#--------------------------------------------- Committee -------------------------------------------
committees = ('Data Analysis' , 'Web Development' , 'Android App' , 'Social Media' , 'Multimedia' , 'Direct Marketing' , 'Energy4me' , 'Extracurricular' , 'Logistics' , 'OC' , 'Magazine Editing' , 'Magazine Design' , 'International Relations (IR)' , 'Human Resources Development (HRD)' , 'Human Resources Management (HRM)')
with st.container():
    committee = st.selectbox('Which committee do you want to join ?' , committees)

st.markdown(
        """
<style>
    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
    width: 750px;
border: 3px solid black;
padding: 25px 25px ;
margin: 5px 0px 15px 10px;
border-radius: 25px  ;
box-shadow: 5px 5px lightblue;
    }
</style>
""" , unsafe_allow_html=True)
#---------------------------------------------------------------------------------------------------------

#--------------------------------------------- q4 -------------------------------------------

with st.container():
    q4 = st.text_area('Why did you choose this committee ?' )

#---------------------------------------------------------------------------------------------------------

#--------------------------------------------- q4 -------------------------------------------

with st.container():
    q5 = st.text_area('What do you know about the responsibilities of the committee you are applying for ? \n\n(Be specific)' )

#---------------------------------------------------------------------------------------------------------

#--------------------------------------------- q4 -------------------------------------------

with st.container():
    comment = st.text_area('One Space')

#---------------------------------------------------------------------------------------------------------

is_clicked = st.button('Submit')
st.markdown("""
<style>
            .st-emotion-cache-1bv3lpx {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 38.4px;
    margin: 0px 32%;
    line-height: 1.6;
    color: inherit;
    width: 300px;
    user-select: none;
    background-color: rgb(255, 255, 255);
    border: 1px solid rgba(49, 51, 63, 0.2);
            }
            </style>
""" , unsafe_allow_html=True)
if is_clicked:
    if (name == "") | (phone == "") | (email == "") | (facebook == "") | (university == "") | (faculty == "") | (department == "") | (level == "") | (committee == "") | (q1 == "") | (q2 == "") | (q3 == "") | (q4 == "") | (q5 == "") :
        st.write('Please , Answer All Questions')
        if comment == "" :
            comment = 'No Comment'
    else : 
        cursor.execute(f"INSERT INTO spe_form1 (FULL_NAME , phone , email ,facebook_link, university , faculty	 , department , level , q1 ,q2 , q3 , committee , q4 , q5 , space) values ( '{name}' , '{phone}' , '{email}' , '{facebook}' , '{university}', '{faculty}', '{department}', '{level}', '{q1}', '{q2}', '{q3}', '{committee}', '{q4}', '{q5}', '{comment}' )")
        connection.commit()
        connection.close()
        st.write('Your Form is submitted')
        webbrowser.open_new('https://spewebform-bsbze48qnkznyfqn3xw6ts.streamlit.app/' )
              







