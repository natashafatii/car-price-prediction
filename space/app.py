# app.py - FINAL WORKING VERSION
import gradio as gr
import pandas as pd
import numpy as np
import os

print("=" * 50)
print(" Car Price Prediction System")
print("=" * 50)

# Initialize variables
ml_loaded = False

# Try to load models
try:
    import joblib
    print("Attempting to load ML models...")
    
    # Check files
    model_files = ['encoder.pkl', 'scaler.pkl', 'lr_model.pkl']
    for f in model_files:
        if os.path.exists(f):
            print(f"✓ Found: {f}")
        else:
            print(f"✗ Missing: {f}")
    
    # Try loading
    if all(os.path.exists(f) for f in model_files):
        encoder = joblib.load('encoder.pkl')
        scaler = joblib.load('scaler.pkl')
        model = joblib.load('lr_model.pkl')
        ml_loaded = True
        print(" ML models loaded successfully!")
    else:
        print(" Missing model files. Using demo mode.")
        
except Exception as e:
    print(f" Error loading models: {e}")
    print(" Running in demo mode...")

def predict_price(brand, model_year, engine_size, mileage, fuel_type, transmission, owner_count):
    """Predict car price"""
    try:
        # Convert inputs
        model_year = float(model_year)
        engine_size = float(engine_size)
        mileage = float(mileage)
        owner_count = int(owner_count)
        
        if ml_loaded:
            # Try ML prediction
            try:
                # Create input arrays
                input_cat = [[brand, fuel_type, transmission]]
                input_num = [[model_year, engine_size, mileage, owner_count]]
                
                # Transform
                cat_encoded = encoder.transform(input_cat)
                num_scaled = scaler.transform(input_num)
                
                # Combine features
                features = np.hstack([cat_encoded, num_scaled])
                
                # Predict
                price = model.predict(features)[0]
                
                return f" **ML Prediction:** Rs {price:,.0f}"
            except Exception as e:
                print(f"ML prediction failed: {e}")
                # Fall back to demo mode
                pass
        
        # Demo mode calculation
        base_price = 1000000
        depreciation = (2024 - model_year) * 50000
        engine_bonus = engine_size * 200000
        mileage_penalty = mileage * 0.5
        transmission_bonus = 50000 if transmission == "Automatic" else 0
        owner_penalty = (owner_count - 1) * 30000
        
        price = base_price - depreciation + engine_bonus - mileage_penalty + transmission_bonus - owner_penalty
        price = max(200000, price)  # Minimum price
        
        if ml_loaded:
            return f" **Demo Prediction:** Rs {price:,.0f}"
        else:
            return f" **Prediction:** Rs {price:,.0f}\n\n*(Using demo calculation)*"
            
    except Exception as e:
        return f" **Error:** {str(e)}\nPlease check your input values."

# Create interface - REMOVED 'theme' parameter for Gradio 6.0.2 compatibility
with gr.Blocks(title="Car Price Predictor") as demo:
    gr.Markdown("#  Car Price Prediction System")
    gr.Markdown("### Bahria University, Lahore Campus")
    gr.Markdown("**Course:** CSL-487 - Introduction to Data Science Lab")
    
    with gr.Row():
        with gr.Column():
            brand = gr.Dropdown(
                choices=["Toyota", "Honda", "Suzuki", "Hyundai", "Kia", 
                        "BMW", "Audi", "Mercedes", "Ford", "Nissan"],
                value="Toyota",
                label="Car Brand"
            )
            
            year = gr.Slider(
                minimum=2000,
                maximum=2024,
                value=2020,
                step=1,
                label="Model Year"
            )
            
            engine = gr.Slider(
                minimum=0.8,
                maximum=5.0,
                value=2.0,
                step=0.1,
                label="Engine Size (L)"
            )
        
        with gr.Column():
            mileage = gr.Slider(
                minimum=0,
                maximum=300000,
                value=50000,
                step=1000,
                label="Mileage (km)"
            )
            
            fuel = gr.Dropdown(
                choices=["Petrol", "Diesel", "Hybrid"],
                value="Petrol",
                label="Fuel Type"
            )
            
            transmission = gr.Dropdown(
                choices=["Manual", "Automatic"],
                value="Automatic",
                label="Transmission"
            )
            
            owners = gr.Slider(
                minimum=1,
                maximum=5,
                value=1,
                step=1,
                label="Previous Owners"
            )
    
    # Predict button
    predict_btn = gr.Button("🚀 Predict Price", variant="primary")
    
    # Output
    output = gr.Markdown()
    
    # Examples
    gr.Examples(
        examples=[
            ["Toyota", 2020, 1.5, 50000, "Petrol", "Automatic", 1],
            ["Honda", 2018, 1.8, 80000, "Petrol", "Manual", 2],
            ["BMW", 2021, 3.0, 30000, "Diesel", "Automatic", 1]
        ],
        inputs=[brand, year, engine, mileage, fuel, transmission, owners],
        outputs=output,
        fn=predict_price
    )
    
    # Footer
    gr.Markdown("---")
    gr.Markdown("**Faculty:** Mr. Muhammad Umar Tariq")
    gr.Markdown("**Student:** Natasha")

    
    # Connect button
    predict_btn.click(
        fn=predict_price,
        inputs=[brand, year, engine, mileage, fuel, transmission, owners],
        outputs=output
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()
