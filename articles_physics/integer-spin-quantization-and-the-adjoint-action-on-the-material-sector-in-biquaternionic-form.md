# __Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form__

## Introduction

A particle of integer spin is, in Wigner's classification, a state that transforms under the rotation group in a representation of dimension $2s+1$: one state for $s=0$, three for $s=1$, five for $s=2$. The spin-$0$ case is realized in the biquaternion framework by the center $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$, on which the rotations act trivially; the spin-$\tfrac12$ case by the left ideal that carries the fundamental representation, treated in the companion subcategory on spin $\tfrac12$. The present article treats the integer-spin cases, and its central claim is that the **spin-one** representation is not merely compatible with the biquaternion algebra but is *the same object as* a natural operation inside it: the adjoint action of the rotation algebra on the vector part of the material sector $\mathbb{M}_-$ is, on the nose, the three-dimensional spin-one representation.

This identification is the framework's own contribution, and it is the reason the subcategory is organized around the material sector rather than around a separate internal space. The algebra does not have to be told what a vector is, nor how the rotation group acts on one, in order to produce the spin-one triplet: the quaternion multiplication already does it, and the diagonalization of the adjoint action already produces the circular and longitudinal polarizations that the massive vector field needs.

The article is organized as follows. The rotation algebra is constructed as the algebra of inner derivations of $\mathbb{B}$, and its action on the material sector is computed. The three-dimensional invariant subspace is identified, the commutators and the Casimir are evaluated, and the weight basis that diagonalizes one generator is exhibited. The spin-one triplet is then identified with the polarization triad of the massive vector field, and the raising and lowering operators are written. A section explains why the action on the material sector is the correct one for the polarisation index, separating the orbital from the internal part of the angular momentum. A section places the construction in the general integer-spin setting, where the carrier is a symmetric traceless tensor of the material sector and the spin-one case is the rank-one instance. The quantization of integer-spin fields is then stated, with the bosonic oscillator algebra, the positivity of the massive case, the spin–statistics theorem, and the massless helicity states. The article closes with the accounting of what the algebra supplies and what is imported.

- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the angular-momentum operators, the orbital–internal split, and the rotation conventions.
- Companion article *The Photon in Biquaternionic Form*, for the massless helicity states, the circular polarization basis, and the removal of the longitudinal state.
- Companion article *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the Fock construction and the proof that the ladder algebra is not native to $\mathbb{B}$.
- Companion article *The Spin–Statistics Theorem in Biquaternionic Form*, for the connection between integer spin and bosonic exchange symmetry.
- Companion article *The Klein–Gordon Equation in Biquaternionic Form*, for the scalar case and the trivial action of the rotations on the center.
- Companion article *Canonical Quantization of the Biquaternion Maxwell Field*, for the two massless polarizations and the first-class constraint structure.
- Companion article *Canonical Quantization of the Biquaternion Proca Field*, for the massive vector field whose three on-shell polarizations are the weight basis of this article.
- Companion article *Canonical Quantization of the Biquaternion Graviton Field*, for the rank-two instance of the tensor-power construction, where the trace removal is performed on the symmetric square of the material vector.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$, and central $i$. The material sector is $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}$ (imaginary scalar plus real vector), the informational sector is $\mathbb{M}_+=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\}$, and the material basis is $\hat e_0=ie_0$, $\hat e_k=e_k$, with $\eta_{\mu\nu}=\langle\hat e_\mu,\hat e_\nu\rangle=\mathrm{diag}(-1,+1,+1,+1)$. The vector part of the material sector is $V=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$, a three-dimensional complex space on which the rotations act, and it is the carrier of the spin-one representation. The angular momentum operator is $J_k=\tfrac12\mathrm{ad}_{ie_k}$, with $\mathrm{ad}_XY=[X,Y]=XY-YX$. The adjoint action is bracketing, a derivation of the algebra: $\mathrm{ad}_X(YZ)=(\mathrm{ad}_XY)Z+Y(\mathrm{ad}_XZ)$.

## The Rotation Algebra as Inner Derivations

### Rotations and Their Generators

