document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const locationSelect = document.getElementById('location-select');
    const newLocationInput = document.getElementById('new-location');
    
    locationSelect.addEventListener('change', function() {
        if (this.value) {
            newLocationInput.value = '';
        }
    });
    
    newLocationInput.addEventListener('input', function() {
        if (this.value.trim()) {
            locationSelect.value = '';
        }
    });
    
    form.addEventListener('submit', function(e) {
        const hasExisting = locationSelect.value !== '';
        const hasNew = newLocationInput.value.trim() !== '';
        
        if (!hasExisting && !hasNew) {
            e.preventDefault();
            alert('Please select an existing location or enter a new one.');
            return false;
        }
        
        if (hasExisting && hasNew) {
            e.preventDefault();
            alert('Please choose either an existing location OR enter a new one, not both.');
            return false;
        }
    });
});