# __Remaining Non-Hermitian Adjoints Outside the Gauge Sector__

## Scope

This file is an **inventory**, not a list of defects. It records every remaining place outside the gauge sector where a conjugation is written with an inverse, and states for each whether the Hermitian adjoint could stand in its place.

The answer divides the corpus in four groups, and only one of them is an exception:

| group | articles | lines | can the star replace the inverse? |
|---|---|---|---|
| star is not the adjoint | 2 | 3 | no |
| star is the adjoint | 3 | 10 | yes, value unchanged |
| bivector law, star not applicable | 7 | 21 | no |
| outside the algebra | 3 | 8 | no sandwich exists |

Four clauses already deleted are not listed: the two pointers in *Conventions in the Biquaternion Universe* and *The Six Subspaces*, the form clause in *The Exponential and the Generator*, and the duplicate notation row in *Charge Conjugation and the Division Ring*.

Quotations are verbatim, except that link targets inside a quoted paragraph are rebased to this file's location.

Nine articles cannot be written with the star: two in group 1 and the seven in group 3. Three more can, with no change of value. Three are outside the algebra. Fifteen articles, forty-two lines, one defect.

The earlier version of this file counted eight articles, omitted the seven bivector-law articles entirely, and left the exercise's false conclusion standing. The quotations and line numbers of the original eight entries are unchanged.

## 1. The Star Is Not the Adjoint: Three Lines

### 1. [Exercise: Duality Rotation and the Riemann-Silberstein Vector](../articles_physics/exercise-duality-rotation-and-the-riemann-silberstein-vector.html), lines 318, 331

The candidate conjugation gives instead
$$
\tilde U\,\vec e_x\,\tilde U^{*} = \vec e_x, \qquad
\tilde U\,\vec e_y\,\tilde U^{*} = \vec e_y,
\qquad
\tilde U\,\vec e_z\,\tilde U^{*} = \cosh\psi\,\vec e_z - i\sinh\psi,
$$
(so the candidate does not even preserve the pure-vector subspace on $\vec e_z$, producing a scalar part), hence
$$
\tilde U\,\tilde F\,\tilde U^{*} = iE_0\,\vec e_x,
$$
which is **not** $\tilde F_{\mathrm D}$: the transverse electric field is left unchanged, with no $\cosh\psi$ enhancement and no induced magnetic field. The natural candidate fails on a boost. This is the sharpest form of the gap: the four-vector conjugation, which is the only Lorentz action the parents exhibit, is not the Lorentz action of the field strength.

**Solution (c).** For the same boost, the transformation
$$
\tilde F \mapsto \tilde U^{\natural}\,\tilde F\,\tilde U = \tilde U^{-1}\,\tilde F\,\tilde U
$$
does reproduce the standard result:
$$
\tilde U^{\natural}\,\vec e_x\,\tilde U = \cosh\psi\,\vec e_x - i\sinh\psi\,\vec e_y,
\qquad
\tilde U^{\natural}\,\vec e_y\,\tilde U = \cosh\psi\,\vec e_y + i\sinh\psi\,\vec e_x,
$$
so
$$
\boxed{\;\tilde U^{\natural}\,\tilde F\,\tilde U
= i\cosh\psi\,E_0\,\vec e_x + \sinh\psi\,E_0\,\vec e_y = \tilde F_{\mathrm D}\;}.
$$
The boost is therefore reproduced by $\tilde U^{-1}\tilde F\tilde U$, while the rotation of part (a) is reproduced by $\tilde U\tilde F\tilde U^{*}$. The two cases require different orderings, so no single one of these adjoint actions, with the parents' rotor conventions, is the Lorentz transformation law of $\tilde F$. The parent gives no law at all, and its claim that the two pieces "transform independently under the Lorentz group" is therefore unverified: the abstract representation-theoretic statement that the self-dual and anti-self-dual pieces carry the two complex conjugate three-dimensional representations is standard, but the biquaternion realization of that statement is not supplied, and the obvious candidate for it is false. Determining the correct biquaternion action — plausibly an adjoint action conjugated by a fixed linear map on the field-strength space — is left open. **This is the gap this exercise reports in its parent.**

**Remaining issue.** Line 318 writes $\tilde U^{-1}\tilde F\tilde U$ and proves it correct. Line 331 says the rotation needs $\tilde U\tilde F\tilde U^{*}$ and the boost needs this other ordering. The inverse cannot become the star: at line 290 the boost rotor is Hermitian, $\tilde U^{*}=\tilde U$, and the star gives $\tilde U\tilde F\tilde U$, which line 312 shows is wrong.