The rotation group acts on the algebra by inner automorphisms. For a unit quaternion $Q$ with $Q\bar{Q}=e_0$, the map

$$
R_Q:\;X\longmapsto QXQ^{-1}=\bar{Q}XQ
$$

is an algebra automorphism that fixes the center, hence fixes $i$, and preserves the division of $\mathbb{B}$ into $\mathbb{M}_-$ and $\mathbb{M}_+$: conjugation preserves the Hermiticity type, so the material sector is mapped to itself. Writing $Q=e^{\theta\,e_k/2}$ with $\theta$ the rotation angle about the $k$-th axis, the infinitesimal generator of the map is the inner derivation

$$
\delta_kX = \tfrac{\theta}{2}\,[e_k,X] = \tfrac{\theta}{2}\,\mathrm{ad}_{e_k}X .
$$

The three derivations $\mathrm{ad}_{e_k}$ span the Lie algebra of the rotation group, and the Hermitian angular-momentum operator is the corresponding anti-Hermitian generator multiplied by $i$:

$$
J_k = \tfrac12\,\mathrm{ad}_{ie_k} = \tfrac{i}{2}\,\mathrm{ad}_{e_k}.
$$

The factor $i$ is the usual one that turns the anti-Hermitian generator $e_k$ of the unitary rotation into a Hermitian observable. The three $J_k$ act on the material sector by bracketing, $X\mapsto[J_k,X]$, and they are derivations: the Leibniz rule holds, so the action on a product is the sum of the actions on the factors.

### The Adjoint Action Preserves the Material Sector

A short computation fixes the action on the basis. Since $ie_0$ is central, $\mathrm{ad}_{ie_k}(ie_0)=0$: the imaginary scalar direction is invariant. On the vector units the multiplication rule gives

$$
\mathrm{ad}_{e_3}(e_1)=2e_2,\qquad
\mathrm{ad}_{e_3}(e_2)=-2e_1,\qquad
\mathrm{ad}_{e_3}(e_3)=0,
$$

and cyclically, so that

$$
J_3e_1=ie_2,\qquad J_3e_2=-ie_1,\qquad J_3e_3=0 .
$$

The computation is elementary and was checked in the companion file against the $2\times2$ complex representation $e_k=-i\sigma_k$, where the multiplication rule $e_je_k=\varepsilon_{jkl}e_l$ for $j\neq k$ (with $e_k^2=-e_0$) holds with residual zero. Three consequences follow at once: the vector part $V=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ is invariant under the adjoint action; the full material sector decomposes into invariant pieces,

$$
\mathbb{M}_- = \mathrm{span}_{\mathbb{R}}\{ie_0\}\;\oplus\;V,
$$

of real dimensions $1$ and $3$ (or complex dimensions, if the vector part is complexified); and the adjoint action is real on $V$ in the sense that it maps the real span of $e_1,e_2,e_3$ to itself, with the $i$'s appearing only through the Hermitian normalization of $J_k$.

### The Commutators and the Casimir

Because $\mathrm{ad}$ is a Lie algebra homomorphism, the commutators of the derivations are the derivations of the commutators. For the Hermitian generators this gives

$$
[J_i,J_j] = i\,\varepsilon_{ijk}J_k ,
$$

which was verified to machine precision on the three-dimensional representation: the residual of $[J_i,J_j]-i\varepsilon_{ijk}J_k$ was zero for all nine pairs. The quadratic Casimir is

$$
J^2 = J_1^2+J_2^2+J_3^2 = 2\,I_3,
$$

verified with residual zero. The value $2=s(s+1)$ at $s=1$ is the algebraic statement that the adjoint action on $V$ is the **spin-one** representation, and $2s+1=3$ is the dimension of $V$. No further input is needed: once the multiplication table of the quaternion units is fixed, the representation is fixed.

### The Explicit Matrices

In the basis $(e_1,e_2,e_3)$ the three generators read off from the adjoint action are the standard Cartesian spin-one matrices,

