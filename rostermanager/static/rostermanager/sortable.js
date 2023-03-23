$(function() {
    $( ".connectedSortable" ).sortable({
        connectWith: ".connectedSortable",
        update: function(event, ui) {
            // Get the new order of the items
            var new_order = $(this).sortable('toArray');

            // Send the new order to the server
            $.ajax({
                url: "{% url 'update_order' %}",
                type: "POST",
                data: {'new_order': new_order},
                success: function() {
                    // Success message
                },
                error: function() {
                    // Error message
                }
            });
        }
    });
});



