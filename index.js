<<<<<<< HEAD
function randomItem(table){
    return table[Math.random() * table.length];
}
=======
import { dummyData } from './data/dummyData.js';
import { getRandomItem } from './utils/helperFunctions.js';
>>>>>>> d707d5f012c5040f52ef7f25def9757681d083b4

const root = document.getElementById('root');
const ul = document.createElement('ul');

dummyData.forEach(monster => {

    const li = document.createElement('li');
    const randomItem = getRandomItem(monster.lootTable).treasureName;

    li.textContent = `${monster.monsterRace} has dropped 1 ${randomItem}`;
    ul.appendChild(li);
})

root.appendChild(ul);