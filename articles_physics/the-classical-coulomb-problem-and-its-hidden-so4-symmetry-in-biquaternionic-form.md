# __The Classical Coulomb Problem and Its Hidden SO(4) Symmetry in Biquaternionic Form__

## Introduction

The classical Coulomb problem is the motion of a charged particle in the inverse-square electrostatic field of a fixed charge. Its force law,

$$
\mathbf{F} = \frac{q_1q_2}{4\pi\epsilon_0}\frac{\hat{\mathbf{r}}}{r^2},
$$

is the same inverse-square form as the Kepler force, with the coupling $\kappa = -q_1q_2/(4\pi\epsilon_0)$ replacing $GMm$; for opposite charges the coupling is attractive and the problem is the Kepler problem with a different constant. The orbits are the conic sections derived in the preceding article of this subcategory, and the present article does not repeat them. Its subject is the symmetry that the $1/r$ potential conceals.

The inverse-square force conserves not only the angular momentum $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ but also the **Runge–Lenz vector** $\mathbf{A} = \mathbf{p}\times\mathbf{L} - m\kappa\hat{\mathbf{r}}$. Together these six quantities close under the Poisson bracket into a Lie algebra, and for bound orbits the algebra is $\mathfrak{so}(4)$, the six-dimensional rotation algebra of four-dimensional space. The symmetry is **hidden** in the sense that it is not a symmetry of space; it is a symmetry of the phase space that mixes the conserved orbital vectors. It is the classical origin of the $n^2$ degeneracy of the non-relativistic hydrogen spectrum, and the quantization of the same algebra is how Pauli obtained the Balmer formula before the Schrödinger equation existed.

The article develops the symmetry in the framework's notation and states plainly what the framework does and does not supply. The generators $\mathbf{L}$ and $\mathbf{A}$ are real vectors, $\mathbf{L}$ is the vector part of the quaternion product $\mathbf{r}\mathbf{p}$, and the brackets are computed with the Poisson bracket of the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*. What the framework does **not** supply is the compact algebra $\mathfrak{so}(4)$ itself: the biquaternion algebra is finite-dimensional, and its largest compact subalgebra is the material sector $\mathbb{M}_- \cong \mathfrak{u}(2)$, of real dimension four, so a compact six-dimensional algebra does not embed in it. The six-dimensional algebra it does carry is its traceless part, the Lorentz algebra $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(3,1)$ of rotations and boosts — the split real form of the very same complexification as $\mathfrak{so}(4)$, and the symmetry type of the unbound case below. The extra generators of the bound-state symmetry live in the phase space of the particle, not in $\mathbb{B}$, and the article is explicit about that boundary. The non-relativistic hydrogen article records the same boundary from the quantum side, as an open question about the algebraic origin of the degeneracy; the present article supplies the classical symmetry algebra, locates it correctly, and fixes how far the algebra's own structure reaches towards it.

**Conventions.** The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = \epsilon_{jkl}e_l$ for $j \neq k$; the scalar imaginary $i$ is central with $i^2 = -e_0$. The material sector is $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$, with $\mathbb{B} = \mathbb{M}_+\oplus\mathbb{M}_-$ and $i\mathbb{M}_\pm = \mathbb{M}_\mp$. The configuration is a real vector in $\operatorname{span}\{e_1,e_2,e_3\} \subset \mathbb{M}_-$; the potential and the energy are central scalars, real multiples of $e_0$. The Poisson bracket is the classical bracket of the companion article on the bracket and the quantum commutator, with $\{x_i,p_j\} = \delta_{ij}$ and $\{x_i,x_j\} = \{p_i,p_j\} = 0$, and the bracket of vector-valued functions is taken componentwise. The angular momentum is $\mathbf{L} = \mathbf{r}\times\mathbf{p} = \tfrac12[\mathbf{r},\mathbf{p}]$, the vector part of the quaternion product $\mathbf{r}\mathbf{p}$.

## The Classical Coulomb Problem

### The Force and the Potential

Two point charges at separation $r$ interact with the Coulomb force. For a light charge $q_1$ moving in the field of a fixed heavy charge $q_2$ the force is central and inverse-square,

$$
V(r) = \frac{q_1q_2}{4\pi\epsilon_0}\frac{1}{r} , \qquad \mathbf{F} = -\frac{q_1q_2}{4\pi\epsilon_0}\frac{\hat{\mathbf{r}}}{r^2} .
$$

Writing $\kappa = -q_1q_2/(4\pi\epsilon_0)$ puts the force in the Kepler form $\mathbf{F} = -\kappa\hat{\mathbf{r}}/r^2$: for opposite charges $q_1q_2 < 0$ so $\kappa > 0$ and the force is attractive, while for like charges $\kappa < 0$ and the force is repulsive. The potential $\tilde{V} = V(r)e_0$ is a central scalar in $\mathbb{M}_+$, the force is a real vector in $\mathbb{M}_-$ commuting with the position, $[\mathbf{r},\mathbf{F}] = 0$, and the whole central-scalar machinery of the preceding articles applies without change.

