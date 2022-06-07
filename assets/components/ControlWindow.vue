<template>
    <div class="container" style="display: flex; justify-content: center;">
        <div class="control-element">
            <div class="control-buttons">
                <label>Score</label>
                <button @click="sortByScore(true)" class="btn btn-primary">10 ➝ 0</button>
                <button @click="sortByScore(false)" class="btn btn-primary">0 ➝ 10</button>
            </div>
            <div class="control-buttons">
                <label>Name</label>
                <button @click="sortByName(false)" class="btn btn-primary">A ➝ Z</button>
                <button @click="sortByName(true)" class="btn btn-primary">Z ➝ A</button>
            </div>
        </div>
        <div class="control-element">
            <label>Only scored:</label>
            <input id="scoredOnly" type="checkbox" @click="filterGamelist()"/>
        </div>        
        <div class="control-element">
            <label>Console:</label>
            <input @change="filterGamelist()" class="form-control" list="consoleListOptions" id="consoleOptionList" placeholder="Search console">
                <datalist id="consoleListOptions">
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
        <div class="control-element">
            <label>Search:</label>
            <input type="text" v-model="gameSearchValue" @keyup="filterGamelist()" class="form-control" placeholder="Search game">
        </div>
    </div>
</template>

<script>
    export default{
        
        data(){
            return {
                gameSearchValue: ""
            }
        },
        
        methods: {

            filterGamelist(filterString = this.gameSearchValue){
                let consoleValue = document.getElementById('consoleOptionList').value;
                let onlyScoredIsChecked = document.getElementById("scoredOnly").checked;
                let list = document.getElementById('game-gallery').children;
                list = Array.prototype.slice.call(list, 0);

                list.forEach(element => {
                    element.style["display"] = "block"
                    
                    if(element.getElementsByClassName('console')[0].innerHTML != consoleValue && consoleValue != ""){
                        element.style["display"] = "none"
                        return
                    }
                    if(onlyScoredIsChecked){
                        if(element.getElementsByClassName('ranking').length <= 0){
                            element.style["display"] = "none"
                            return
                        }
                    }
                    if(filterString != ""){
                        console.log(filterString)
                        if(!String(element.getElementsByClassName('title')[0].innerHTML).toLowerCase().includes(filterString.toLowerCase())){
                            element.style["display"] = "none"
                            return
                        }
                    }

                });
            },
            sortByScore(descending){
                let list = document.getElementById('game-gallery').children;
                list = Array.prototype.slice.call(list, 0);

                list.sort((a, b) => {
                    let aValue;
                    let bValue;

                    if(a.getElementsByClassName('ranking').length <= 0) aValue = 0;
                    else aValue = parseInt(a.getElementsByClassName('ranking')[0].innerHTML)
                    if(b.getElementsByClassName('ranking').length <= 0) bValue = 0;
                    else bValue = parseInt(b.getElementsByClassName('ranking')[0].innerHTML)

                    if(descending) return aValue < bValue ? 1 : -1
                    else return aValue > bValue ? 1 : -1
                })
                
                let parent = document.getElementById('game-gallery');
                parent.innerHTML = "";
                for(var i = 0; i < list.length; i++) {
                    parent.appendChild(list[i]);
                }
            },
            sortByName(descending){
                let list = document.getElementById('game-gallery').children;
                list = Array.prototype.slice.call(list, 0);

                if(descending) list.sort((a,b) => a.getElementsByClassName('title')[0].innerHTML < b.getElementsByClassName('title')[0].innerHTML ? 1 : -1)
                else list.sort((a,b) => a.getElementsByClassName('title')[0].innerHTML > b.getElementsByClassName('title')[0].innerHTML ? 1 : -1)

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

    label {
        font-size: 1.2rem;
        margin-right: 1rem;
        vertical-align: middle;
    }
    
    .btn {
        margin-right: 1rem
    }

    .control-element {
        display: flex;
        margin-left: 1rem;
        padding-left: 1rem;
        align-items: center;
        border-left: 2px solid var(--light-blue);
    }

@media only screen and (max-width: 768px) {
    .control-container {
        flex-wrap: wrap;
        justify-content: unset;
    }
    .control-element {
        padding-top: 1rem;
    }
}
</style>