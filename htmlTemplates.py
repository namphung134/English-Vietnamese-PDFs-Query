css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://images2.thanhnien.vn/Uploaded/thanhchau/2023_01_10/g-dragon-comeback1-2079.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://scontent.fsgn2-10.fna.fbcdn.net/v/t39.30808-6/391655586_3729951613958038_2040583842344314315_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_ohc=JuWeEsckOxEAX845l0F&_nc_ht=scontent.fsgn2-10.fna&oh=00_AfCld-I_Ws-x8ykdfwo1AwLvb-LcrIZ0BDR3Pd9gjKYefA&oe=65F752B6">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''