$$
J_1=\begin{pmatrix}0&0&0\\0&0&-i\\0&i&0\end{pmatrix},
\qquad
J_2=\begin{pmatrix}0&0&i\\0&0&0\\-i&0&0\end{pmatrix},
\qquad
J_3=\begin{pmatrix}0&-i&0\\i&0&0\\0&0&0\end{pmatrix}.
$$

Each was obtained by applying $\tfrac12\mathrm{ad}_{ie_k}$ to the basis units and reading the coefficients of $e_1,e_2,e_3$, and the matrices agree with the standard spin-one representation in the Cartesian basis. They are Hermitian and traceless, and the trace vanishing is the statement that the weights of the triplet sum to zero. The deeper distinction between integer and half-integer spin is visible in the weight set itself: for integer $s$ the weights are $-s,\dots,0,\dots,s$ and include $m=0$, so the multiplet dimension $2s+1$ is odd and the minimal polynomial of $J_3$ has odd degree; for half-integer $s$ the weights are $\pm\tfrac12,\pm\tfrac32,\dots$, no weight vanishes, and the dimension is even. The adjoint action produces only the first case, because its representation space is a subspace of the algebra and the algebra is built from integer weights.

## The Spin-One Multiplet and Its Weight Basis

### Diagonalizing the Third Generator

The eigenvectors of $J_3$ are found by diagonalizing the $3\times3$ matrix. The result is that the complex combinations

$$
\varepsilon_+ = \frac{e_1+ie_2}{\sqrt2},
\qquad
\varepsilon_- = \frac{e_1-ie_2}{\sqrt2},
\qquad
\varepsilon_0 = e_3
$$

satisfy

$$
J_3\varepsilon_+ = +\varepsilon_+,\qquad
J_3\varepsilon_- = -\varepsilon_-,\qquad
J_3\varepsilon_0 = 0,
$$

and the eigenvalues $\pm1,0$ were confirmed directly. Equivalently, $J_3$ satisfies its own cubic characteristic identity

$$
J_3^3 - J_3 = 0,
$$

verified with residual zero: for spin one the third power of a generator returns it to itself, a property of the three eigenvalues $\pm1,0$, and of no other triplet of distinct integers summing to zero. The basis $\{\varepsilon_+,\varepsilon_-,\varepsilon_0\}$ is the circular and longitudinal polarization triad: $\varepsilon_\pm$ are the two circular polarizations, and $\varepsilon_0$ is the linear polarization along the third axis. The raising and lowering operators

$$
J_\pm = J_1\pm iJ_2
$$

act as

$$
J_\pm\varepsilon_\mp = \pm\sqrt{2}\,\varepsilon_0,
\qquad
J_\pm\varepsilon_0 = \mp\sqrt{2}\,\varepsilon_\pm,
\qquad
J_\pm\varepsilon_\pm = 0,
$$

the shift operations of the spin-one multiplet, with the matrix elements $\sqrt{s(s+1)-m(m\pm1)}=\sqrt2$ up to the relative signs shown. Those signs are the phases fixed by the displayed basis; flipping the phase of $\varepsilon_+$ restores the Condon–Shortley signs, so that the weight assignments and the multiplet structure are independent of the convention. The triplet is therefore not merely a list of three vectors; it is a weighted multiplet with the ladder structure that the adjoint action supplies.

<!-- CONVENTION — weight-basis phases: for the basis eps_+ = (e_1 + i e_2)/sqrt2, eps_- = (e_1 - i e_2)/sqrt2, eps_0 = e_3 and the generators J_k = (1/2) ad_{i e_k}, the ladder operators satisfy J_+ eps_- = +sqrt2 eps_0, J_+ eps_0 = -sqrt2 eps_+, J_- eps_+ = -sqrt2 eps_0, J_- eps_0 = +sqrt2 eps_-, and J_± eps_± = 0. The signs are a consequence of the phases of the displayed basis; the standard Condon–Shortley form is recovered by the phase shift eps_+ → -eps_+. The eigenvalue statement J_3 eps_± = ±eps_±, J_3 eps_0 = 0 is convention independent. Do not "correct" these signs without also changing the phase of eps_+. -->