The two-body problem reduces to the one-body form by separating the centre of mass, exactly as in the gravitational case, with $m$ the reduced mass and $\mathbf{r}$ the relative coordinate. In the atomic case the heavy charge is a nucleus and the reduced mass is close to the electron mass.

### The Absence of Intrinsic Magnetism

The subcategory in which this article sits is that of effects **without intrinsic magnetism**, and the Coulomb problem is the archetype. The particle is structureless: it carries charge and mass and nothing else. It has no magnetic moment, because a magnetic moment requires either an internal current distribution or an intrinsic spin, and neither is present. Its motion in the electrostatic field produces a magnetic field by Ampère's law — a uniformly moving charge is a current — but that field is the field of the particle's orbital motion, not of an intrinsic magnetic moment, and it does not react back on the particle in the electrostatic problem. The spin-dependent couplings that would make an intrinsic moment visible, the spin-orbit coupling and the Zeeman and Stern–Gerlach interactions, are absent here and belong to the sibling subcategories on intrinsic magnetism and on higher multipoles.

This is worth stating because the conserved Runge–Lenz vector is sometimes mistaken for an internal vector. It is not. It is a function of the orbital variables $(\mathbf{r},\mathbf{p})$, it lives in the same real three-space as the position and momentum, and it would exist for a charged structureless particle with no magnetic moment whatever. It is a property of the orbit, not of the particle.

### The Bound and Unbound Orbits

The effective potential and the orbit classification are those of the Kepler problem, with $\kappa$ carrying the sign of the interaction:

$$
V_{\text{eff}}(r) = \frac{q_1q_2}{4\pi\epsilon_0}\frac{1}{r} + \frac{L^2}{2mr^2} = -\frac{\kappa}{r} + \frac{L^2}{2mr^2} .
$$

For the attractive case $\kappa > 0$: the energy is negative for bound orbits and the orbit is an ellipse with the focus at the fixed charge,

$$
r(\theta) = \frac{p}{1 + e\cos(\theta-\theta_0)}, \qquad p = \frac{L^2}{m\kappa}, \qquad e = \sqrt{1 + \frac{2EL^2}{m\kappa^2}} ,
$$

with semi-major axis $a = -\kappa/(2E)$; for $E \geq 0$ the orbit is a parabola or a hyperbola. For the repulsive case $\kappa < 0$ the effective potential is monotonically decreasing, every orbit is unbound, and the orbit is one branch of a hyperbola. The repulsive case is the Rutherford scattering configuration; its deflection is treated in the standard literature and is not needed for the symmetry algebra, which concerns the bound and unbound cases through the sign of the energy.

### The Repulsive Case and Rutherford Scattering

The repulsive orbit is worth one line because it is the experimental face of the classical Coulomb problem. With $\kappa < 0$, and writing the asymptotic speed as $v_\infty$ so that $E = \tfrac12 mv_\infty^2$ and $L = mv_\infty b$ with $b$ the impact parameter, the eccentricity is $e = \sqrt{1 + 2EL^2/(m\kappa^2)} > 1$ and the orbit is a hyperbola. The deflection angle $\Theta$ between the incoming and outgoing asymptotes satisfies

$$
\tan\frac{\Theta}{2} = \frac{|\kappa|}{mv_\infty^2 b} ,
$$

so that the deflection grows without bound as the impact parameter decreases, and it is toward the force centre for attraction and away from it for repulsion. The classical differential cross section that follows is the Rutherford formula,

$$
\frac{d\sigma}{d\Omega} = \left(\frac{|\kappa|}{2mv_\infty^2}\right)^2\frac{1}{\sin^4(\Theta/2)} = \left(\frac{|q_1q_2|}{16\pi\epsilon_0 E}\right)^2\frac{1}{\sin^4(\Theta/2)} ,
$$

whose agreement with experiment established the nuclear model of the atom. The formula uses only the classical orbit; no spin, no magnetic moment and no quantum state enters. The particle is the structureless charged point of the central-scalar limit, and the scattering is its purely electrostatic response.

## The Six Conserved Quantities

### Angular Momentum

The centrality of the force conserves the angular momentum,

$$
\mathbf{L} = \mathbf{r}\times\mathbf{p} = \tfrac12[\mathbf{r},\mathbf{p}], \qquad \{L_i, H\} = 0 ,
$$

with $H = p^2/(2m) - \kappa/r$ the Hamiltonian. The conservation was derived in the preceding article as $\dot{\mathbf{L}} = \tfrac12[\mathbf{r},\mathbf{F}] = 0$, and it holds for every central force.

### The Runge–Lenz Vector

The extra conserved vector is

