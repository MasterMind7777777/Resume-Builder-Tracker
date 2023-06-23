$(document).ready(function () {
    var gridSize = 20; // Adjust the grid size as needed


    // Adjust section positions on page load
    $('.section').each(function () {
        var section = $(this);
        var sectionOffset = section.offset();
        var adjustedOffset = {
            top: Math.round(sectionOffset.top / gridSize) * gridSize,
            left: Math.round(sectionOffset.left / gridSize) * gridSize
        };

        section.offset(adjustedOffset);
    });

    // Enable draggable functionality for sections
    $('.section').draggable({
        containment: '.resume.container', // Restrict dragging within the resume container
        handle: '.drag-handle', // Use a specific element as the handle for dragging
        scroll: false, // Disable scrolling while dragging
        grid: [gridSize, gridSize], // Set the grid size for dragging
        stop: function (event, ui) {
            // Check for overlap with other sections
            var draggedSection = $(this);
            var draggedSectionOffset = draggedSection.offset();

            $('.section').each(function () {
                var otherSection = $(this);

                // Skip the dragged section itself
                if (otherSection.is(draggedSection)) {
                    return;
                }

                var otherSectionOffset = otherSection.offset();
                var overlapX =
                    draggedSectionOffset.left < otherSectionOffset.left + otherSection.outerWidth() &&
                    draggedSectionOffset.left + draggedSection.outerWidth() > otherSectionOffset.left;
                var overlapY =
                    draggedSectionOffset.top < otherSectionOffset.top + otherSection.outerHeight() &&
                    draggedSectionOffset.top + draggedSection.outerHeight() > otherSectionOffset.top;

                if (overlapX && overlapY) {
                    // Sections are overlapping, adjust the position

                    // Calculate the new position
                    var newPosition = {
                        top: draggedSectionOffset.top,
                        left: draggedSectionOffset.left,
                    };

                    // Adjust the position to move the section away from the overlapping section
                    if (draggedSectionOffset.top < otherSectionOffset.top) {
                        newPosition.top = otherSectionOffset.top - draggedSection.outerHeight() - gridSize;
                    } else {
                        newPosition.top = otherSectionOffset.top + otherSection.outerHeight() + gridSize;
                    }

                    // Apply the new position
                    draggedSection.offset(newPosition);
                    draggedSectionOffset = newPosition;
                }
            });
        },
    });

    // Enable resizable functionality for sections using the resize handles
    $('.section').each(function () {
        var section = $(this);
        var verticalHandle = section.find('.resize-handle-vertical');

        var originalWidth = section.width();
        var originalHeight = section.height();
        var originalX, originalY;

        verticalHandle.on('mousedown', function (event) {
            event.preventDefault();
            originalX = event.pageX;
            originalWidth = section.width();

            $(document).on('mousemove', function (event) {
                function displayTextWidth(text, font) {
                    let canvas = displayTextWidth.canvas || (displayTextWidth.canvas = document.createElement('canvas'));
                    let context = canvas.getContext('2d');
                    context.font = font;
                    let metrics = context.measureText(text);
                    return metrics.width;
                }

                var deltaX = event.pageX - originalX;
                var newWidth = originalWidth + deltaX;

                // Apply grid to resize width
                newWidth = Math.round(newWidth / gridSize) * gridSize;

                // Check if the new width exceeds the container's width or goes beyond the left edge
                var container = section.closest('.resume.container');
                var containerMargin = parseInt(container.css('padding'), 10);
                var containerWidth = container.width();
                var containerLeftOffset = container.offset().left;

                var sectionLeft = section.offset().left;
                var sectionRight = sectionLeft + newWidth;

                if (
                    sectionLeft >= containerLeftOffset &&
                    sectionRight <= containerLeftOffset + containerMargin + containerWidth
                ) {
                    section.css('width', newWidth + 'px');

                    // Check if the text inside the sub-section exceeds its width
                    var subSection = section.find('.sub-section');
                    var paragraphs = subSection.find('p');

                    // Initialize a variable to store the maximum width
                    var maxWidth = 0;

                    // Iterate through each <p> element
                    paragraphs.each(function () {
                        // Get the text content of the <p> element
                        var text = $(this).text();

                        // Calculate the width of the text using the displayTextWidth function
                        var width = displayTextWidth(text, section.find('p').css('font'));

                        // Update the maximum width if necessary
                        if (width > maxWidth) {
                            maxWidth = width;
                        }
                    });

                    // Enforce the minimum width based on the longest text line
                    var minSectionWidth = maxWidth;
                    if (newWidth < minSectionWidth) {
                        section.css('width', minSectionWidth + 'px');
                    }
                }
            });

            $(document).on('mouseup', function () {
                $(document).off('mousemove');
                $(document).off('mouseup');
            });
        });
    });

    // Handle form submission to save adjusted layout
    $('form').submit(function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Generate the adjusted layout HTML dynamically
        var adjustedLayout = $('.resume.container').html();

        // Create the data object to send in the request
        var data = {
            layout_id: 123, // Replace with the actual layout ID
            adjusted_layout: adjustedLayout,
        };

        // Send the AJAX request to save the adjusted layout
        $.ajax({
            type: 'POST',
            url: '/api_v1/resumes/save_adjusted_layout/',
            data: data,
            success: function (response) {
                // Handle the success response
                console.log(response);
            },
            error: function (xhr, textStatus, errorThrown) {
                // Handle the error response
                console.error(errorThrown);
            },
        });
    });
});