# __The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case__

## Introduction

The hydrogen atom is the Coulomb problem: a particle of mass $m$ bound by the central potential $V(r)=-\kappa/r$, where $\kappa = Ze^2/(4\pi\epsilon_0)$ for a nucleus of charge $Ze$. In the standard non-relativistic treatment the problem is solved by separating the Laplacian in spherical coordinates, reducing it to a radial equation. The bound-state energies are

$$
E_n = -\frac{m\kappa^2}{2\hbar^2 n^2},
$$

the eigenstates are labelled by the quantum numbers $n,l,m$, and each orbital level carries a two-valued spin factor.

This article writes that problem in the notation of the biquaternion framework and asks what the framework contributes to it. The material it uses is already on the shelf. The companion article *Angular Momentum and Spin in Biquaternionic Form* supplies the orbital operators $L_k e_t$, sitting in the scalar slot, the spin operators $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, sitting in the vector slots, and the eigenvalue $\hbar^2 l(l+1)$ through which the angular problem couples to the radial one. The companion article *The Schrödinger Equation in Biquaternionic Form* supplies the state module $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$ and fixes the scalar imaginary $i$ as the unit of the equation.

The honest summary can be stated before the derivation, and it is simple. The non-relativistic Coulomb Hamiltonian is a **central scalar** element of $\mathbb{M}_+$: its vector part vanishes. It therefore treats the spin as a spectator, and the biquaternion equation reduces componentwise to the ordinary scalar Schrödinger equation. The genuinely algebraic ingredients are the two-dimensional module $\mathbb{B}\tilde\Pi$ that carries the spin factor and the placement of the orbital and spin operators in complementary slots. What the framework does **not** supply is the space in which the bound states live and an algebraic account of the $n^2$ degeneracy; both gaps are stated where they arise and collected in a section of their own, rather than smoothed over.

The title covers the non-relativistic case only. The relativistic case begins from the biquaternion Dirac equation with the Coulomb potential, where the Hamiltonian is no longer central, the spin is no longer a spectator, and the $l$-degeneracy is lifted; it is left to its own article and is described only qualitatively at the end.

## The Coulomb Hamiltonian in $\mathbb{M}_+$

### The kinetic term and a sign

The momentum operator of the framework is

$$
\tilde p = -i\hbar\nabla = \vec e_k p_k, \qquad \nabla = \vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z, \qquad p_k = -i\hbar\partial/\partial Q_k .
$$

Since $\tilde p$ has a purely imaginary vector part, it is Hermitian and lies in $\mathbb{M}_+$: it is an observable, not a generator. It is the same element that the companion articles use to build the orbital angular momentum, $\vec r\tilde p\in\mathbb{B}$ for the material-sector position $\vec r\in\mathbb{H}_{\mathbb{B}}$.

The kinetic energy requires care with the quaternion square. The components $p_j$ commute, so the cross terms in the product $\tilde p\circ\tilde p$ cancel pairwise:

$$
\tilde p^{\,2} = \sum_{\mu,\nu} \vec e_\mu \vec e_\nu\,p_\mu p_\nu
= \sum_k \vec e_k^2p_k^{\,2}
= -\Big(\sum_k p_k^{\,2}\Big)e_t
= -p^{\,2}e_t ,
$$

because $\vec e_\mu \vec e_\nu+\vec e_\nu \vec e_\mu=0$ for $\mu\neq\nu$. Here $p^{\,2}=p\cdot p=-\hbar^2\nabla^2$. Since quaternion conjugation negates the vector part, $\tilde p^{\natural}=-\tilde p$, and

$$
\tilde p\,\tilde p^{\natural} = \langle\tilde p\rangle_{\natural} = -\tilde p^{\,2} = p^{\,2}e_t = -\hbar^2\nabla^2\,e_t .
$$

The two natural transcriptions therefore agree, and the kinetic energy is