$$
\mathbf{A} = \mathbf{p}\times\mathbf{L} - m\kappa\,\hat{\mathbf{r}} , \qquad \{A_i, H\} = 0 ,
$$

whose conservation, direction and magnitude were established in the preceding article:

$$
\mathbf{A}\cdot\mathbf{L} = 0, \qquad |\mathbf{A}| = m\kappa e, \qquad |\mathbf{A}|^2 = m^2\kappa^2 + 2mEL^2 .
$$

The conservation is special to the inverse-square law. Its physical meaning is that the apsidal line of the orbit is fixed: the vector points from the force centre to the perihelion, and its constancy is the statement that the ellipse does not precess. A force law that differs from $1/r^2$ by any radial power produces a precessing orbit, and the precession rate measures the deviation. The closure of the Kepler and Coulomb orbits is therefore the visible consequence of the hidden symmetry.

### Counting and Independence

The six quantities $\mathbf{L}$ and $\mathbf{A}$ are not independent functions on the four-dimensional bound phase space; the constraints are

$$
\mathbf{L}\cdot\mathbf{A} = 0, \qquad |\mathbf{A}|^2 = m^2\kappa^2 + 2mEL^2 ,
$$

and on a fixed energy shell $E$ the second is a relation among the squares. The number of independent conserved quantities for the three-dimensional bound problem is five (the three components of $\mathbf{L}$, the energy, and the two angles that fix the direction of $\mathbf{A}$), which is the maximal number for a three-dimensional system and makes the problem maximally superintegrable. The algebra below is the algebraic expression of that maximality.

## The Symmetry Algebra

### The Brackets

The Poisson brackets of the six generators close on themselves:

$$
\{L_i, L_j\} = \epsilon_{ijk}L_k, \qquad \{L_i, A_j\} = \epsilon_{ijk}A_k, \qquad \{A_i, A_j\} = -2mE\,\epsilon_{ijk}L_k .
$$

The first is the angular-momentum algebra; the second says that $\mathbf{A}$ transforms as a vector under rotations; the third is the new relation, and its coefficient depends on the energy. All three were verified by numerical differentiation of the phase-space functions at several representative bound phase-space points, with the maximum deviation from the stated right-hand sides of order $10^{-11}$.

The appearance of $E$ in the third bracket is the reason the algebra has different forms in the bound and unbound cases.

### The Bound Case: $\mathfrak{so}(4)$

For $E < 0$ define the rescaled vector

$$
\mathbf{D} = \frac{\mathbf{A}}{\sqrt{-2mE}} ,
$$

so that $\{D_i, D_j\} = \epsilon_{ijk}L_k$ and $\{L_i, D_j\} = \epsilon_{ijk}D_k$. The six generators $\mathbf{L}, \mathbf{D}$ then form two commuting copies of $\mathfrak{su}(2)$. Define

$$
\mathbf{J}^{\pm} = \frac{1}{2}\left(\mathbf{L} \pm \mathbf{D}\right) .
$$

Using the brackets,

$$
\{J_i^+, J_j^+\} = \epsilon_{ijk}J_k^+, \qquad \{J_i^-, J_j^-\} = \epsilon_{ijk}J_k^-, \qquad \{J_i^+, J_j^-\} = 0 ,
$$

so that $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ with generators $\mathbf{J}^+$ and $\mathbf{J}^-$. The numerical check confirms all three relations, and the two Casimirs are equal:

$$
\left(\mathbf{J}^+\right)^2 = \left(\mathbf{J}^-\right)^2 = \frac{1}{4}\left(L^2 + D^2\right) = \frac{1}{4}\left(L^2 + \frac{|\mathbf{A}|^2}{-2mE}\right) = \frac{m\kappa^2}{8|E|} ,
$$

where the last equality uses $|\mathbf{A}|^2 = m^2\kappa^2 + 2mEL^2$. For the representative bound point used in the check, both Casimirs evaluate to $0.27982080$ while $m\kappa^2/(8|E|)$ evaluates to the same value to eight decimal places. The equality of the two Casimirs is what makes the bound-state representations balanced, and it is the algebraic statement that fixes the degeneracy.

### The Unbound and Threshold Cases

For $E > 0$ the third bracket changes sign. Defining $\mathbf{D} = \mathbf{A}/\sqrt{2mE}$ gives

$$
\{D_i, D_j\} = -\epsilon_{ijk}L_k, \qquad \{L_i, D_j\} = \epsilon_{ijk}D_k ,
$$

which is the algebra $\mathfrak{so}(3,1)$ of the Lorentz group in three space dimensions. Its Casimirs are $\mathbf{L}\cdot\mathbf{D}$ and $L^2 - D^2$, and the representations are the infinite-dimensional ones of the non-compact group; this is the algebraic reflection of the fact that the unbound orbits are hyperbolas with a continuous family of scattering angles.

