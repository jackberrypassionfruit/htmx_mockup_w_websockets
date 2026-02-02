const testFunc = () => console.log('It worked!');

const toggleDisabledTagById = (tagID) => {
    document.getElementById(tagID).disabled = 
        !document.getElementById(tagID).disabled;
}