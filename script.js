// https://raw.githubusercontent.com/B6Infinity/bigdudebot_141/master/users.json
// https://raw.githubusercontent.com/B6Infinity/bigdudebot_141/master/users.json



//fetching the data

let users;

fetch('./users.json').then(response => {
    return response.json();

}).then(data => {

    let _users = JSON.parse(JSON.stringify(data));
    console.log(_users);
    users = _users;

    main(users);
    




}).catch(err => {
    
    console.log(err);
    console.log("Could not fetch the database!");
    let loadingWheel = document.getElementById('loading_wheel');
    loadingWheel.remove();
    
    //create the warning prompt

    let warningPrompt = document.createElement('div');
    warningPrompt.id = 'failed_data';
    let warningLogo = document.createElement('div');
    warningLogo.id = 'warninglogo';

    let WarningLogoIcon = document.createTextNode('⚠');
    let failedTextPrompt = document.createTextNode('FAILED TO GET THE DATA...\nTRY AGAIN!');

    warningLogo.appendChild(WarningLogoIcon);
    warningPrompt.appendChild(warningLogo);

    warningPrompt.appendChild(failedTextPrompt);
    
    document.body.append(warningPrompt);


    // show the error message
});





//console.log(users);
//for (let id in users)



function calculateScore(level, xp){
    
    let score = xp;
    let endPoint = Math.pow(level+1, 4);
        
    //console.log(0/10);
    
    
    let str1 = '';
    
    if(score >= 1000){
        let front = String(Math.trunc(score/1000));
        let back = String(Math.trunc((score%1000)/10));
        if(back == '0'){
            str1 = front + 'K';
        }
        else{            
            str1 = front+'.'+back+'K';
        }
    }
    else{
        str1 = score;
    }

    let str2 = '';
    if(endPoint >= 1000){
        let front = String(Math.trunc(endPoint/1000));
        let back = String(Math.trunc((endPoint%1000)/10));

        if(back == '0'){
            str2 = front + 'K';
        }
        else{            
            str2 = front+'.'+back+'K';
        }
    }
    else{
        str2 = endPoint;
    }

    let ret = str1 + ' / ' + str2;
    console.log(ret);
    console.log(score + ' / ' + endPoint);
    return(ret);

}

//THE MATHEMATICAL CALCULATION BEHIND THE XP AD SHITTY PERCENT
function calculatePercentage(level, xp){
    
    //level = parseInt(level);
    //xp = parseInt(xp);
    
    let startPoint = Math.pow(level, 4);
    let endPoint = Math.pow(level+1, 4);
    
    endPoint = endPoint - startPoint;
    xp = xp - startPoint;
    startPoint = startPoint - startPoint;

    let percentage = String((xp/endPoint)*100);
    
    return(percentage);
}