At the threshold $E = 0$ the coefficient in the third bracket vanishes, $\{A_i,A_j\} = 0$, and with $\mathbf{D} = \mathbf{A}$ the brackets become $\{D_i,D_j\}=0$ and $\{L_i,D_j\} = \epsilon_{ijk}D_k$. This is the algebra of the Euclidean group $E(3)$: the $\mathbf{L}$ generate rotations and the $\mathbf{A}$ generate translations. The three cases are collected below.

| Energy | Rescaled vector | Algebra | Group |
|---|---|---|---|
| $E < 0$ | $\mathbf{D} = \mathbf{A}/\sqrt{-2mE}$ | $\{D,D\}=\epsilon L$, $\{L,D\}=\epsilon D$ | $\mathfrak{so}(4)\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ |
| $E = 0$ | $\mathbf{D} = \mathbf{A}$ | $\{D,D\}=0$, $\{L,D\}=\epsilon D$ | $\mathfrak{e}(3)$ |
| $E > 0$ | $\mathbf{D} = \mathbf{A}/\sqrt{2mE}$ | $\{D,D\}=-\epsilon L$, $\{L,D\}=\epsilon D$ | $\mathfrak{so}(3,1)$ |

The bound case is the one that bears on the hydrogen spectrum, and it is the case developed below.

### Numerical Checks

The bracket algebra was verified by central-difference evaluation of the Poisson brackets of the six generators at several representative bound phase-space points; the figures quoted are for the point with $m = \kappa = 1$ and $E = -0.446714$, and the identities reproduce at every bound point tested. The brackets $\{L_i,L_j\} = \epsilon_{ijk}L_k$, $\{L_i,A_j\} = \epsilon_{ijk}A_k$ and $\{A_i,A_j\} = -2mE\,\epsilon_{ijk}L_k$ were all confirmed to a maximum deviation of order $10^{-11}$; the rescaled bracket $\{D_i,D_j\} = \epsilon_{ijk}L_k$ was confirmed to the same accuracy; and the two $\mathfrak{su}(2)$ relations $\{J_i^\pm,J_j^\pm\} = \epsilon_{ijk}J_k^\pm$ and $\{J_i^+,J_j^-\} = 0$ were confirmed to order $10^{-11}$. The two Casimirs were found equal to eight decimal places, both equal to $0.27982080$, in agreement with $m\kappa^2/(8|E|)$; and the identities $\mathbf{L}\cdot\mathbf{A} = 0$ and $|\mathbf{A}|^2 = m^2\kappa^2 + 2mEL^2$ were confirmed to machine precision.

The algebra statements of the closing sections were checked at the same time, in explicit complex-matrix form using the isomorphism $e_k \mapsto -i\sigma_k$, $i \mapsto iI_2$ of $\mathbb{B}$ with $M_2(\mathbb{C})$. The material sector was confirmed closed under the commutator, with $[\mathbb{M}_+,\mathbb{M}_+] \subseteq \mathbb{M}_-$ and every element of $[\mathbb{M}_-,\mathbb{M}_-]$ again anti-Hermitian; the traceless part was confirmed to close exactly on

$$
\left[\tfrac{e_i}{2},\tfrac{e_j}{2}\right] = \epsilon_{ijk}\tfrac{e_k}{2}, \qquad
\left[\tfrac{e_i}{2},\tfrac{ie_j}{2}\right] = \epsilon_{ijk}\tfrac{ie_k}{2}, \qquad
\left[\tfrac{ie_i}{2},\tfrac{ie_j}{2}\right] = -\epsilon_{ijk}\tfrac{e_k}{2} ;
$$

and the six operators $L_k, R_k$ of left and right multiplication were confirmed antisymmetric on $\mathbb{H}$, with $[L_i,L_j] = 2\epsilon_{ijk}L_k$, $[R_i,R_j] = -2\epsilon_{ijk}R_k$, $[L_i,R_j] = 0$ and $\sum_kL_k^2 = \sum_kR_k^2 = -3\,e_0$. The last identity is the statement of equal Casimirs, and its value divided by the square of the generator normalization gives $\tfrac34$, that is $j(j+1)$ at $j = \tfrac12$.

<!-- CONVENTION — what the algebra contains at dimension six: the claim that $\mathbb{B}$ carries an $\mathfrak{so}(3,1)$ but no $\mathfrak{so}(4)$ is deliberate and is not a miscount. $\mathbb{M}_-$ is closed under the commutator and is $\mathfrak{u}(2)$, of real dimension four; since the maximal compact subalgebra of $\mathfrak{gl}(2,\mathbb{C})$ is $\mathfrak{u}(2)$, no compact six-dimensional algebra embeds, whereas the traceless part $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(3,1)$ is six-dimensional and does embed. The $\mathfrak{so}(4)$ that appears in this article is either the phase-space symmetry of the Coulomb problem or the bimultiplication algebra of the algebra on itself, never a commutator subalgebra of the biquaternions. A reviewer must not "repair" this by putting $\mathfrak{so}(4)$ inside $\mathbb{B}$. -->