$$
\boxed{\;T = -\frac{1}{2m}\tilde p^{\,2} = \frac{1}{2m}\tilde p\,\tilde p^{\natural} = \frac{p^{\,2}}{2m}e_t\;}.
$$

The explicit minus sign is not decoration. The quaternion square of a pure vector is **minus** its Euclidean square, so writing $\tilde p^{\,2}/(2m)$ without the sign would reverse the kinetic term, leaving a Hamiltonian unbounded below and no bound states at all. The sign is the same algebraic fact — $\vec e_k^2=-e_t$ — that gives the biquaternion norm $\langle\tilde H\rangle_{\natural}=h_t^2-|\vec h|^2$ on $\mathbb{M}_+$ its Lorentzian signature; for the momentum, whose scalar part is zero, the biquaternion norm is $-\sum_kh_k^2\,e_t$, the negative of the Euclidean square. The kinetic operator is, up to the factor $1/2m$, the biquaternion norm of the momentum.

### The potential

The Coulomb potential is the central scalar

$$
\tilde\Phi = V(r)\,e_t, \qquad V(r) = -\frac{\kappa}{r}, \qquad \kappa = \frac{Ze^2}{4\pi\epsilon_0} .
$$

It lies in $\mathbb{M}_+$, and in fact in the centre $\mathbb{C}_{\mathbb{B}}$. Two honest remarks belong here. First, the $1/r$ form is put in by hand: the framework's Maxwell equation does produce the field of a point charge as an imaginary vector in $\mathbb{M}_+$, but the point-charge source is input, not derived. Second, the potential is a scalar and carries no vector part, so the framework's sector structure is not used by it; a vector-valued or spin-dependent coupling would be a different problem, and none is introduced here.

### The Hamiltonian and its sector

Adding the two terms,

$$
\boxed{\;H = T+\tilde\Phi
= \left[-\frac{\hbar^2}{2m}\nabla^2-\frac{\kappa}{r}\right]e_t
= h_t\,e_t, \qquad h_t = -\frac{\hbar^2}{2m}\nabla^2-\frac{\kappa}{r}\;}.
$$

The Hamiltonian is Hermitian and lies in $\mathbb{M}_+$, and its vector part is zero: $\vec h=0$ in the general form $\tilde H=h_te_t+i\vec h$. It is therefore **central**, commuting with every element of $\mathbb{B}$, and in particular with the spin operators and with $i$.

The generator of the Schrödinger equation is

$$
-\frac{i}{\hbar}H
= i\left(\frac{\hbar}{2m}\nabla^2+\frac{\kappa}{\hbar r}\right)e_t \in \mathbb{M}_- ,
$$

and it lies along the time-like direction $ie_t$ of the material sector, as the companion article on the Schrödinger equation requires of a time-translation generator. Both the observable and the generator are scalar multiples of $e_t$. The framework's sector split is thus realised here in its simplest possible form: the entire Hamiltonian content of the non-relativistic Coulomb problem sits in the scalar slot, and the vector slots are empty.

## The State Module and the Spinor Wave Function

The framework's states are spinors in the Peirce carrier $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$, a minimal left ideal here. A position-space treatment requires a spinor **field**,