### The Triplet as the Polarization Triad

The identification with the massive vector field of the Proca case is now immediate. The on-shell polarization vectors of a massive spin-one field are three vectors orthogonal to the momentum; in the rest frame they are the three spatial directions, and the adjoint action's triplet is exactly that three-dimensional space with its rotation action. The spin basis $\{\varepsilon_+,\varepsilon_-,\varepsilon_0\}$ is the basis in which the helicity about the third axis is diagonal; the transverse polarizations are $\varepsilon_\pm$ and the longitudinal one is $\varepsilon_0$, or a boost of it. The completeness relation of the massive vector field,

$$
\sum_{r=1}^{3}\varepsilon^r_\mu\varepsilon^r_\nu = \eta_{\mu\nu}+\frac{p_\mu p_\nu}{\mu^2},
$$

is the statement that the triplet spans the spatial polarisation space, and it respects the adjoint action because both sides are rotation-invariant objects in their respective indices.

For the massless field the situation is different in a way the adjoint action makes visible. The helicity operator $\lambda = \hat{\mathbf{p}}\cdot\mathbf{J}$ has eigenvalues $\pm1$ on the two circular states and $0$ on the longitudinal one, and the massless theory keeps only the $\pm1$ states; the $\lambda=0$ state is removed by the gauge structure, as the companion article *The Photon in Biquaternionic Form* develops. The adjoint action therefore carries, in one object, both the three massive polarizations and the two massless ones: which subset is physical is decided not by the algebra but by whether the gauge symmetry is present, that is, by whether the mass vanishes.

### The Massless Restriction of the Adjoint Action

For a massless field the little group is the Euclidean group of the plane transverse to the momentum, and its finite-dimensional unitary representations that occur in nature are labelled by the helicity, the eigenvalue of $\lambda=\hat{\mathbf{p}}\cdot\mathbf{J}$. In the adjoint action's basis this is transparent. Choosing $\hat{\mathbf{p}}=e_3$, the helicity is $J_3$, with eigenvalues $\pm1,0$: the two circular states $\varepsilon_\pm$ have $\lambda=\pm1$ and span the transverse plane, while $\varepsilon_0$ has $\lambda=0$ and is longitudinal. The massless field keeps the two states of $\lambda=\pm1$, and the restriction of the adjoint action to the transverse plane is the direct sum of the two one-dimensional helicity representations,

$$
J_3\big|_{\mathrm{span}\{\varepsilon_+,\varepsilon_-\}} = \mathrm{diag}(+1,-1).
$$

This is not the two-dimensional fundamental representation of the rotation group. The helicity states of a massless vector are the $\pm1$ weights of the triplet with the zero weight removed, not a spinor representation, and the removal is performed by the gauge structure rather than by the algebra. The distinction matters because the two representations behave differently under a rotation by $2\pi$: the integer-weight representations are single-valued, the half-integer ones are double-valued, and the adjoint action can produce only the first kind. The appendix-like question of how the double-valued representations arise is answered in the spin-$\tfrac12$ subcategory by the left ideal, not here.

### Why the Third Power Vanishes for Spin One

The identity $J_3^3=J_3$ deserves a remark, because it is the algebraic fingerprint of the triple. For a generator of the spin-$s$ representation the eigenvalues are $-s,-s+1,\dots,s$, and the polynomial that annihilates the generator on the representation — the minimal polynomial — is $\prod_{m=-s}^{s}(J_3-m)$ of degree $2s+1$. For $s=1$ this is $J_3(J_3-1)(J_3+1)=J_3^3-J_3$. The adjoint action on a three-dimensional space can be checked against this: the residual of $J_3^3-J_3$ was zero. A trace-free $3\times3$ matrix with eigenvalues $\pm1,0$ and unit normalization is a spin-one generator, and the adjoint action produces one.

## The Internal and Orbital Parts of Angular Momentum

It is worth being precise about what the adjoint action is the action *on*. A field in the material sector is a map $\tilde{\Phi}:\mathbb{R}^{1,3}\to\mathbb{M}_-$; its value at a point is a material biquaternion, and a rotation acts on it in two ways: on the point, through the argument, and on the value, through the adjoint action. The total angular momentum is the sum of the two,