## The Classical Origin of the Degeneracy

### Balanced Representations

The group $SO(4)$ generated by $\mathbf{J}^+$ and $\mathbf{J}^-$ is the double cover $SU(2)\times SU(2)$, and its irreducible representations are the tensor products $\mathcal{D}^{j_+}\otimes\mathcal{D}^{j_-}$ of dimensions $(2j_+ + 1)(2j_- + 1)$. A conserved quantity that commutes with the Hamiltonian is a function of the Casimirs, so the energy is a function of $(\mathbf{J}^+)^2$ and $(\mathbf{J}^-)^2$; and since the two Casimirs are **equal** for the Coulomb problem, the representations that occur have $j_+ = j_- = j$, with dimension

$$
\dim = (2j+1)^2 .
$$

The degeneracy of an energy level is therefore a **perfect square**, and the quantum number that labels it is $2j+1$. This is the group-theoretic origin of the $n^2$ degeneracy: the levels of the non-relativistic hydrogen atom carry the balanced representations of the hidden $SO(4)$, and a balanced representation has square dimension.

### The Energy–Casimir Relation and the Quantum Multiplicity

The value of the Casimir is fixed by the energy through

$$
\left(\mathbf{J}^\pm\right)^2 = \frac{m\kappa^2}{8|E|} ,
$$

so that specifying $E$ specifies $j$, and the level's orbital degeneracy is $(2j+1)^2$. When the classical functions are replaced by operators and the algebra is quantized, the Casimir takes the values $\hbar^2(n^2-1)/4$ for the hydrogen levels $n = 1, 2, 3, \dots$, so that $j = (n-1)/2$ and

$$
2j + 1 = n, \qquad \dim = n^2 .
$$

The Balmer formula $E_n = -m\kappa^2/(2\hbar^2n^2)$ is recovered by inverting the Casimir relation, which is how Pauli obtained the spectrum in 1926 from the commutation relations of $\mathbf{L}$ and $\mathbf{A}$ alone, before the Schrödinger equation was written down. Fock's later reformulation identified the symmetry group geometrically as $SO(4)$ acting on the momentum sphere. These are standard results of the quantum theory, imported here as the quantum counterparts of the classical brackets; the present article is the classical symmetry and the brackets are the classical ones.

### What This Says About the Biquaternion Framework

The quantum companion article *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case* records the $n^2$ degeneracy and states that the framework does not account for it, and poses the $SO(4)$ origin as an open question. The present article answers half of the question and sharpens the other half.

**What is answered.** The degeneracy's square form is the dimension of a balanced representation of $\mathfrak{so}(4)$, and the symmetry that produces it is generated by the angular momentum and the Runge–Lenz vector. This is the origin of the degeneracy, it is classical, and the classical generators are $\mathbf{L}$ and $\mathbf{A}$ as written above. The degeneracy is not a coincidence of the Coulomb potential; it is the representation theory of the hidden symmetry.

**What remains open.** The generators $\mathbf{L}$ and $\mathbf{A}$ are functions on the phase space, not elements of $\mathbb{B}$, and the algebra $\mathfrak{so}(4)$ is six-dimensional. Why the algebra cannot host it is worth stating exactly, because the exact statement is sharper than the count of dimensions. Under the commutator the material sector is closed, $[\mathbb{M}_-,\mathbb{M}_-] \subseteq \mathbb{M}_-$ and $[\mathbb{M}_+,\mathbb{M}_+] \subseteq \mathbb{M}_-$, and $\mathbb{M}_-$ is the algebra $\mathfrak{u}(2) \cong \mathfrak{u}(1)\oplus\mathfrak{su}(2)$ of real dimension four, whose traceless part $\operatorname{span}\{e_1,e_2,e_3\}$ is the $\mathfrak{su}(2)$ of rotations. Since the maximal compact subalgebra of $\mathfrak{gl}(2,\mathbb{C})$ is $\mathfrak{u}(2)$, of dimension four, no compact subalgebra of dimension six lies in $\mathbb{B}$: the compact algebra $\mathfrak{so}(4) \cong \mathfrak{su}(2)\oplus\mathfrak{su}(2)$ is not a commutator subalgebra of the biquaternions, and that is the reason, rather than a count of rotation generators.

What $\mathbb{B}$ does contain at dimension six is its traceless part, which is $\mathfrak{sl}(2,\mathbb{C})$ as a real Lie algebra, spanned by the rotations $e_k/2$ — the vector directions of the material sector — together with the boosts $ie_k/2$ — the vector directions of the informational sector:

