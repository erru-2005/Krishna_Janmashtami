# Krishna Janmashtami 2025 Website

A responsive, modern website for celebrating Krishna Janmashtami with comprehensive mobile-first design and cross-device compatibility.

## 🌟 Features

### Responsive Design
- **Mobile-First Approach**: Optimized for all screen sizes from 320px to 4K displays
- **Progressive Enhancement**: Works on all devices with graceful degradation
- **Touch-Friendly Interface**: Optimized for touch devices with proper touch targets
- **Cross-Browser Compatibility**: Works on all modern browsers

### Screen Size Support
- **Mobile Phones**: 320px - 575px (portrait and landscape)
- **Tablets**: 576px - 991px (portrait and landscape)
- **Desktop**: 992px - 1199px
- **Large Desktop**: 1200px+ (including 4K displays)

### Performance Optimizations
- **Service Worker**: Offline functionality and caching
- **Lazy Loading**: Images load only when needed
- **Optimized Assets**: Compressed images and minified code
- **Fast Loading**: Optimized for slow connections

### Accessibility Features
- **Screen Reader Support**: Proper ARIA labels and semantic HTML
- **Keyboard Navigation**: Full keyboard accessibility
- **High Contrast**: Supports high contrast mode
- **Reduced Motion**: Respects user's motion preferences

## 📱 Responsive Breakpoints

### Extra Small (Mobile)
```css
@media (max-width: 575.98px)
```
- Optimized for mobile phones
- Single column layouts
- Larger touch targets
- Simplified navigation

### Small (Large Mobile/Tablet)
```css
@media (min-width: 576px) and (max-width: 767.98px)
```
- Landscape mobile optimization
- Two-column layouts where appropriate
- Improved button sizing

### Medium (Tablet)
```css
@media (min-width: 768px) and (max-width: 991.98px)
```
- Tablet-optimized layouts
- Enhanced navigation
- Better content spacing

### Large (Desktop)
```css
@media (min-width: 992px) and (max-width: 1199.98px)
```
- Desktop layouts
- Full navigation menu
- Optimal content width

### Extra Large (Large Desktop)
```css
@media (min-width: 1200px)
```
- Large screen optimization
- Maximum content width
- Enhanced visual effects

## 🎨 Design Features

### Typography
- **Responsive Font Sizing**: Text scales appropriately for each screen size
- **Readable Line Lengths**: Optimized for comfortable reading
- **Hierarchy**: Clear visual hierarchy maintained across devices

### Layout
- **Flexible Grid System**: Bootstrap-based responsive grid
- **Fluid Containers**: Content adapts to screen width
- **Consistent Spacing**: Maintained across all breakpoints

### Interactive Elements
- **Hover Effects**: Desktop-only hover states
- **Touch Feedback**: Visual feedback for touch interactions
- **Smooth Transitions**: CSS transitions for better UX

## 🚀 Technical Implementation

### CSS Features
- **CSS Grid & Flexbox**: Modern layout techniques
- **CSS Custom Properties**: Consistent theming
- **Media Queries**: Comprehensive breakpoint system
- **Viewport Units**: Responsive sizing

### JavaScript Enhancements
- **Responsive Navigation**: Mobile menu handling
- **Dynamic Content**: Adjusts based on screen size
- **Performance Monitoring**: Optimized event handling
- **Touch Gestures**: Swipe support for mobile

### Progressive Web App Features
- **Service Worker**: Offline functionality
- **App Manifest**: Installable on mobile devices
- **Fast Loading**: Optimized asset delivery
- **Background Sync**: Enhanced user experience

## 📋 Browser Support

### Fully Supported
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Partially Supported
- Internet Explorer 11 (basic functionality)
- Older mobile browsers (graceful degradation)

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Krishna_Janmashtami
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the website**
   - Open `http://localhost:5000` in your browser
   - Test on different devices and screen sizes

## 📱 Testing Responsive Design

### Manual Testing
1. **Browser Developer Tools**
   - Use device simulation in Chrome DevTools
   - Test all breakpoints (320px to 4K)
   - Check both portrait and landscape orientations

2. **Real Devices**
   - Test on actual mobile phones
   - Test on tablets (iPad, Android tablets)
   - Test on different desktop screen sizes

3. **Cross-Browser Testing**
   - Test on Chrome, Firefox, Safari, Edge
   - Test on mobile browsers (Safari iOS, Chrome Android)

### Automated Testing
- Use tools like BrowserStack or LambdaTest
- Implement responsive testing with Selenium
- Use Lighthouse for performance testing

## 🎯 Performance Metrics

### Target Metrics
- **First Contentful Paint**: < 1.5s
- **Largest Contentful Paint**: < 2.5s
- **Cumulative Layout Shift**: < 0.1
- **First Input Delay**: < 100ms

### Optimization Techniques
- **Image Optimization**: WebP format with fallbacks
- **Code Splitting**: Load only necessary JavaScript
- **Caching Strategy**: Service worker caching
- **Minification**: Compressed CSS and JavaScript

## 🔧 Customization

### Colors
The website uses CSS custom properties for easy theming:
```css
:root {
    --primary-color: #FF6B35;
    --secondary-color: #4A90E2;
    --accent-color: #FFD700;
    --dark-color: #2C3E50;
    --light-color: #ECF0F1;
}
```

### Typography
Font sizes are responsive and can be adjusted in the CSS:
```css
.responsive-text {
    font-size: clamp(1rem, 2.5vw, 1.5rem);
}
```

### Layout
Grid layouts can be customized using Bootstrap classes:
```html
<div class="col-lg-4 col-md-6 col-sm-12">
    <!-- Content -->
</div>
```

## 📞 Support

For questions or issues with the responsive design:
- Check the browser console for JavaScript errors
- Verify CSS is loading correctly
- Test on different devices and browsers
- Review the responsive breakpoints

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with ❤️ for Krishna Janmashtami 2025**
