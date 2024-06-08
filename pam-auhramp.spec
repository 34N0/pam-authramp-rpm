%bcond_without check

Name: pam-authramp
Version: 1.0
Release: 1%{?dist}
Summary: The AuthRamp PAM module provides an account lockout mechanism based on the number of authentication failures.

License: GPL-3.0-or-later
URL: https://github.com/34N0/pam-authramp
Source0: https://github.com/34N0/pam-authramp/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo-rpm-macros >= 24
BuildRequires: pam-devel
BuildRequires: clang-devel


%global _description %{expand:
The AuthRamp PAM (Pluggable Authentication Modules) module provides an account lockout mechanism
based on the number of authentication failures. It calculates a dynamic delay for subsequent
authentication attempts, increasing the delay with each failure to mitigate brute force attacks.
}

%description %{_description}

%prep
%autosetup -n pam-authramp-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
cargo build --release
cargo build --release -p cli

%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -D -p -m 755 target/release/authramp %{buildroot}%{_bindir}/authramp
install -D -p -m 755 target/release/libpam_authramp.so %{buildroot}%{_libdir}/security/libpam_authramp.so
install -D -p -m 644 examples/system-auth/authramp.conf %{buildroot}/etc/security/authramp.conf

%files
%license LICENSE-GPL
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%{_bindir}/authramp
%{_libdir}/security/libpam_authramp.so
/etc/security/authramp.conf

%changelog
%autochangelog