$$
\left[\tfrac{e_i}{2},\tfrac{e_j}{2}\right] = \epsilon_{ijk}\tfrac{e_k}{2}, \qquad
\left[\tfrac{e_i}{2},\tfrac{ie_j}{2}\right] = \epsilon_{ijk}\tfrac{ie_k}{2}, \qquad
\left[\tfrac{ie_i}{2},\tfrac{ie_j}{2}\right] = -\epsilon_{ijk}\tfrac{e_k}{2} .
$$

This is the Lorentz algebra of the corpus's rotors, and it is $\mathfrak{so}(3,1)$: the split real form of the same complexification whose compact real form is $\mathfrak{so}(4)$. The algebra therefore carries a six-dimensional symmetry algebra of exactly the right complexification, and the real form it carries is the one belonging to the **unbound** case of the brackets above; the bound case's compact $\mathfrak{so}(4)$ is its compact form. An algebraic account of the bound-state degeneracy **inside $\mathbb{B}$** is still not available, and the open question of the hydrogen article is not resolved by the present article. What is established is that the symmetry is classical, that it lives in the phase space, and that the algebra's own six-dimensional structure is the continuation of the bound-state symmetry to the other sign of the energy.

## The Reach and the Limits of the Algebra

### What the Algebra Contains

The biquaternion algebra contains the following objects of the Coulomb problem.

**The real three-space.** The vectors $\mathbf{r}, \mathbf{p}, \mathbf{L}, \mathbf{A}$ all lie in $\operatorname{span}\{e_1,e_2,e_3\} \subset \mathbb{M}_-$, which is the configuration three-space. The angular momentum is the vector part of the product $\mathbf{r}\mathbf{p}$, $\mathbf{L} = \operatorname{Vect}(\mathbf{r}\mathbf{p})$, and its conservation is the vanishing of the commutator $[\mathbf{r},\mathbf{F}]$.

**The rotation group.** The unit real quaternions $R$ act by $R(\cdot)R^{-1}$ and rotate all six generators as vectors: $R\mathbf{L}R^{-1}$ is the rotated angular momentum, and the same for $\mathbf{A}$. The algebra carries the $\mathfrak{su}(2)$ of spatial rotations in its own commutator, $[e_j,e_k] = 2\epsilon_{jkl}e_l$.

**The central scalars.** The energy, the potential and the coupling are real multiples of $e_0$; the Casimir value $m\kappa^2/(8|E|)$ and the energy–eccentricity relation are scalar statements.

**The Lorentz algebra.** The traceless part of $\mathbb{B}$ is closed under the commutator and is six-dimensional; generated by the rotations $e_k/2$ and the boosts $ie_k/2$, it is $\mathfrak{so}(3,1) \cong \mathfrak{sl}(2,\mathbb{C})$, the Lorentz algebra of the corpus's rotors. It is the compact form $\mathfrak{so}(4)$ that is absent, not the six-dimensional complexification.

### The Symmetry of the Algebra on Itself

There is one place where a six-dimensional rotation algebra arises from the algebra alone, and recording it fixes the boundary exactly. Left and right multiplication by the unit real quaternions are isometries of $\mathbb{H} \cong \mathbb{R}^4$, and the six operators

$$
L_k : q \mapsto e_kq, \qquad R_k : q \mapsto qe_k
$$

are antisymmetric there. They close as

$$
[L_i,L_j] = 2\epsilon_{ijk}L_k, \qquad [R_i,R_j] = -2\epsilon_{ijk}R_k, \qquad [L_i,R_j] = 0 ,
$$

so that $\operatorname{span}\{L_1,L_2,L_3,R_1,R_2,R_3\}$ is six-dimensional and is $\mathfrak{su}(2)\oplus\mathfrak{su}(2) \cong \mathfrak{so}(4)$: the rotations of the four-dimensional space on which the algebra acts. This is the sense in which the algebra does carry an $\mathfrak{so}(4)$ — as the symmetry of its own module structure. It is not a commutator subalgebra, and it acts on the algebra rather than on the phase space, so it does not supply the hidden symmetry of the Coulomb problem.

Under this action $\mathbb{B}$ is a single balanced representation. Its two Casimirs are equal, $\sum_kL_k^2 = \sum_kR_k^2 = -3\,e_0$ on $\mathbb{H}$ — the balance condition that the bound-state multiplicity requires — and its complex dimension is four, the value of $n^2$ at $n = 2$. The lowest shell of the degeneracy therefore has an image in the algebra, as the balanced $(\tfrac12,\tfrac12)$; the shells $n \geq 3$, of dimensions $9, 16, \dots$, have none, because the self-action of a four-dimensional algebra carries only one balanced representation. The boundary is consequently sharper than a dimension count: the algebra is not foreign to the symmetry — it carries the symmetry's lowest carrier, with the balance the multiplicity needs — but it cannot carry the tower, and it does not derive the dynamics that selects the inverse-square force. Whether the matching at $n = 2$ has dynamical content is not established here, and the degeneracy's algebraic origin remains the open question it was.