$$
\mathbf{J} = \mathbf{L}+\mathbf{S},
\qquad
\mathbf{L} = \tilde{x}\times\tilde{p},
\qquad
\mathbf{S}_k = \tfrac12\mathrm{ad}_{ie_k},
$$

with $\mathbf{S}$ the adjoint action acting on the material index. The two commute, because $\mathbf{L}$ acts on the argument and $\mathbf{S}$ on the value, and the total generators satisfy the same algebra. The scalar field of the companion spin-$0$ subcategory has $\mathbf{S}=0$ because its values lie in the center; the spin-$\tfrac12$ field has $\mathbf{S}$ equal to the left-ideal action of the companion subcategory. The integer-spin field of spin one is the first case in which the internal action is the adjoint action, and the reason is that the field is a material **vector**, the representation of $\mathbb{B}$ that the algebra naturally acts on by bracketing.

The decomposition of the material sector, $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0\}\oplus V$, is the decomposition of the field into a spin-$0$ piece and a spin-$1$ piece under the internal action. For the Proca field this is not a decomposition into independent physical fields — the constraint structure of the massive vector theory ties the two together, and the spin-$0$ component $A_0$ is not independent — but it is the correct transformation law of the components.

## General Integer Spin

For spin $s$ the carrier is the space of symmetric traceless rank-$s$ tensors of the material vector space $V$, of complex dimension $2s+1$. In biquaternion terms this is the symmetric traceless part of the $s$-fold tensor power of the vector part, and the angular momentum operator is the sum of the adjoint actions on the factors, by the Leibniz rule,

$$
\mathbf{S}^{(s)}_k = \sum_{a=1}^{s}\underbrace{I\otimes\cdots\otimes\tfrac12\mathrm{ad}_{ie_k}\otimes\cdots\otimes I}_{s\ \text{factors}} .
$$

The trace removal is what reduces the tensor power to the irreducible spin-$s$ piece; it can be imposed by the metric pairing $\langle\cdot,\cdot\rangle=\mathrm{Sc}(\cdot\,\bar{\cdot})$ between factors, which is an operation the algebra already provides. The integer-spin representations are thus all constructed from the adjoint action, the tensor product, the symmetry projector, and the trace removal, and no new algebraic input is required.

The cases nearest at hand are $s=1$, which is the adjoint action itself and is the subject of the preceding sections, and $s=2$, which is the symmetric traceless rank-two tensor and is the subject of the article of this subcategory on the graviton. The $s=2$ carrier contains, by the Clebsch–Gordan series of $1\otimes1$, a spin-$2$, a spin-$1$ and a spin-$0$ piece; the antisymmetric part is the spin-$1$ triplet, while in the symmetric part the trace subtraction removes the spin-$0$ piece, leaving the five components of the massive spin-two carrier — the massless graviton retaining two of them after the gauge removal. The angular momentum of the spin-two field is the sum of two adjoint actions, and its helicity eigenvalues are $\pm2$, the statement that the graviton field's two massless polarizations differ by two units of helicity. The machinery is the same in every integer-spin case; only the tensor rank and the projection change.

The dimension count makes the projection explicit. The full tensor square of $V$ has complex dimension $9$ and decomposes as

$$
1\otimes1 = 0\oplus1\oplus2,
\qquad
9 = 1+3+5 .
$$

The symmetric part of the square has dimension $6$ and contains the spin-$2$ and spin-$0$ pieces, $6=5+1$; the traceless symmetric part has dimension $5$ and is the spin-two carrier; the trace is the spin-zero singlet; and the antisymmetric part, of dimension $3$, is again the adjoint triplet of spin one. Each piece is obtained from the tensor square by a projection that uses only the symmetry of the indices and the bilinear form: no new algebraic structure is needed.

The additivity of the angular momentum across factors is the Leibniz rule in disguise. Because each $J_k$ is a derivation, its action on a product of material vectors is the sum of its actions on the factors,

