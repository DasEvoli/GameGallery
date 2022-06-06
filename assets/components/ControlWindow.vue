<template>
    <div class="container">
        <div class="control-container">
            <h2>Sort by:</h2>
            <div class="control-buttons">
                <label>Score</label>
                <button @click="sortByScore(true)" class="btn btn-primary">10 ... 0</button>
                <button @click="sortByScore(false)" class="btn btn-primary">0 ... 10</button>
            </div>
            <div class="control-buttons">
                <label>Name</label>
                <button @click="sortByScore()" class="btn btn-primary">A ... Z</button>
                <button @click="sortByScore()" class="btn btn-primary">Z ... A</button>
            </div>
        </div>
        <div class="control-container">
            <label>Only played:</label>
            <input id="playedOnly" type="checkbox" @click="filterGamelist()"/>
        </div>        
        <div class="control-container">
            <label>Console:</label>
            <input @change="filterGamelist()" class="form-control" list="datalistOptions" id="consoleOptionList" placeholder="Type to search...">
                <datalist id="datalistOptions">
                    <option value="3DS Downloads"/>
                    <option value="Amiga"/>
                    <option value="Amiga CD32"/>
                    <option value="Atari 2600"/>
                    <option value="C64"/>
                    <option value="CDi"/>
                    <option value="DreamCast"/>
                    <option value="DSi Ware"/>
                    <option value="G&W"/>
                    <option value="GB"/>
                    <option value="GBA"/>
                    <option value="GBC"/>
                    <option value="GCN"/>
                    <option value="Genesis"/>
                    <option value="GG"/>
                    <option value="Jaguar"/>
                    <option value="Lynx"/>
                    <option value="N64"/>
                    <option value="NDS"/>
                    <option value="NES"/>
                    <option value="Odyssey²"/>
                    <option value="PC"/>
                    <option value="PS1"/>
                    <option value="PS2"/>
                    <option value="PS3"/>
                    <option value="PS4"/>
                    <option value="PSP"/>
                    <option value="Q&Q²"/>
                    <option value="Saturn"/>
                    <option value="Sega CD"/>
                    <option value="SMS"/>
                    <option value="SNES"/>
                    <option value="SNES Mini"/>
                    <option value="Switch"/>
                    <option value="Tiger"/>
                    <option value="Wii U"/>
                    <option value="Wii"/>
                    <option value="WiiWare"/>
                    <option value="XB360"/>
                    <option value="XBONE"/>
                    <option value="XBOX"/>
                </datalist>
        </div>

    </div>
</template>

<script>
    export default{
        methods: {
            filterGamelist(){
                let consoleValue = document.getElementById('consoleOptionList').value;
                let onlyPlayedIsChecked = document.getElementById("playedOnly").checked;
                let list = document.getElementById('game-gallery').children;
                list = Array.prototype.slice.call(list, 0);
                list.forEach(element => {
                    element.style["display"] = "block"
                    if(element.getElementsByClassName('console')[0].innerHTML == consoleValue || consoleValue == ""){
                        if(onlyPlayedIsChecked){
                            if(element.getElementsByClassName('ranking')[0].innerHTML == 0){
                                element.style["display"] = "none"
                                return
                            }
                        }
                    }
                    else {
                        element.style["display"] = "none"
                        return
                    }
                });
            },

            sortByScore(descending){
                let list = document.getElementById('game-gallery').children;
                list = Array.prototype.slice.call(list, 0);
                if(descending) list.sort((a, b) => parseInt(a.getElementsByClassName('ranking')[0].innerHTML) < parseInt(b.getElementsByClassName('ranking')[0].innerHTML) ? 1 : -1)
                else list.sort((a, b) => parseInt(a.getElementsByClassName('ranking')[0].innerHTML) > parseInt(b.getElementsByClassName('ranking')[0].innerHTML) ? 1 : -1)
                
                let parent = document.getElementById('game-gallery');
                parent.innerHTML = "";
                for(var i = 0; i < list.length; i++) {
                    parent.appendChild(list[i]);
                }
            }
        }
    }
</script>

<style scoped>
    .container {
        background-color: #008eff69;
        width: 100%;
        height: 100%;
    }
    
    label {
        font-size: 1.5rem;
        margin-right: 1rem;
    }
    
    .btn {
        margin-right: 1rem
    }
</style>