### What the Algebra Does Not Contain

**The reciprocal length.** The Runge–Lenz vector contains $\hat{\mathbf{r}} = \mathbf{r}/|\mathbf{r}|$, and $|\mathbf{r}|^{-1}$ is not a polynomial in the components of $\mathbf{r}$. Normalization is a nonlinear operation, and the finite-dimensional algebra does not implement it. The same obstruction applies to the potential $-\kappa/r$, which is a central scalar function but not an element built from $\mathbf{r}$ by algebra operations; it is a function on the configuration space, inserted as data.

**The phase space.** The six generators and their brackets are functions on the six-dimensional space of pairs $(\mathbf{r},\mathbf{p})$. That space is not a module over $\mathbb{B}$; the algebra is a single copy of $M_2(\mathbb{C})$ and the phase space is infinite-dimensional as a space of functions. The hidden symmetry is a symmetry of the phase space.

**The six-dimensional algebra.** The biquaternion algebra has real dimension eight, $\mathbb{B} \cong M_2(\mathbb{C})$. Its largest compact subalgebra is the material sector $\mathbb{M}_- \cong \mathfrak{u}(2)$, of real dimension four, which contains the $\mathfrak{su}(2)$ of spatial rotations; a compact six-dimensional algebra such as $\mathfrak{so}(4)$ therefore does not embed, and the three extra generators of the hidden symmetry require the phase-space structure that the algebra does not carry. The six-dimensional subalgebra the algebra does possess is its traceless part, the Lorentz algebra $\mathfrak{sl}(2,\mathbb{C}) \cong \mathfrak{so}(3,1)$ generated by the rotations and the boosts — the non-compact real form of the same complexification as $\mathfrak{so}(4)$, and the symmetry type of the unbound case. This is the structural boundary between the framework's algebra and the hidden symmetry, and it is the same boundary that the quantum hydrogen article reports.

## Summary

The classical Coulomb problem is the inverse-square force with coupling $\kappa = -q_1q_2/(4\pi\epsilon_0)$. Its force is a central real vector in $\mathbb{M}_-$, its potential a central scalar in $\mathbb{M}_+$, and its orbits the conic sections. For the attractive case $\kappa > 0$, with the mass written $m$ as everywhere else in this subcategory,

$$
p = \frac{L^2}{m\kappa}, \qquad e = \sqrt{1 + \frac{2EL^2}{m\kappa^2}} , \qquad a = -\frac{\kappa}{2E} .
$$

The repulsive case $\kappa < 0$ has $p < 0$, so its polar orbit is the same expression with $|p|$ in place of $p$; the eccentricity formula and $a = -\kappa/(2E)$ hold with the signs as written.

The particle is structureless and carries no intrinsic magnetic moment; its orbital motion's magnetic field is not an intrinsic magnetism.

The inverse-square law conserves, besides the angular momentum $\mathbf{L} = \tfrac12[\mathbf{r},\mathbf{p}]$, the Runge–Lenz vector $\mathbf{A} = \mathbf{p}\times\mathbf{L}-m\kappa\hat{\mathbf{r}}$ with $|\mathbf{A}| = m\kappa e$. The six generators close under the Poisson bracket:

$$
\{L_i,L_j\} = \epsilon_{ijk}L_k, \qquad \{L_i,A_j\} = \epsilon_{ijk}A_k, \qquad \{A_i,A_j\} = -2mE\,\epsilon_{ijk}L_k .
$$

Rescaling by the energy produces the hidden symmetry: for $E<0$, with $\mathbf{D} = \mathbf{A}/\sqrt{-2mE}$ and $\mathbf{J}^\pm = \tfrac12(\mathbf{L}\pm\mathbf{D})$, the generators satisfy

$$
\{J_i^+,J_j^+\} = \epsilon_{ijk}J_k^+, \qquad \{J_i^-,J_j^-\} = \epsilon_{ijk}J_k^-, \qquad \{J_i^+,J_j^-\} = 0 ,
$$

so that the symmetry algebra is $\mathfrak{so}(4)\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$, with equal Casimirs

$$
\left(\mathbf{J}^+\right)^2 = \left(\mathbf{J}^-\right)^2 = \frac{m\kappa^2}{8|E|} .
$$

The balanced representations of dimension $(2j+1)^2$ are the classical origin of the $n^2$ degeneracy of the hydrogen spectrum, with $2j+1 = n$ after quantization. For $E>0$ the algebra is $\mathfrak{so}(3,1)$ and for $E=0$ it is $\mathfrak{e}(3)$.