**Remaining defect.** The inverse is correct and must stay. The defect is the conclusion drawn from it. Lines 331 and 359 state that the rotation needs $\tilde U\tilde F\tilde U^{*}$, the boost needs $\tilde U^{-1}\tilde F\tilde U$, and therefore that "no single one of these adjoint actions" is the Lorentz transformation law of $\tilde F$. That is false. The rotation agrees because a real rotation rotor satisfies $\tilde u^{*}=\tilde u^{\natural}=\tilde u^{-1}$: it is the degenerate case of one law, not a second law. The residual disagreement is a convention, since part (a) rotates the field actively by $+\varphi$ while part (b) boosts the frame passively by $+v_b$.

**No action on the formula.** The conclusion at lines 331 and 359 needs correcting in the article; the inverse stays.

### 2. [The Eigenspinor](../articles_physics/the-eigenspinor-the-lorentz-rotor-as-a-function-of-proper-time.html), line 77

**The four-momentum and the four-velocity.** For this boost the rotor is Hermitian, $\tilde U^{*} = \tilde U$, and of unit biquaternion norm, $\langle\tilde U\rangle_{\natural} = 1$, so $\tilde U\tilde U^{*} = \tilde U^2 = \gamma(e_t - i\beta\vec u)$ with $\beta = v/c$. Hence

$$
\tilde{P} = imc\,\tilde U^2 = i\gamma mc\,(e_t - i\beta\vec u) = m\gamma(ic\,e_t + \vec v),
$$

**The eigenprojection reading.** The two eigenprojections of the momentum are $\tilde\Pi_\pm=\tfrac12(e_t\mp i\vec u_p)$. For the pure boost along $\vec u_p$ they are fixed by the eigenspinor, $\tilde U\tilde\Pi_\pm\tilde U^{-1}=\tilde\Pi_\pm$, because the boost commutes with its own axis and with $e_t$; the eigenspinor moves the spin frame and not the momentum projectors. The residual rotor of the rest frame acts on them by conjugation and carries them among the minimal idempotents, which is the spin freedom of *Two gauges* above. Read this way, the eigenspinor is the transport of the spin frame, and the eigenvalue decomposition of the momentum is the pair of projectors that the transport leaves invariant; [The Spectral Reading of a Four-Vector](../articles_physics/the-spectral-reading-of-a-four-vector.html) gives the spectral form of that pair.

**Remaining issue.** Line 59 states $\tilde U^{*}=\tilde U$ for the boost. Line 77 conjugates the eigenprojections by $\tilde U^{-1}$. The star would fix them instead of moving them, so the inverse must stay. The natural conjugate $\tilde U^{\natural}$ is equal to it and is already defined at line 57.

**No action.** The inverse is the quaternion conjugate, the natural conjugation on this slice. Writing $\tilde U^{\natural}$ is a notation choice, not a correction.

## 2. The Star Is the Adjoint: No Action

### 3. [The Neutrino and Majorana Fermions](../articles_physics/the-neutrino-and-majorana-fermions-in-biquaternionic-form.html), lines 61, 120

Charge conjugation is a **conjugate-linear** map on the Dirac module. In four dimensions it is written with a charge-conjugation matrix $C$ acting on the Dirac conjugate,

$$
\psi^{c} \;=\; C\,\bar{\psi}^{\,T},
\qquad
\bar{\psi} \;=\; \psi^{\dagger}\gamma^0 ,
$$

and the matrix is fixed by the requirement that the kinetic term be preserved,

$$
C\,\gamma^{\mu\,T}\,C^{-1} \;=\; -\,\gamma^{\mu}.
$$


The transpose, not the inverse or the conjugate, appears because $C$ is the matrix of a bilinear pairing on the module. Two features of this definition must be stated before it is used, and they are the two traps of the subject.

**The matrix is basis-dependent, and the reality condition is basis-dependent in form.** A change of Clifford basis $\gamma^\mu\mapsto S\gamma^\mu S^{-1}$ sends $C\mapsto SCS^{T}$, so the explicit matrix changes with the basis even though the map it defines does not. In the block basis of the Conventions, with $g=\mathrm{diag}(+,-,-,-)$, the choice

