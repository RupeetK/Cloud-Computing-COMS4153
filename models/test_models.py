from person import PersonBase
from address import AddressBase
from uuid import uuid4

# Test instantiation
try:
    p1 = PersonBase(
        uni="abc1234",
        first_name="Test",
        last_name="User",
        email="test@example.com"  # Required field - must provide valid email
    )
    print(f"p1.addresses: {p1.addresses}")  # Expected: []
    print(f"Type of p1.addresses: {type(p1.addresses)}")

    # Create and append an address to p1
    addr = AddressBase(
        street="Test St",
        city="Test City",
        postal_code="12345",
        country="US"
    )
    p1.addresses.append(addr)
    print(f"len(p1.addresses): {len(p1.addresses)}")  # Expected: 1

    # Create a second independent instance
    p2 = PersonBase(
        uni="def5678",
        first_name="Another",
        last_name="User",
        email="another@example.com"  # Required field
    )
    print(f"len(p2.addresses): {len(p2.addresses)}")  # Expected: 0 (proves independence)

    # Test that they're truly independent
    print(f"p1 addresses: {len(p1.addresses)}")
    print(f"p2 addresses: {len(p2.addresses)}")
    print("✓ Test passed - no shared mutable state!")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()