$$
\psi(t',x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\in\mathbb{B}\tilde\Pi \cong \mathbb{C}^2,
$$

a two-component object defined on the spatial coordinates of the material sector. This is an extension of the framework's quantum formalism, which the companion articles state for a single qubit, and it should be labelled as one: the position dependence is carried by the **argument** of the field, not by the algebra. The algebra acts on the internal two-dimensional index; the argument is external structure that the finite-dimensional algebra does not contain.

Under the isomorphism $\mathsf{M}_2$ the field $\psi$ is a column vector in $\mathbb{C}^2$, the spin operators $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$ act on its two components as $\tfrac{\hbar}{2}\sigma_k$, and the orbital operators $L_k e_t$ act on the argument as $L_k$ times the identity. The framework expresses the distinction between these two kinds of action algebraically. The orbital operators occupy the **scalar** slot $e_t$; the spin operators occupy the **vector** slots $i\vec e_k$. Because a scalar multiple of $e_t$ is central, the two families commute:

$$
[L_i,\tilde S_j]=0 .
$$

This is the framework's statement that the external and internal degrees of freedom are independent, and it is what makes the separation of the Coulomb problem possible in the form below.

## Separation of the Coulomb Problem

### Conserved quantities

Because $H$ is central it commutes with everything, so

$$
[H,L_k]=0, \qquad [H,\tilde S_k]=0, \qquad [H,L^2]=0, \qquad [H,\tilde S^2]=0,
$$

with the Casimir operators built from the operators of the companion article, $L^2e_t$ and $\tilde S^2=\tfrac{3\hbar^2}{4}e_t$. The orbital magnetic quantum number $m$, the orbital quantum number $l$, and the spin quantum numbers are therefore all good quantum numbers of the non-relativistic Coulomb problem, and the Hamiltonian mixes none of them.

One consequence deserves emphasis, because it distinguishes this article from the relativistic one. Since $H$ is spin-independent, the **total** angular momentum $\tilde J_k=L_k+\tilde S_k$ and its coupling are not needed here. The coupled basis $|n,l,j,m_j\rangle$ and the spin–orbit eigenvalues of the angular-momentum article become relevant only when the $1/c^2$ corrections are included; in the non-relativistic problem the natural basis is the uncoupled one, $|n,l,m\rangle\,|\!\uparrow\rangle,|n,l,m\rangle\,|\!\downarrow\rangle$.

A clarification is owed at this point, because the angular-momentum article introduces the spin–orbit operator $L_k\tilde S_k$ in the same discussion of the hydrogen atom and records its eigenvalues. Those eigenvalues are not properties of the Hamiltonian $H$ of this article. The Coulomb Hamiltonian above is strictly spin-independent, and the spin–orbit interaction is a relativistic correction of relative order $v^2/c^2$; it enters the spectrum only when the relativistic problem is treated. The coupled-basis construction of the angular-momentum article is the correct machinery for that corrected problem, not for the uncorrected one considered here.

### The angular and spin factors

The orbital angular momentum operators have the standard spherical-coordinate forms and spectra,

$$
L^2\,Y_l^m = \hbar^2 l(l+1)\,Y_l^m, \qquad L_z\,Y_l^m = \hbar m\,Y_l^m ,
$$

with $Y_l^m$ the spherical harmonics. The spin operators satisfy $\tilde S^2=\tfrac{3\hbar^2}{4}e_t$, which is $s(s+1)\hbar^2$ with $s=\tfrac12$, and their eigenstates are the idempotents: the projection of the spin along a unit direction $\vec u$ has the two eigenspaces

$$
\vec u_k\tilde S_k\,\tilde{\Pi}(\pm\vec u) = \pm\tfrac{\hbar}{2}\,\tilde{\Pi}(\pm\vec u),
\qquad
\tilde{\Pi}(\pm\vec u)=\tfrac12(e_t\pm i\vec u),
$$

and for the axis $\vec u=\vec e_z$ the two idempotents $\tilde{\Pi}(\pm \vec e_z)=\tfrac12(e_t\pm i\vec e_z)$ are the spin-up and spin-down states.

The framework's Born rule for the spin factor is the trace formula. For the observable $\tilde S_k$ in the pure state $\tilde{\Pi}(\vec u)=\tfrac12(e_t+i\vec u)$,

$$
\mathrm{Tr}\bigl(\tilde{\Pi}(\vec u)\,\tilde S_k\bigr) = 2\,\mathrm{Sc}\bigl(\tilde{\Pi}(\vec u)\,\tilde S_k\bigr) = \frac{\hbar}{2}\vec u_k ,
$$

which is the standard spin-1/2 expectation value, written as the plain form of $\mathbb{M}_+$, read as the trace pairing.

### The ansatz and the radial equation

Separate the field as

$$
\boxed{\;\psi_{nlm m_s}(r,\theta,\phi) = R_{nl}(r)\,Y_l^m(\theta,\phi)\,\chi_{m_s}\;},
\qquad \chi_{m_s}\in\mathbb{B}\tilde\Pi ,
$$

with $\chi_{m_s}$ a constant spinor. Substituting into the biquaternion Schrödinger equation $i\hbar\,\partial/\partial t'\psi=H\psi$ and using the spherical decomposition of the Laplacian,

$$
-\hbar^2\nabla^2 = \frac{L^2}{r^2} - \frac{\hbar^2}{r^2}\partial/\partial r\,\bigl(r^2\partial/\partial r\,\bigr),
$$

the angular factor is an eigenfunction of $L^2$ with eigenvalue $\hbar^2l(l+1)$, and the equation reduces to the radial equation for $u_{nl}=rR_{nl}$:

$$
-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[\frac{\hbar^2 l(l+1)}{2mr^2}-\frac{\kappa}{r}\right]u = E\,u .
$$

This is the standard radial Coulomb equation. The framework's contribution at this step is the identification of the coupling: the whole of the angular problem enters the radial equation through the single eigenvalue $\hbar^2 l(l+1)$ of $L^2$, which is exactly the statement the angular-momentum article makes about the operators "that a position-space treatment of the hydrogen atom requires". The spin factor does not enter the radial equation at all, because $H$ is central; it multiplies the solution.

## The Spectrum and the Eigenstates

### The spectrum

The bound-state solutions of the radial equation are the standard ones. The spectrum is

$$
\boxed{\;E_n = -\frac{m\kappa^2}{2\hbar^2 n^2} = -\frac{\kappa}{2a_0 n^2}\;},
\qquad n=1,2,3,\dots,
$$

where $a_0=\hbar^2/(m\kappa)$ is the Bohr radius. For hydrogen, $a_0=0.529\,\text{Å}$ and $E_1=-13.6\,\text{eV}$. The principal quantum number is $n=n_r+l+1$ with radial quantum number $n_r=0,1,2,\dots$, so that for a given $n$,

$$
l=0,1,\dots,n-1, \qquad m=-l,\dots,+l, \qquad m_s=\pm\tfrac12 .
$$

### The degeneracy

The count of orbital states at level $n$ is

$$
\sum_{l=0}^{n-1}(2l+1)=n^2 ,
$$

and each carries the two spin values, so the level has degeneracy $2n^2$. The factor of two is the one part of the counting that is algebraic: the module $\mathbb{B}\tilde\Pi$ on which the spin acts is two-dimensional, and $\tilde S^2=\tfrac{3\hbar^2}{4}e_t$ says that its internal factor is spin-$\tfrac12$. The factor $n^2$ is another matter, and the framework does not account for it; see the section "What the Framework Does Not Supply" below.

### The eigenstates

The radial eigenfunctions are the standard ones, expressed through the associated Laguerre polynomials:

$$
R_{nl}(r) = N_{nl}\,\rho^{\,l}\exp(-\rho/2)\,L_{n-l-1}^{2l+1}(\rho),
\qquad \rho = \frac{2r}{n a_0},
$$

with $N_{nl}$ the normalisation constant. The lowest few, normalised for $\int_0^\infty R^2r^2\,dr=1$ in units $a_0=1$, are

$$
R_{10}=2\exp(-r), \qquad
R_{20}=\frac{1}{\sqrt2}\Bigl(1-\frac{r}{2}\Bigr)\exp(-r/2), \qquad
R_{21}=\frac{1}{\sqrt{24}}\,r\,\exp(-r/2).
$$

The ground state is therefore

$$
\psi_{100}(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z) = \frac{1}{\sqrt{\pi a_0^3}}\,\exp(-r/a_0)\,\chi_{m_s},
\qquad E_1=-\frac{\kappa}{2a_0},
$$

a spinor field whose orbital factor is the familiar exponential and whose spin factor is any of the two idempotents $\tilde{\Pi}(\pm \vec e_z)$. A complete eigenstate is the product $R_{nl}Y_l^m\chi_{m_s}$: the radial factor solves the radial equation, the angular factor is an eigenfunction of $L^2$ and $L_z$ in the scalar slot, and the spin factor is an idempotent of the vector slot. The eigenvalue is $E_n$, independent of $l$, $m$ and $m_s$.

## Correspondence with the Standard Solution

Under the isomorphism $\mathsf{M}_2$ the transcription is transparent. The field $\psi$ is a two-component column, the central Hamiltonian acts as $h_t I_2$, and the biquaternion Schrödinger equation becomes two identical copies of the standard Schrödinger equation for the Coulomb problem. The correspondence is collected here.

| Standard object | Biquaternion object | Slot |
|---|---|---|
| Hamiltonian $-\frac{\hbar^2}{2m}\nabla^2-\frac{\kappa}{r}$ | $H = \bigl[-\frac{\hbar^2}{2m}\nabla^2-\frac{\kappa}{r}\bigr]e_t\in\mathbb{M}_+$ | scalar |
| Kinetic term $p^2/2m$ | $-\frac{1}{2m}\tilde p^{\,2}=\frac{1}{2m}\tilde p\tilde p^{\natural}$ | scalar |
| Orbital $L_k$ | $L_k e_t$ | scalar |
| Spin $S_k=\frac{\hbar}{2}\sigma_k$ | $\tilde S_k=\frac{\hbar}{2}i\vec e_k$ | vector |
| Wavefunction $\psi\in L^2(\mathbb{R}^3)\otimes\mathbb{C}^2$ | spinor field $\psi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\in\mathbb{B}\tilde\Pi$ | module |
| Spectrum $E_n=-\frac{m\kappa^2}{2\hbar^2n^2}$ | identical | — |
| Degeneracy $2n^2$ | identical, spin factor from $\dim\mathbb{B}\tilde\Pi=2$ | — |

The spectrum, the eigenfunctions, the quantum numbers and the degeneracies are the standard ones. The biquaternion form is a transcription, and it predicts nothing beyond the standard solution. What it does isolate is three structural facts that the standard notation leaves implicit:

1. **The kinetic term is a biquaternion-norm object.** It carries an explicit minus sign relative to $\tilde p^{\,2}$, because the quaternion square of a pure vector is minus the Euclidean square. The spinless-looking scalar $p^2/2m$ is really $\frac{1}{2m}\tilde p\tilde p^{\natural}$, a quadratic form of the momentum.
2. **The Hamiltonian is central and the generator is in the material sector.** The observable $H$ lies in $\mathbb{M}_+$; the generator $-iH/\hbar$ lies in $\mathbb{M}_-$ along $ie_t$. The entire Coulomb content is carried by the scalar slot, and the vector slots, which the spin occupies, are untouched.
3. **Orbital and spin operators occupy complementary slots.** The orbital operators are scalar multiples of $e_t$ and central; the spin operators are vector-slot elements. Their commutativity, $[L_i,\tilde S_j]=0$, is the framework's reason for the separability of the non-relativistic problem, and the reason the total-angular-momentum coupling is not required here.

## What the Framework Does Not Supply

The article's title promises the hydrogen atom in biquaternionic form. What has been delivered is the Coulomb problem written in the framework's notation, plus the structural facts above. The gaps should be recorded plainly.

**1. The bound-state space is not a module over $\mathbb{B}$.** The algebra is finite-dimensional, $\mathbb{B}\cong M_2(\mathbb{C})$, and it has a single irreducible module, the two-dimensional fundamental one, which carries spin-$\tfrac12$. The bound states span $L^2(\mathbb{R}^3)\otimes\mathbb{C}^2$, an infinite-dimensional space that $\mathbb{B}$ does not contain, and the $(2l+1)$-dimensional orbital representations are representations of the rotation algebra that are not $\mathbb{B}$-modules at all — the spin-1/2 and angular-momentum articles state both points. The algebra supplies the spin factor; it does not supply the solution space, and there is no finite-dimensional algebraic trick that would extract the hydrogen spectrum from $\mathbb{B}$.

**2. There is no position–momentum pair in $\mathbb{M}_+$.** The companion article on the harmonic oscillator shows that $[\tilde H_1,\tilde H_2]=i\hbar e_t$ has no solution with $\tilde H_1,\tilde H_2\in\mathbb{M}_+$: the commutator of two Hermitian biquaternions is a real pure quaternion with no scalar part, and equivalently its trace vanishes while $\mathrm{Tr}(i\hbar e_t)=2i\hbar$. Consequently the position dependence used here is not an algebraic observable of the framework; it is the argument of the spinor field. (The position that appears in the construction $\vec r\tilde p$ is the material-sector vector $\vec r\in\mathbb{H}_{\mathbb{B}}$, not an element of $\mathbb{M}_+$.) The position-space theory is therefore an extension of the framework, not a consequence of it.

**3. The $n^2$ degeneracy has no algebraic account here.** The degeneracy across $l$ at fixed $n$ is the $SO(4)$ symmetry generated by the Runge–Lenz vector, and the angular-momentum article records the framework's lack of an algebraic account of that hidden symmetry as an open question. This article inherits the degeneracy from the standard solution and offers no explanation of it. It is worth being explicit that the count $\sum_{l=0}^{n-1}(2l+1)=n^2$ is a sum of $SO(3)$ multiplicities and does not by itself explain why the energies are degenerate across $l$; the degeneracy, not the count, is the unexplained fact.

**4. The potential is inserted, and no deviation is predicted.** The $1/r$ binding is a central scalar placed in the Hamiltonian. The framework neither derives it from a deeper principle nor modifies it, and the non-relativistic spectrum agrees with the standard one term by term. Any framework-specific effect would have to appear as a coupling the standard Coulomb problem does not have, and none is proposed.

A fifth, smaller point is worth a line. The corpus's biquaternion special-functions article defines Laguerre polynomials $L_n(\tilde Q)$ for a biquaternion argument. Those are not the functions used above: the radial variable is a real scalar, $\rho=2r/(na_0)$, so the radial functions are the ordinary associated Laguerre polynomials with a real argument. The biquaternion-valued special functions are a separate construction and are not needed here; writing them in would be a misapplication.

## Where the Relativistic Case Differs

The companion article *The Hydrogen Atom in Biquaternionic Form — The Relativistic Case* would begin from the biquaternion Dirac equation with the Coulomb potential rather than from the Schrödinger equation. Four differences from the present treatment are structural, and each is already visible in the framework's angular-momentum machinery.

**The Hamiltonian ceases to be central.** The relativistic Coulomb problem couples the spin and the orbit, so the total angular momentum $\tilde J_k=L_k+\tilde S_k$ replaces the separate factors. The spin–orbit operator $L_k\tilde S_k$ has the eigenvalues given in the angular-momentum article,

$$
\bigl(L_k\tilde S_k\bigr)_{j=l\pm\frac12} =
\begin{cases} +\dfrac{\hbar^2 l}{2}, & j=l+\tfrac12,\\[6pt] -\dfrac{\hbar^2(l+1)}{2}, & j=l-\tfrac12, \end{cases}
$$

and the relevant basis is the coupled one, $|n,l,j,m_j\rangle$, built with the Clebsch–Gordan coefficients for $\tfrac12\otimes l$.

**The good quantum numbers change.** In the non-relativistic problem the level depends on $n$ alone and $l,m,m_s$ are all good. Relativistically the level depends on $n$ and $j$, not on $l$: the $l$-degeneracy at fixed $n$ is lifted, and what survives is a degeneracy between the two $l=j\pm\tfrac12$ states at the same $j$ (with no partner for the extreme $j=n-\tfrac12$).

**The spectrum is the Sommerfeld/Dirac form.** Writing $\alpha=e^2/(4\pi\epsilon_0\hbar c)$ for the fine-structure constant, the exact bound-state energies are

$$
E_{nj} = mc^2\left[1+\frac{(Z\alpha)^2}{\bigl(n-\delta_j\bigr)^2}\right]^{-1/2},
\qquad
\delta_j = j+\tfrac12-\sqrt{\bigl(j+\tfrac12\bigr)^2-(Z\alpha)^2},
$$

whose expansion in $(Z\alpha)^2$ returns the non-relativistic $E_n$ at leading order and the fine structure

$$
\Delta E_{\text{fs}} = -\frac{mc^2(Z\alpha)^4}{2n^3}\left(\frac{1}{j+\tfrac12}-\frac{3}{4n}\right)
$$

at the next order. The Darwin term, the relativistic kinetic correction and the gyromagnetic factor $g=2$ appear in the same expansion, as the framework's Dirac articles and the Foldy–Wouthuysen exercise develop.

**The framework's algebraic content moves to the vector slots.** In the non-relativistic problem the spin is a spectator and the whole Hamiltonian sits in the scalar slot. Relativistically the spin is dynamical, its slot is occupied by part of the Hamiltonian, and the sector structure — the observable/generator split and the coupling $[\tilde J_i,\tilde J_j]=i\hbar\epsilon_{ijk}\tilde J_k$ — does work that it does not do here. Whether the framework adds anything to the standard Dirac–Coulomb solution beyond that rearrangement is a question for the relativistic article; this article makes no claim about it, and the title is restricted to the non-relativistic case for that reason.

## Summary

The non-relativistic hydrogen atom in biquaternionic form is the Coulomb problem for a spinor field. The momentum $\tilde p=-i\hbar\nabla$ is Hermitian in $\mathbb{M}_+$; its quaternion square is minus the Euclidean square, $\tilde p^{\,2}=-p^{\,2}e_t=\hbar^2\nabla^2e_t$, so the kinetic energy is $-\tilde p^{\,2}/(2m)=\tilde p\tilde p^{\natural}/(2m)=p^{\,2}/(2m)e_t$. Adding the central scalar potential $-\kappa/r$ gives

$$
H = \left[-\frac{\hbar^2}{2m}\nabla^2-\frac{\kappa}{r}\right]e_t = h_te_t \in \mathbb{M}_+,
\qquad
-\frac{i}{\hbar}H = i\left(\frac{\hbar}{2m}\nabla^2+\frac{\kappa}{\hbar r}\right)e_t \in \mathbb{M}_- .
$$

The Hamiltonian is central, so the spin is a spectator, the total-angular-momentum coupling is not needed, and the spinor equation reduces componentwise to the standard scalar Schrödinger equation. Separation in the framework's operators, with orbital operators in the scalar slot and spin operators in the vector slots, gives the standard radial equation with the angular coupling $\hbar^2 l(l+1)$, the standard spectrum

$$
E_n = -\frac{m\kappa^2}{2\hbar^2 n^2} = -\frac{\kappa}{2a_0n^2},
$$

the standard eigenstates $R_{nl}(r)Y_l^m(\theta,\phi)\chi_{m_s}$, and the degeneracy $2n^2$, of which only the factor of two is algebraic, being the dimension of the state module $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$ together with $\tilde S^2=\tfrac{3\hbar^2}{4}e_t$.

The framework's contribution is therefore structural, not spectral. It identifies the kinetic term as a biquaternion-norm object, places the observable in $\mathbb{M}_+$ and the generator in $\mathbb{M}_-$ along $ie_t$, and separates orbital from spin degrees of freedom by slot. It does not supply the bound-state space, which is not a module over the finite-dimensional algebra; it does not supply a position–momentum pair in $\mathbb{M}_+$; and it does not account for the $n^2$ degeneracy, whose $SO(4)$ origin remains an open question in the corpus. The spectrum and eigenstates are the standard ones, and no deviation is predicted. The relativistic case, where the spin couples and the degeneracy is lifted, is left to its own article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_\mu \vec e_\nu=\epsilon_{\mu\nu\lambda}\vec e_\lambda$ $(\mu\neq\nu)$ |
| $i$ | Central scalar imaginary, $i^2=-e_t$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material): generators; $i\mathbb{M}_+=\mathbb{M}_-$ |
| $\mathbb{M}_+$ | Hermitian subspace (informational): observables and states |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace; $\vec r=x\vec e_x+y\vec e_y+z\vec e_z$ the material position |
| $\mathbb{C}_{\mathbb{B}}$ | Centre, $\operatorname{span}_\mathbb{R}\{e_t,ie_t\}$ |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\mathsf{M}_2(i\vec e_k)=\sigma_k$ | Isomorphism with $M_2(\mathbb{C})$ |
| $\tilde p=-i\hbar\nabla=\vec e_k p_k$, $p_k=-i\hbar\partial/\partial Q_k$ | Momentum, Hermitian, in $\mathbb{M}_+$ |
| $\tilde p^{\,2}=-p^{\,2}e_t$, $\tilde p\tilde p^{\natural}=p^{\,2}e_t$ | Quaternion square and biquaternion norm of the momentum |
| $T=-\tilde p^{\,2}/(2m)$ | Kinetic energy |
| $H=h_te_t$, $h_t=-\frac{\hbar^2}{2m}\nabla^2-\frac{\kappa}{r}$ | Coulomb Hamiltonian, central, in $\mathbb{M}_+$ |
| $-iH/\hbar\in\mathbb{M}_-$ | Time-translation generator, $H$ read through $i$ |
| $\kappa=Ze^2/(4\pi\epsilon_0)$ | Coulomb coupling |
| $a_0=\hbar^2/(m\kappa)$ | Bohr radius |
| $L_k e_t$, $L^2e_t$ | Orbital operators, scalar slot |
| $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, $\tilde S^2=\tfrac{3\hbar^2}{4}e_t$ | Spin operators, vector slots |
| $\tilde J_k=L_k+\tilde S_k$ | Total angular momentum (needed only relativistically) |
| $\mathbb{B}\tilde\Pi\cong\mathbb{C}^2$ | State module of spinors $\psi$ |
| $\tilde{\Pi}(\pm\vec u)=\tfrac12(e_t\pm i\vec u)$ | Spin eigenstates (idempotents) |
| $\operatorname{Tr}(\tilde\Pi\tilde H^{*})=\operatorname{Tr}(\tilde\Pi\tilde H)=2\,\mathrm{Sc}(\tilde\Pi\tilde H^{*})$ | Trace reading at normalisation (Born rule) |
| $E_n=-\frac{m\kappa^2}{2\hbar^2n^2}$ | Bound-state spectrum, $n=n_r+l+1$ |

## Further Reading

- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the operator treatment of angular momentum and the hydrogen spectrum.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the standard separation of the Coulomb problem and the hydrogen wavefunctions.
- Albert Messiah, *Quantum Mechanics* (Dover, 1999), for the radial equation, the Laguerre functions, and the degeneracy of the Coulomb problem.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 1977), for the Coulomb problem and the $SO(4)$ symmetry generated by the Runge–Lenz vector.
- B. L. van der Waerden, *Sources of Quantum Mechanics* (Dover, 1968), for the historical development of the Bohr–Sommerfeld spectrum.
- H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957), for the hydrogen spectrum and its relativistic corrections.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the relation of biquaternions to $M_2(\mathbb{C})$ and the spinor representation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Coulomb problem and the Kepler symmetry.