$$
J_k(X_1X_2\cdots X_s) = \sum_{a=1}^{s}X_1\cdots (J_kX_a)\cdots X_s,
$$

which is exactly the statement that the total internal angular momentum of a composite is the sum of the internal angular momenta of its parts. The rule that combines the angular momenta of composite systems is therefore not imposed on the algebra from outside; it is the derivation property, and the higher integer-spin carriers inherit their transformation law from it.

## Quantization of Integer-Spin Fields

### Bosonic Modes

An integer-spin field is quantized with commutators, not anticommutators. The mode expansion carries one oscillator pair for each of the $2s+1$ polarizations at each momentum,

$$
\hat{\Phi}(x) = \int\!\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2\omega_{\mathbf{p}}}}
\sum_{r=1}^{2s+1}\left[
\chi^r(\mathbf{p})\,\hat{a}_r(\mathbf{p})\,e^{-ip_\mu x^\mu}
+ \chi^{r*}(\mathbf{p})\,\hat{a}_r^\dagger(\mathbf{p})\,e^{+ip_\mu x^\mu}
\right],
$$

with polarization labels $\chi^r$ and mode operators satisfying

$$
\left[\hat{a}_r(\mathbf{p}),\hat{a}_s^\dagger(\mathbf{q})\right]
= \delta_{rs}(2\pi)^3\delta^{(3)}(\mathbf{p}-\mathbf{q}),
\qquad
\left[\hat{a}_r(\mathbf{p}),\hat{a}_s(\mathbf{q})\right]=0 .
$$

The Fock space is the symmetric (bosonic) algebra over the one-particle space, and the Hamiltonian is normal-ordered, $:\hat{H}:=\int d^3p/(2\pi)^3\,\omega_{\mathbf{p}}\sum_r\hat{a}_r^\dagger\hat{a}_r$, with $2s+1$ half-quanta per mode in the vacuum energy. For a massive integer-spin field the $2s+1$ polarizations all have positive norm, as in the Proca case; for a massless one the covariant description requires the indefinite metric and the subsidiary condition, and the physical polarizations are the two helicity states $\pm s$.

The reason the bracket must be a commutator is the spin–statistics theorem, which the companion article *The Spin–Statistics Theorem in Biquaternionic Form* treats in the framework's terms. Its content here is the linkage between the adjoint action and the bosonic algebra: integer spin means that the internal angular momentum eigenvalues are integers, and the exchange of two identical particles must return the state to itself, so the mode operators commute. A hypothetical integer-spin field quantized with anticommutators would have a state of the wrong exchange symmetry, and the theorem forbids it. The algebra does not independently forbid it — the Fock companion proves that the bracket is not native to $\mathbb{B}$ — but the representation theory that the adjoint action realizes is what the theorem uses.

### Positivity, Gauge, and the Two Massless States

The massive integer-spin case is the case in which the little group is $\mathrm{SO}(3)$ and all $2s+1$ states are physical, with positive norm. The massless case is the case in which the little group contracts to $\mathrm{ISO}(2)$ and the physical states are the two of helicity $\pm s$; the remaining $2s-1$ states are removed by the gauge symmetry, and their removal costs the indefinite metric in a covariant description. The Proca-to-Maxwell transition of the preceding article is the $s=1$ instance: three positive-norm states become two physical states plus the two unphysical ones that the subsidiary condition removes, precisely when the mass vanishes and the gauge symmetry appears. The same pattern holds for every integer $s$, and the pattern is a property of the little group, not of the algebra.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The inner derivations $\mathrm{ad}_{ie_k}$ as the rotation generators, and the fact that they preserve the material sector; the invariant vector part $V$ and the scalar direction $ie_0$, giving the internal decomposition $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0\}\oplus V$; the commutation relations $[J_i,J_j]=i\varepsilon_{ijk}J_k$; the Casimir eigenvalue $J^2=2I$, which is the algebraic statement of spin one; the weight basis $\varepsilon_\pm,\varepsilon_0$ and the ladder structure $J_\pm$; the identity $J_3^3=J_3$; the tensor-power construction of the higher integer-spin carriers, with the trace removal supplied by the algebra's bilinear form.

