Name: pam-authramp
Version: 0.9.1
Release: 1%{?dist}
Summary: The AuthRamp PAM module provides an account lockout mechanism based on the number of authentication failures.

License: GPL-3.0-or-later
URL: https://github.com/34N0/pam-authramp
Source0: https://github.com/34N0/pam-authramp/archive/refs/tags/v%{version}.tar.gz

BuildRequires: rust
BuildRequires: cargo
BuildRequires: pam-devel
BuildRequires: clang-devel

%description
The AuthRamp PAM (Pluggable Authentication Modules) module provides an account lockout mechanism
based on the number of authentication failures. It calculates a dynamic delay for subsequent
authentication attempts, increasing the delay with each failure to mitigate brute force attacks.

%prep
%autosetup

%build
cargo build -p lib -p cli --release

%install
install -D -p -m 755 target/release/authramp %{buildroot}%{_bindir}/authramp
install -D -p -m 755 target/release/libpam_authramp.so %{buildroot}%{_libdir}/security/libpam_authramp.so
install -D -p -m 644 examples/system-auth/authramp.conf %{buildroot}/etc/security/authramp.conf


%files
%license LICENSE
%doc README.md SECURITY.md
%{_bindir}/authramp
%{_libdir}/security/libpam_authramp.so
/etc/security/authramp.conf

%changelog
* Fri Jan 19 2024 34n0 <34n0@immerda.ch> - 0.9.1
- Initial spec file