$$
C \;=\; i\gamma^2\gamma^0 \;=\; \begin{pmatrix}\epsilon&0\\ 0&-\epsilon\end{pmatrix},
\qquad
\epsilon \;=\; i\sigma_2 \;=\; \begin{pmatrix}0&1\\ -1&0\end{pmatrix},
$$

is antisymmetric, $C^{T}=-C$, with $C^2=-I_4$ and $C^{\dagger}=C^{-1}$, and it satisfies $C\gamma^{\mu T}C^{-1}=-\gamma^\mu$ for $\mu=0,1,2,3$. The same map written in the Dirac basis $\gamma_{\mathrm D}^{0}=\mathrm{diag}(I_2,-I_2)$ has the charge-conjugation matrix $S C S^{T}$, which is a different matrix. The existence of a charge-conjugation matrix is a statement about the signature, not about the basis; its form is a statement about the basis. A calculation that fixes a sign by comparing "$C$" across two papers that use different Clifford bases is comparing two different matrices.

| Statement | Verification |
|---|---|
| $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4$, $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3=\mathrm{diag}(-I_2,I_2)$ | all $16$ commutators and anticommutators, exact |
| $C^{T}=-C$, $C^2=-I_4$, $C^\dagger=C^{-1}$ | exact, $C=i\gamma^2\gamma^0$ |
| $C\gamma^{\mu T}C^{-1}=-\gamma^\mu$ | all $\mu=0,1,2,3$ |

**Remaining issue.** $C^{-1}$ in the defining relation. Line 74 states $C^{\dagger}=C^{-1}$, and the notation row at 119 repeats it. The inverse is already the Hermitian adjoint.

**Fix.** $C^{-1}\to C^{\dagger}$ at lines 61 and 120. Value unchanged. The transpose of $\gamma^{\mu}$ remains, and a biquaternion sandwich has no transpose.

### 4. [The Biquaternion Basis of a Unified Field Fibre Bundle](../articles_physics/the-biquaternion-basis-of-a-unified-field-fibre-bundle.html), lines 116, 220

The source's Section V performs Majorana's 1937 transformation on the same $G$, with the aim stated in its own words: to obtain a $*$-unitary transformation for which the Dirac equation becomes "with real coefficients and symmetric for both: fermions and antifermions". The transformation is the Weyl-basis charge conjugation,

$$
\tilde U = \tilde U^{-1} = \frac{1}{\sqrt2}\begin{pmatrix} \sigma_0 & \sigma_2 \\ \sigma_2 & -\sigma_0 \end{pmatrix} ,
$$

attributed by the source to Majorana. It was verified to be $*$-unitary and involutive, $\tilde Q^\dagger \tilde Q = \tilde Q^2 = I_4$, with a worst deviation of $2.2\times10^{-16}$.

The source's own generators are printed in its Eq. (28) as $\gamma_0 = \sigma_0\oplus\sigma_0$ with $\gamma_k = \begin{pmatrix} 0 & -\sigma_k \\ \sigma_k & 0\end{pmatrix}$. As printed they are **not** a Clifford set: $\{\gamma_0,\gamma_k\} = 2\gamma_k$, which does not vanish, so the displayed $\gamma_0$ has lost a sign and must be $\sigma_0\oplus(-\sigma_0)$. With that single correction the four generators satisfy the whole algebra for the metric $\mathrm{diag}(+1,-1,-1,-1)$ — every square and every anticommutator verified exactly. The correction does not touch $G$ itself, because the source writes $G = a_0I_4 + \boldsymbol\gamma\!\cdot\!\vec a$ with the identity, not $\gamma_0$, in the timelike slot.

**The verified effect.** The source's Eq. (34) is the transformation the corpus needs, and with it the source's stated purpose is achieved. Recomputing $G_2 = \tilde UG\tilde U^{-1}$ term by term and recomposing it gives

$$
G_2 = a_0 I_4 + \gamma_{2,1} a_1 + \gamma_{2,2} a_2 + \gamma_{2,3} a_3
$$