**Imported, and left visible.** The Wigner classification and the little-group analysis; the bosonic oscillator algebra and the Fock construction; the normal-ordering and positivity arguments; the spin–statistics theorem, cited to the companion article; the Clebsch–Gordan series used to identify the content of the rank-two tensor; and the identification of the adjoint action's triplet with the polarizations of the massive vector field, which is a physical reading of an algebraic fact.

**Not supplied.** A derivation of why the physical fields should live in the adjoint representation rather than in some other representation of the rotation algebra, apart from the vector character of the fields; the value of the spin of any given particle; and any empirical content. The construction shows that if a spin-one field is placed in the material sector, the algebra supplies the triplet and its ladder; it does not select the material sector.

## Open Questions

1. **The internal action for higher spin.** For $s\ge2$ the internal angular momentum is the sum of adjoint actions on the tensor factors, and the trace removal uses the bilinear form. Is there an irreducible algebraic object — a rank-$s$ symmetric traceless element built from a single biquaternion rather than a tensor power — that carries the spin-$s$ representation, and does such an object exist for every $s$?

2. **Spin and sector.** The adjoint action on $\mathbb{M}_-$ gives the triplet and on $\mathbb{M}_+$ gives another triplet; the two sectors are exchanged by multiplication by $i$. Does the physical spin-one field select one sector, and is the selection the same one that the Proca Lagrangian makes by placing the potential in $\mathbb{M}_-$?

3. **The spin-one state module.** For spin $\tfrac12$ the state module is a left ideal, of which there are many; for spin one the carrier is the invariant subspace $V$, of which there is one. Is the uniqueness of the integer-spin carrier an algebraic theorem, and does it explain why integer-spin representations are the ones the algebra realizes without a choice?

4. **The ladder and the mode algebra.** The ladder operators $J_\pm$ of the spin-one multiplet are algebraic; the mode operators $\hat{a}_r$ are not. Is there a deformation or a completion of $\mathbb{B}$ in which the two are the same kind of object, so that the spin ladder is the mode algebra of the field?

5. **The helicity-zero state.** The longitudinal state is physical for $\mu\neq0$ and removed at $\mu=0$. Is there an algebraic characterization of the removal — a projection in $\mathbb{B}$ that annihilates the $\lambda=0$ polarization exactly when the mass vanishes — that would make the gauge structure an algebraic statement rather than a limit?

6. **Empirical content.** As everywhere, whether the identification of the spin-one carrier with the material sector yields any prediction distinguishing the framework from standard integer-spin field theory. It does not, in the construction given here.

## Summary

Integer-spin quantization in the biquaternion framework rests on an identification: the adjoint action of the rotation algebra on the vector part of the material sector **is** the spin-one representation. The rotation generators are the inner derivations $J_k=\tfrac12\mathrm{ad}_{ie_k}$, the vector part $V=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ is invariant, and the imaginary scalar direction $ie_0$ is fixed, so that $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0\}\oplus V$ decomposes into an internal spin-$0$ and spin-$1$ piece.

The representation was computed explicitly: $[J_i,J_j]=i\varepsilon_{ijk}J_k$ with residual zero, the Casimir $J^2=2I$ with residual zero, the weight basis $\varepsilon_\pm=(e_1\pm ie_2)/\sqrt2$ and $\varepsilon_0=e_3$ with $J_3$ eigenvalues $\pm1,0$, and the identity $J_3^3-J_3=0$ that characterizes the triple. The ladder operators $J_\pm=J_1\pm iJ_2$ shift between the weights with matrix element $\sqrt2$. The triplet is the polarization triad of the massive vector field, and the massless theory retains the two helicity states $\pm1$ while the gauge structure removes the $\lambda=0$ state.

