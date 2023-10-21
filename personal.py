import streamlit as st
st.image('images/logo.png')
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
    name = st.text_input('FULL NAME : ' , max_chars=50)

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

is_clicked = st.button('Next')

if is_clicked : 
    if (name == '') | (phone == '') | (email == '') | (facebook == ''):
        st.write('Please , Enter All Personal information')
    else : 
        if (not email.endswith('@gmail.com') ) or (len(email) <= len('@gmail.com')) :
            st.write("E-Mail must be gmail account")    