| Symbol | Meaning |
|---|---|
| $P(G,M)$, $G$ | The source's principal fibre bundle and its structural group, the "single geometrical structure" of the unified theory |
| $G = \begin{pmatrix} A & B \\ -B & A \end{pmatrix}$, $A = a_0\sigma_0$, $B = \boldsymbol\sigma\!\cdot\!\vec a$ | The source's structural group; the regular representation of the pair $(A,B)$, not the real form of $Q$ |
| $Q = a_0\sigma_0 - i\boldsymbol\sigma\!\cdot\!\vec a = A - iB$ | The source's $2\times2$ spinorial matrix; equals $\mathsf{M}_2(\tilde Q)$ |
| $\tilde Q = a_0 + \vec a\!\cdot\!\mathbf e$, $a_0 = p_0/m$, $\vec a = i\vec p/m$ | The biquaternion behind $Q$; Hermitian, of unit norm on the mass shell |
| $a_0^2+a_1^2+a_2^2+a_3^2 = 1$ | The source's Eq. (19); with imaginary $a_k$ it is $\langle\tilde Q\rangle_{\natural} = 1$ and the mass shell |
| $\langle\tilde Q\rangle_{\natural} = \tilde Q\tilde Q^{\natural} = \det\mathsf{M}_2(\tilde Q)$ | The biquaternion norm; the source's $N = 1$, the corpus's $\langle\tilde P\rangle_{\natural} = -m^2$ in $\mathbb{M}_-$ |
| $G^+ = \begin{pmatrix} A & -B \\ B & A \end{pmatrix}$ | The source's conjugate transpose: ordinary transpose with quaternionic conjugation, not the matrix adjoint; identical to the ordinary transpose whenever $B$ is symmetric, i.e. whenever the coefficient of $\sigma_2$ vanishes, which is the slice on which $G^+G = I_4$ is the Euclidean orthogonality condition |
| $G = A\,I_4 + B\,J$, $J^2 = -I_4$ | The source's Eq. (4); equivalently $G = I_2\otimes A + J_2\otimes B$ |
| $G_2 = \tilde UG\tilde U^{-1}$ | The Majorana-transformed structural group; real and symmetric |

**Remaining issue.** $\tilde U^{-1}$ in the similarity $G_2=\tilde UG\tilde U^{-1}$. Line 112 states $\tilde U^{\dagger}\tilde U=I_4$, so the inverse is the matrix adjoint.

**Fix.** $\tilde U^{-1}\to\tilde U^{\dagger}$ at lines 116 and 220. The object is a $4\times4$ matrix, not an element of $\mathbb{B}$.

### 5. [The Skyrme Model and the Topological Baryon](../articles_physics/the-skyrme-model-and-the-topological-baryon-in-biquaternionic-form.html), lines 21, 50, 58, 150, 223, 273

- **Established, and recomputed below.** The topological current
$$
B^\mu = \frac{1}{24\pi^2}\,\varepsilon^{\mu\nu\rho\sigma}\,\mathrm{Tr}\!\left(j_\nu j_\rho j_\sigma\right),
\qquad
j_\mu = \tilde U^{-1}\partial/\partial Q_\mu\,\tilde U ,
$$
is conserved identically, and its charge is the degree of the map $\tilde U:\mathbb{S}^3\to\mathbb{S}^3$. For the hedgehog configuration $\tilde U = \cos F(r)\,e_t + \sin F(r)\,\vec u_r$ the charge is


$$
\tilde U(\tilde{Q})\in\mathbb{H}^1_{\mathbb{B}} ,
\qquad
\tilde U = \exp\!\left(\frac{\vec\pi}{f_\pi}\right),
\qquad
\tilde U^{-1} = \tilde U^{\natural} = \tilde U^{*} ,
$$