// RECREATE THE CARD IN JS AND PUSH IT IN THE PAGE
function pushCard(users, uid){
        
    let CARD = document.createElement('div');
    CARD.className = 'cards_holder';


    let memberCard = document.createElement('div');
    memberCard.className = 'membercard';


    let dpSpan = document.createElement('span');
    dpSpan.className = 'dp_holder';


    let profilePic = document.createElement('img');
    profilePic.id = 'profile_pic';
    profilePic.src = users[uid].profile_pic;
    profilePic.alt = 'userdphere';
    profilePic.style = 'max-width: 82px;';

    dpSpan.appendChild(profilePic);
    memberCard.appendChild(dpSpan);

    let dataHolderDiv = document.createElement('div');
    dataHolderDiv.className = 'data_holder';

    let memberName = document.createElement('span');
    memberName.className = 'member_name';
    memberName.style = 'font-size: 35px;';
    let nameOfUser = document.createTextNode(users[uid].name);
    
    memberName.appendChild(nameOfUser);
    dataHolderDiv.appendChild(memberName);

    if(uid == '497084701337714689'){ //if B6's ID (aka server owner)
        let crownSpan = document.createElement('span');
        crownSpan.className = 'crownlogo';
        let crownLogo = document.createElement('img');
        crownLogo.src = 'https://www.nicepng.com/png/full/46-464368_owner-discord-emoji-discord.png'                   ;
        crownLogo.className = 'crown';
        crownSpan.appendChild(crownLogo);

        let serverOwnerspan = document.createElement('span');
        serverOwnerspan.className = 'server_owner';
        let Text = document.createTextNode('Server Owner');
        serverOwnerspan.appendChild(Text);
        crownSpan.appendChild(serverOwnerspan);

        dataHolderDiv.appendChild(crownSpan);

    }

    let rankNo = document.createElement('span');
    rankNo.className = 'rank_no';
    rankNo.style = "right: 0; float: right; font-size: 25px;";
    rank = users[uid].rank;
    rank = String(rank);
    if(rank.charAt(rank.length-1) == '1' && rank.slice(-2) != '11'){
        rank = '1st';
        memberCard.className = 'membercard_1';
    }
    else if(rank.charAt(rank.length-1) == '2' && rank.slice(-2) != '12'){
        rank = '2nd';
        memberCard.className = 'membercard_2';
    }
    else if(rank.charAt(rank.length-1) == '3' && rank.slice(-2) != '13'){
        rank = '3rd';
        memberCard.className = 'membercard_3';
    }
    else{
        rank = rank + 'th';
        
    }


    ranktxt = document.createTextNode(rank);
    rankNo.appendChild(ranktxt);

    dataHolderDiv.appendChild(rankNo);

    let levelNo = document.createElement('span');
    levelNo.className = 'level_no';
    let level = document.createTextNode('Level '+users[uid].level);
    levelNo.appendChild(level);

    dataHolderDiv.appendChild(levelNo);

    let Bar = document.createElement('span');
    Bar.className = 'bar';
    let XPG = document.createElement('span');
    XPG.className = 'xp';

    //let xp_percent = String(23); ///////////////////////////////////// THIS IS THE THINGY!!!!
    let xp_percent = calculatePercentage(users[uid].level, users[uid].experience);
    XPG.style = 'width: '+xp_percent+'%;';

    Bar.appendChild(XPG);
    dataHolderDiv.appendChild(Bar);

    let scoreSpan = document.createElement('span');
    scoreSpan.className = 'score';
    let Score = document.createTextNode(calculateScore(users[uid].level, users[uid].experience));

    scoreSpan.appendChild(Score);
    dataHolderDiv.appendChild(scoreSpan);
    memberCard.appendChild(dataHolderDiv);

    CARD.appendChild(memberCard);

    document.body.append(CARD);

}

function detectMob() {
    return ( ( window.innerWidth <= 800 ) && ( window.innerHeight <= 600 ) );
}

function pushFooter(){
    let footer = document.createElement('footer');
    footer.id = 'footer';
    let text = document.createTextNode('Website Powered by ');
    footer.appendChild(text);
    let broteenDas = document.createElement('a');
    broteenDas.text = 'Broteen Das';
    broteenDas.href = 'https://instagram.com/broteen_das';
    broteenDas.target = '_blank';
    footer.appendChild(broteenDas);
    brr = document.createElement('br');
    footer.appendChild(brr);
    let invText = document.createElement('a');
    invText.text = '\n\nJoin the TASK FORCE 141 Discord server now for more awesomeness!';
    invText.href = 'https://discord.com/invite/JPHSrZJ';
    footer.appendChild(invText);

    

    let clickMe = document.createElement('a');
    clickMe.text = 'Psst! Try Clicking me...!';
    clickMe.href = 'https://www.youtube.com/b6infinity';
    clickMe.target = '_blank';
    brr = document.createElement('br');
    footer.appendChild(brr);
    brr = document.createElement('br');
    footer.appendChild(brr);
    clickMe.style = 'font-size: 10px';
    clickMe.target = '_blank';

    footer.appendChild(clickMe);

    document.body.appendChild(footer);
}


function main(users){

    // id of THE BIG DUDE: 764773592620859403
    
    
    
    let members = 0;
    for(let id in users){
        if(id == "764773592620859403"){
            delete users[id];
        }
        members++;
    }

    console.log(members);



    // remove the loading wheel
    let loadingWheel = document.getElementById('loading_wheel');
    loadingWheel.remove();



    for(let i = 1; i<=members; i++){
        for(let id in users){
            if(users[id].rank == i){
                pushCard(users, id);
            }
        }
    }


    pushFooter();

    
    console.log(detectMob());
}