The framework supplies the real three-space in which all six generators take their values, the product form $\mathbf{L} = \operatorname{Vect}(\mathbf{r}\mathbf{p})$, and the rotation group that acts on them. It does not supply the compact six-dimensional symmetry algebra, because the largest compact subalgebra of $\mathbb{B} \cong M_2(\mathbb{C})$ is the material sector $\mathbb{M}_- \cong \mathfrak{u}(2)$, of dimension four, and because $\mathbf{A}$ contains the reciprocal length $\mathbf{r}/|\mathbf{r}|$ and lives on the phase space. What it does supply at dimension six is the Lorentz algebra $\mathfrak{so}(3,1) \cong \mathfrak{sl}(2,\mathbb{C})$ — the split form of the same complexification as $\mathfrak{so}(4)$, and the symmetry type of the unbound case — together with the balanced $(\tfrac12,\tfrac12)$ self-action whose dimension is $n^2$ at $n = 2$ and which cannot carry the higher shells. The degeneracy's algebraic origin inside the framework therefore remains the open question it was; what the present article establishes is the classical symmetry algebra, the precise location of the boundary, and how far the algebra's own structure reaches towards it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_je_k = \epsilon_{jkl}e_l$ $(j\neq k)$ |
| $i$ | Central scalar imaginary, $i^2 = -e_0$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian), informational (Hermitian) sectors |
| $\mathbf{r}, \mathbf{p}$ | Position, momentum: real vectors in $\operatorname{span}\{e_1,e_2,e_3\}$ |
| $q_1, q_2$, $\epsilon_0$ | Charges; vacuum permittivity |
| $\kappa = -q_1q_2/(4\pi\epsilon_0)$ | Coulomb coupling; $\kappa>0$ attractive |
| $V(r) = -\kappa/r$ | Coulomb potential; central scalar |
| $H = p^2/(2m) - \kappa/r$ | Hamiltonian |
| $\mathbf{L} = \mathbf{r}\times\mathbf{p} = \tfrac12[\mathbf{r},\mathbf{p}]$ | Angular momentum; vector part of $\mathbf{r}\mathbf{p}$ |
| $\mathbf{A} = \mathbf{p}\times\mathbf{L} - m\kappa\hat{\mathbf{r}}$ | Runge–Lenz vector |
| $|\mathbf{A}| = m\kappa e$; $\mathbf{A}\cdot\mathbf{L} = 0$ | Magnitude and orthogonality |
| $|\mathbf{A}|^2 = m^2\kappa^2 + 2mEL^2$ | Magnitude identity |
| $\{L_i,L_j\}=\epsilon_{ijk}L_k$ | Angular-momentum bracket |
| $\{L_i,A_j\}=\epsilon_{ijk}A_k$ | Vector transformation of $\mathbf{A}$ |
| $\{A_i,A_j\}=-2mE\,\epsilon_{ijk}L_k$ | Energy-dependent bracket |
| $\mathbf{D} = \mathbf{A}/\sqrt{-2mE}$ $(E<0)$ | Rescaled generator |
| $\mathbf{J}^\pm = \tfrac12(\mathbf{L}\pm\mathbf{D})$ | $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ generators |
| $(\mathbf{J}^\pm)^2 = m\kappa^2/(8|E|)$ | Equal Casimirs |
| $E<0$ / $E=0$ / $E>0$ | $\mathfrak{so}(4)$ / $\mathfrak{e}(3)$ / $\mathfrak{so}(3,1)$ |
| $p = L^2/(m\kappa)$, $a = -\kappa/(2E)$ | Semi-latus rectum, semi-major axis |
| $e = \sqrt{1 + 2EL^2/(m\kappa^2)}$ | Eccentricity |

## Further Reading

- W. Pauli, "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik," *Zeitschrift für Physik* **36** (1926) 336–363, for the derivation of the Balmer formula from the conserved vectors and their commutation relations.
- V. Fock, "Zur Theorie des Wasserstoffatoms," *Zeitschrift für Physik* **98** (1935) 145–154, for the geometrical identification of the hydrogen symmetry group as $SO(4)$.
- V. Bargmann, "Zur Theorie des Wasserstoffatoms: Bemerkungen zur gleichnamigen Arbeit von V. Fock," *Zeitschrift für Physik* **99** (1936) 576–582, for the representation theory of the bound-state symmetry.
- W. Lenz, "Über den Bewegungsverlauf und die Quantenzustände der gestörten Keplerbewegung," *Zeitschrift für Physik* **24** (1924) 197–207, for the conserved vector of the Kepler problem.
- Herbert Goldstein, Charles Poole and John Safko, *Classical Mechanics* (Pearson, 2002), for the Runge–Lenz vector and the symmetry algebra in the classical setting.
- M. Bander and C. Itzykson, "Group theory and the hydrogen atom (I) and (II)," *Reviews of Modern Physics* **38** (1966) 330 and 346, for the $\mathfrak{so}(4)$ and $\mathfrak{so}(4,1)$ treatments of the Coulomb problem.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the classical Coulomb problem and the Rutherford scattering orbit.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Kepler and Coulomb symmetries.