where the last identities hold because $\tilde U$ is a unit real quaternion. The field takes values in the manifold $\mathbb{S}^3$, and the analyses of this article are static: the energy functional is evaluated on configurations $\tilde U(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$ that are pure gauge at spatial infinity, $\tilde U(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\to e_t$ as $|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|\to\infty$, so that they extend to maps $\mathbb{S}^3\to\mathbb{S}^3$.

**The current.** The Maurer–Cartan form of the companion article is

$$
j_\mu = \tilde U^{-1}\partial/\partial Q_\mu\,\tilde U \in\mathfrak{su}(2)\subset\mathbb{M}_- ,
$$

**Remaining issue.** The Maurer-Cartan current $j_\mu=\tilde U^{-1}\partial_\mu\tilde U$. Line 50 states $\tilde U^{-1}=\tilde U^{\natural}=\tilde U^{*}$ for the field.

**Fix.** $\tilde U^{-1}\to\tilde U^{\natural}$ at all six lines (21, 50, 58, 150, 223, 273). Value unchanged. This one changes a standard convention: the left-invariant current is normally written with the inverse.

## 3. The Bivector Law: Seven Articles the Earlier Version Omitted

The field strength is a bivector, and its law is $\tilde F_2=\tilde U^{\natural}\tilde F\tilde U=\tilde U^{-1}\tilde F\tilde U$. These articles state it and were not listed before.

| article | lines |
|---|---|
| [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html) | 385 |
| [Higher Multipoles and the Field-Strength Decomposition](../articles_physics/higher-multipoles-and-the-field-strength-decomposition-in-biquaternionic-form.html) | 260, 382, 414 |
| [The Boost of a Plane Wave as a Rotation and a Dilation](../articles_physics/the-boost-of-a-plane-wave-as-a-rotation-and-a-dilation.html) | 20, 25, 167, 172, 214 |
| [The Lorentz Force in Biquaternion Form](../articles_physics/the-lorentz-force-in-biquaternion-form.html) | 507, 522, 630 |
| [The Relativistic Quadrupole](../articles_physics/the-relativistic-quadrupole-in-biquaternionic-form.html) | 208, 404 |
| [The Relativistic Particle in an External Field](../articles_physics/the-relativistic-particle-in-an-external-field-in-biquaternionic-form.html) | 296 |
| [Exercise: The Electromagnetic Field of a Moving Charge](../articles_physics/exercise-the-electromagnetic-field-of-a-moving-charge.html) | 293, 306, 334, 346, 364, 400 |

The sharpest statement is in *The Relativistic Particle in an External Field*, line 296:

> With that convention the four-velocity, the four-momentum, and the four-force all transform by the **vector** rule, $\tilde{Q}_{\mathrm L} = \tilde U_{\mathrm b}\tilde{Q}\tilde U_{\mathrm b}^{*}$, because all three lie in $\mathbb{M}_-$. The field strength does **not**: it transforms by the **bivector** rule $\tilde{F}_2 = \tilde U_{\mathrm b}^{\natural}\tilde{F}\tilde U_{\mathrm b}$, the same rule used in the Lorentz-force article.

*The Lorentz Force* states the same distinction at line 504: "The field strength is *not* a four-vector, and it does not transform like one."

None of the seven is a defect. They are listed because the earlier version of this file claimed to be complete.

## 4. Clifford Layer: Cannot Be Removed

### 6. [Charge Conjugation and the Division Ring](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html), lines 7, 62, 107, 137

Charge conjugation is the pseudoautomorphism $\bar{A}=\Pi A^{*}\Pi^{-1}$ of a real Clifford algebra, and the matrix $\Pi$ that implements it is fixed by the algebra's division ring. Over a real division ring $K\cong\mathbb{R}$ it is proportional to the identity and the conjugation is trivial; over a quaternionic ring $K\cong\mathbb{H}$ it is a genuine product of generators and the conjugation interchanges particle and antiparticle; over the complex field it is a conjugation between conjugate representations. The three cases are the three charge classes: charged particles at $Ϙ=+1$, neutral particles with antiparticles at $Ϙ=0$, and truly neutral particles at $Ϙ=\bar{0}$. The twice-conjugated spinor is $\bar{\bar{\xi}}=\pm\xi$, with the sign the sign of $\Pi\bar{\Pi}$; for the fundamental representation of $\mathrm{Spin}^{+}(1,3)$ the sign is $+1$, so $C^{2}=1$, an invariant fact of the spinor structure and the algebraic expression of the standard requirement on charge conjugation.

- The charge-conjugation pseudoautomorphism is $\bar{A}=\Pi A^{*}\Pi^{-1}$, conjugate-linear, with $\Pi\gamma_{\vec u_a}\Pi^{-1}=-\gamma_{\vec u_a}$; it is not an automorphism of the real form, and this is the algebra-level form of the CPT article's finding that $C$'s internal matrix is odd.

**Remaining issue.** The map $\bar A=\Pi A^{*}\Pi^{-1}$ is the subject of the article. $\Pi$ is a product of odd Clifford generators, outside $\mathbb{B}$, and $\Pi^{2}=\pm1$, so the inverse is an involution. The map is conjugate-linear in $A$, so no Hermitian sandwich reproduces it.

**No action.** Lines 7 and 62 refer to the same map. The duplicate notation row was removed; these four occurrences stay.

### 7. [The CPT Theorem](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html), lines 242, 307, 336

**Charge conjugation is the pseudoautomorphism.** $C$ is the one operation that is not a fundamental automorphism. In the classification it is the map

$$
A\;\mapsto\;\bar{A}=\Pi\,A^{*}\,\Pi^{-1},
$$

the **complex conjugation** of the algebra element followed by the inner automorphism by a matrix $\Pi$. Here $\Pi$ is a product of Clifford generators and is determined only up to a scalar, and it does not preserve the real subalgebra — it conjugates the generators with a sign, $\Pi\gamma_{a^{\mathrm{fop}}}\Pi^{-1}=-\gamma_{a^{\mathrm{fop}}}$ — which is exactly why the map is a *pseudo*automorphism rather than an automorphism of $\mathrm{Cl}_{n,m}$. Theorem 1 of the source fixes the form of $\Pi$ by the division ring of the real subalgebra: for a real division ring $K\cong\mathbb{R}$ it is proportional to the unit matrix, and for a quaternionic one $K\cong\mathbb{H}$ it is a product of generators with $\Pi\bar{\Pi}=\pm I$. The matrix $\Pi$ is the charge-conjugation matrix, and it is at the algebra level the object that the module computation above fixes to $\eta_C=i\gamma^2$ up to the free phase; the classification is also where that free phase comes from, since $\Pi$ is determined only up to a scalar. The twisted character of $C$ — that it is not one of the algebra's three untwisted involutions — is the classification's form of this article's operational finding that $C$'s internal matrix is **odd** and outside $\mathbb{B}$.

The Clifford-algebra literature supplies a second interpretation of the same eight operations: they are the three non-trivial fundamental automorphisms of $\mathrm{Cl}_{n,m}$ — the grade involution, the reversion and their composite, the Clifford conjugation — together with their composites with the charge-conjugation pseudoautomorphism $A\mapsto\Pi A^{*}\Pi^{-1}$, and they generate $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_2$. The algebra's own conjugations $\bar{\cdot}$, ${}^{*}$ and ${}^{\natural}$ are exactly the three untwisted maps, while $C$ is the twisted one, which is the algebraic form of the article's finding that $C$ is not an inner operation of $\mathbb{B}$. That classification is transcribed, and the step from it to the module intertwiners is left open.

**Remaining issue.** Same map, same reason. The article itself says $\Pi$ is a Clifford generator, odd and outside $\mathbb{B}$.

**No action.** Definition and notation. The notation row at line 336 repeats it.

### 8. [Antilinear Structure and the Two Kinds of Mass](../articles_physics/antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html), line 193

The word "charge conjugation" is used at four levels in the corpus, and the table below fixes which object each level names. The name itself is reserved for **level 3**, the operation on the Dirac module. The levels above it are structures of the pairing, and the level-1 map $\flat$ carries the *shape* of the pairing and not the operation.

| level | object | space | what it is |
|---|---|---|---|
| 1, the algebra | $\flat=-{}^{*}$ | $\mathbb{B}$, real dim $8$ | the algebra's real structure, fixed space $\mathbb{M}_-$; the **shape** of a charge-conjugation pairing |
| 2, the Clifford algebra | $\bar{A}=\Pi A^{*}\Pi^{-1}$ | $\mathrm{Cl}_{n,m}$ | the charge-conjugation **pseudoautomorphism**; $\Pi$ is odd and lies outside $\mathbb{B}$ |
| 3, the module | $C[\psi]=i\gamma^{2}\psi^{*}$ | $\Delta$ | **charge conjugation**; the particle–antiparticle operation |
| 4, the module real structure | $\bar{\cdot}$ | $\Delta\cong S\oplus\bar{S}$ | the fixed-point real structure transported to the module; fixed points $\mathbb{H}_{\mathbb{B}}$ |

**Remaining issue.** Level 2 of a four-level table. Deleting the row leaves three levels and breaks the classification. The same row states that $\Pi$ is odd and outside $\mathbb{B}$.

**No action.** Classificatory.

## Summary

| group | articles | lines | action |
|---|---|---|---|
| star is not the adjoint | 2 | 3 | inverse stays; correct the conclusion at 331 and 359 |
| star is the adjoint | 3 | 10 | none; value unchanged |
| bivector law, star not applicable | 7 | 21 | none; listed for completeness |
| outside the algebra | 3 | 8 | none |

Fifteen articles, forty-two lines, one defect. Nine articles cannot be written with the star. Six can: three by substitution with no change of value, three because no biquaternion sandwich exists.

The one defect is not an adjoint. It is the sentence in *Exercise: Duality Rotation and the Riemann-Silberstein Vector* that reads a convention difference as a missing law. The law is $\tilde F_2=\tilde U^{\natural}\tilde F\tilde U$, and the corpus states it in eight articles.
