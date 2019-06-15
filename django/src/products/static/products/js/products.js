const renderProduct = ({slug, name}) => (
    `
    <div class="catalog__item">
        <a href="/products/${ slug }">${ name }</a>
    </div>
    `
);