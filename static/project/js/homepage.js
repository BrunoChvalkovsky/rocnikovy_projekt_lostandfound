function clearFilters() {
    document.getElementById('location_id').selectedIndex = 0;
    document.getElementById('date_sort').selectedIndex = 0;
    document.querySelector('.filter-form').submit();
}