For general integer spin the carrier is the symmetric traceless rank-$s$ tensor of $V$, the angular momentum is the sum of the adjoint actions on the factors, and the trace removal is effected by the algebra's bilinear form. The rank-one case is the adjoint action itself; the rank-two case is the graviton, with helicity $\pm2$. Integer-spin fields are quantized bosonically, with $2s+1$ mode pairs and positive norm in the massive case, and with the indefinite metric and the subsidiary condition in the massless one; the linkage between integer spin and commuting mode operators is the content of the spin–statistics theorem, which the algebra respects but does not by itself prove.

What the algebra supplies is the triplet, its ladder, its Casimir, and the tensor-power construction of the higher integer-spin carriers. What it does not supply is the physical selection of the material sector as the home of the vector field, the mode algebra, or any empirical content.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_-=\mathrm{span}_{\mathbb{R}}\{ie_0,e_1,e_2,e_3\}$ | Material sector (anti-Hermitian) |
| $\mathbb{M}_+=\mathrm{span}_{\mathbb{R}}\{e_0,ie_1,ie_2,ie_3\}$ | Informational sector (Hermitian) |
| $V=\mathrm{span}_{\mathbb{C}}\{e_1,e_2,e_3\}$ | Vector part of the material sector; spin-one carrier |
| $\mathrm{ad}_XY=[X,Y]$ | Inner derivation (adjoint action) |
| $R_Q(X)=QXQ^{-1}$ | Inner automorphism; rotation for $Q=e^{\theta e_k/2}$ |
| $J_k=\tfrac12\mathrm{ad}_{ie_k}$ | Hermitian angular-momentum (spin) generator |
| $\mathbf{L}=\tilde{x}\times\tilde{p}$, $\mathbf{S}_k=J_k$ | Orbital and internal parts; $\mathbf{J}=\mathbf{L}+\mathbf{S}$ |
| $[J_i,J_j]=i\varepsilon_{ijk}J_k$ | Rotation algebra (verified, residual zero) |
| $J^2=J_1^2+J_2^2+J_3^2=2I$ | Casimir; $2=s(s+1)$ at $s=1$ |
| $\varepsilon_\pm=(e_1\pm ie_2)/\sqrt2$, $\varepsilon_0=e_3$ | Weight basis of the triplet; $J_3$ eigenvalues $\pm1,0$ |
| $J_\pm=J_1\pm iJ_2$ | Ladder operators, matrix element $\sqrt2$ |
| $J_3^3-J_3=0$ | Minimal polynomial of the spin-one generator |
| $\chi^r$, $r=1,\dots,2s+1$ | Polarization labels of a spin-$s$ field |
| $\hat{a}_r,\hat{a}_r^\dagger$ | Bosonic mode operators, $[\hat{a}_r,\hat{a}_s^\dagger]=\delta_{rs}(2\pi)^3\delta^{(3)}$ |
| $\lambda=\hat{\mathbf{p}}\cdot\mathbf{J}$ | Helicity; eigenvalues $\pm s$ |
| $\mathbf{S}^{(s)}_k=\sum_a I\otimes\cdots\otimes J_k\otimes\cdots\otimes I$ | Internal spin for rank-$s$ carriers |

## Further Reading

- Eugene P. Wigner, "On Unitary Representations of the Inhomogeneous Lorentz Group," *Annals of Mathematics* **40** (1939) 149–204, for the little-group classification of particles by mass and spin.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the construction of integer-spin fields and the $(2s+1)$ counting.
- Wu-Ki Tung, *Group Theory in Physics* (World Scientific, 1985), for the rotation-group representations, the Casimir eigenvalues, and the ladder operators.
- Morton Hamermesh, *Group Theory and Its Application to Physical Problems* (Addison-Wesley, 1962), for the symmetric traceless tensor realization of the spin-$s$ representation and the Clebsch–Gordan series.
- Ian J. R. Aitchison and Anthony J. G. Hey, *Gauge Theories in Particle Physics, Vol. I* (CRC Press, 4th ed., 2012), for the little-group analysis of massive and massless vector fields and the counting of polarizations.
- Paul A. M. Dirac, *The Principles of Quantum Mechanics*, 4th ed. (Oxford, 1958), for the angular-momentum algebra and the spin multiplets.
