# __Paravectors and the Geometry of Spacetime__

## Introduction

The biquaternion algebra contains, as a subalgebra, the **algebra of physical space** — the real Clifford algebra $\mathrm{Cl}_{3,0}$. The corpus records this identification (*The Clifford Structure of the Biquaternion Algebra*: $\mathbb{B}\cong\mathrm{Cl}_{3,0}$ as real algebras), but it works throughout in the material sector $\mathbb{M}_-$, whose time coordinate is the imaginary $ict$. This article works instead in the **paravectors** of the algebra of physical space: the four-dimensional real space spanned by the scalar $e_0$ and the three positive-definite generators. That space is exactly the Hermitian subspace $\mathbb{M}_+$ of the corpus, and the material sector is its central-imaginary multiple, $\mathbb{M}_- = i\mathbb{M}_+$. A paravector is thus a spacetime vector written with a **real** time; the $i$ of the $ict$ convention is not removed but relocated, and the geometry becomes a geometry of physical space and its null elements.

The purpose of the article is threefold. First, it fixes the dictionary between the source's paravectors and the corpus's objects, so that results written in the algebra of physical space can be read in the series' conventions. Second, it states and proves the source's **boost rule**, $p\mapsto u\,p_\parallel + p_\perp$, the computational device that replaces the rotor sandwich by a single multiplication, and shows it to be exactly the rotor conjugation already used on the material sector. Third, it records the reading of **biparavectors** as spacetime planes, which is what makes the electromagnetic field a plane-valued object and which the field-strength article then uses.

The source is William E. Baylis, *Relativity in Introductory Physics*, Can. J. Phys. **82** (2004) 853–873 (arXiv:physics/0406158), and his *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), where the paravector formalism is developed. The article presents the paravector reading as a **presentation** of the corpus's own algebra, not as a different theory: the Lorentz group, the null cone, the field and its invariants are the same objects under a change of basis, and nothing below contradicts a result of the companion articles.

The conventions are those of the series. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and $i$ central with $i^2 = -1$. The Hermitian subspace is $\mathbb{M}_+ = \{q_0e_0 + i\mathbf q : q_0\in\mathbb{R}, \mathbf q\ \text{real}\}$ and the material subspace $\mathbb{M}_- = i\mathbb{M}_+$; the scalar imaginary is written $i$ where it is the central element of $\mathbb{B}$ and $\mathrm{i}$ nowhere else, so that no notational distinction is needed. The symbol $c$ is the speed of light in the medium, $c_0$ its vacuum value, and $\mathbf v$ is reserved for particle and frame velocities.

## The Algebra of Physical Space Inside the Biquaternions

Let $\gamma_k = i e_k$, $k = 1,2,3$. These three elements are real (they have vanishing imaginary part in the sense that they are fixed by complex conjugation) and satisfy

$$
\gamma_j\gamma_k + \gamma_k\gamma_j = 2\delta_{jk}\,e_0,
$$

because $\gamma_j\gamma_k = (ie_j)(ie_k) = i^2e_je_k = -e_je_k$ and the quaternion units anticommute for $j\neq k$ while $e_k^2 = -e_0$ gives $\gamma_k^2 = -e_k^2 = +e_0$. They therefore generate a three-dimensional positive-definite Clifford algebra. That algebra is all of $\mathbb{B}$, as the corpus records, and the four-dimensional real space

$$
\mathrm{APS} \;=\; \mathrm{span}_\mathbb{R}\{e_0, \gamma_1, \gamma_2, \gamma_3\} \;=\; \left\{p_0e_0 + p_1\gamma_1 + p_2\gamma_2 + p_3\gamma_3 \;:\; p_\mu \in \mathbb{R}\right\}
$$

is its **paravector space**. Comparing with the definition of the Hermitian subspace,

$$
\mathbb{M}_+ = \left\{q_0e_0 + i\mathbf q\right\}, \qquad \mathbf q = q_1e_1 + q_2e_2 + q_3e_3,
$$

shows that the paravector space is exactly $\mathbb{M}_+$: the identification is $\gamma_k \leftrightarrow ie_k$, so $p_0e_0 + \sum p_k\gamma_k = p_0e_0 + i\sum p_k e_k$. The two readings of the same element are

| | scalar | vector |
|---|---|---|
| corpus basis | $p_0 e_0$ | $i(p_1e_1 + p_2e_2 + p_3e_3)$ |
| paravector basis | $p_0 e_0$ | $p_1\gamma_1 + p_2\gamma_2 + p_3\gamma_3$ |

**The conjugations.** On paravectors the quaternion conjugate ${}^{\natural}$ negates the vector part and leaves the scalar part alone, since $\bar{\gamma}_k = \overline{ie_k} = i\bar{e}_k = -ie_k = -\gamma_k$. This is precisely the **Clifford conjugate** of the algebra of physical space, $p \mapsto \bar p = p_0 - \mathbf p$. Because $\mathbb{M}_+$ is the fixed space of the Hermitian conjugation, $\bar p = p^\dagger$ for a paravector; the reversion, whose action on the paravector generators is the identity, coincides with the Hermitian conjugation on $\mathbb{M}_+$ and is the operation the source writes with a dagger.

**The form.** The biquaternion norm of a paravector is real and reads

$$
p\,\bar p = \left(p_0 + \mathbf p\right)\left(p_0 - \mathbf p\right) = p_0^2 - \mathbf p^2 = p_0^2 - p_1^2 - p_2^2 - p_3^2,
$$

using $\mathbf p^2 = p_1^2 + p_2^2 + p_3^2$ for a real three-vector. This is the Minkowski form of signature $(1,3)$, the form of the informational sector $\mathbb{M}_+$ in the corpus's notation. The material sector carries the same form with the opposite sign: for $\tilde Q = ip \in \mathbb{M}_-$,

$$
N(\tilde Q) = (ip)\overline{(ip)} = i^2\,p\bar p = -p\bar p,
$$

so a paravector is timelike, lightlike or spacelike exactly when the corresponding material element is, with the sign of the interval reversed in the two conventions. The null cone is the same set in both readings.

**The dictionary in one line.** Under the identification $\gamma_k = ie_k$, the algebra of physical space is the Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra, the Clifford conjugate is the quaternion conjugate, the reversion is the Hermitian conjugation, and the Minkowski interval of a paravector is the negative of the corpus norm of its central-imaginary multiple. The material four-vectors are $\tilde Q = ip$ with $p$ a paravector; in coordinates, $\tilde Q = ict\,e_0 + \mathbf x$ corresponds to the paravector $p = ct\,e_0 - \mathbf x$ in the paravector basis, the spatial sign being the convention that $\gamma_k = ie_k$ fixes.

## The Paravector as a Spacetime Vector

A paravector $p = p_0+\mathbf p$ has a real scalar $p_0$ and a real three-vector $\mathbf p$, and it represents the spacetime vector with time component $p_0$ and space components $\mathbf p$. The corpus writes the same vector as a material element with imaginary time; the two are related by the central $i$ and carry the same information. The practical difference is that the paravector's time is real, so that "spacetime" is a real four-dimensional space with one timelike direction and the geometry of light rays is a geometry of a Euclidean three-space with a null cone.

The **invariant interval** between two events is the squared modulus $p\bar p$, and the **proper time** along a worldline is the modulus of the displacement. These are the corpus's interval statements in the paravector reading; no new physics is introduced.

**Proper velocity.** For a particle of velocity $\mathbf v$, with $\beta = |\mathbf v|/c$ and $\gamma = (1-\beta^2)^{-1/2}$, the **proper velocity** is the unimodular paravector

$$
u = \gamma\left(e_0 + \beta\hat{\mathbf v}\right),
\qquad
u\,\bar u = \gamma^2\left(e_0 + \beta\hat{\mathbf v}\right)\left(e_0 - \beta\hat{\mathbf v}\right)
= \gamma^2\left(1 - \beta^2\right)e_0 = e_0 .
$$

The unimodularity is the paravector form of the constant length of the four-velocity. The corpus's four-velocity is $\tilde U = \gamma(ic\,e_0 + \mathbf v)\in\mathbb{M}_-$, and the two are related by

$$
\tilde U = ic\,\bar u,
\qquad\text{equivalently}\qquad
u = -\frac{i}{c}\,\tilde U^{\natural},
$$

which is the corpus's relation $\tilde\Lambda^2 = -\frac{i}{c}\tilde U^{\natural}$ of *The Lorentz Transformation as a Biquaternionic Rotation* written for $u = \tilde\Lambda^2$. The paravector $u$ is Hermitian and its time component is real; the four-velocity $\tilde U$ is anti-Hermitian and its time component is imaginary. The two are not related by the central $i$ alone — that would reverse the spatial sign — but by $i$ followed by the quaternion conjugate, which is what the change of time convention does.

**The boost rotor is a paravector.** The corpus's boost rotor is $\tilde\Lambda = \cosh\frac{w}{2} + i\sinh\frac{w}{2}\hat{\mathbf u}$ with $\hat{\mathbf u}$ a unit real vector; in the paravector basis it is

$$
L = \cosh\frac{w}{2} + \sinh\frac{w}{2}\cdot i\hat{\mathbf u} = \cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf v},
$$

with $\hat{\mathbf v} = i\hat{\mathbf u}$, a unit paravector-vector since $(i\hat{\mathbf u})^2 = -i^2\hat{\mathbf u}\hat{\mathbf u} = -\hat{\mathbf u}\hat{\mathbf u} = e_0$. The rotor is thus a **paravector** — a scalar plus a vector — and its square is the proper velocity,

$$
L^2 = \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf v}\right)^2
= \cosh^2\frac{w}{2} + \sinh^2\frac{w}{2} + 2\cosh\frac{w}{2}\sinh\frac{w}{2}\hat{\mathbf v}
= \cosh w\,e_0 + \sinh w\,\hat{\mathbf v} \;=\; u,
$$

using $\hat{\mathbf v}^2 = e_0$. This is the corpus's relation $u = \tilde\Lambda^2 = -\frac{i}{c}\tilde U^{\natural}$ read in the paravector basis: the square of the boost rotor is the **proper velocity** $u$, a paravector, and the four-velocity $\tilde U$ is its companion under the change of time convention. The relation $u\bar u = e_0$ is the statement that the four-velocity has fixed length.

## The Boost Rule

The computational advantage of the paravector reading is that the Lorentz boost of a spacetime vector is a *product* rather than a sandwich with two factors.

**Theorem (boost rule).** Let $L = \cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf v}$ be a boost rotor, with $\hat{\mathbf v}$ a unit paravector-vector and $u = L^2$ the corresponding proper velocity. For any paravector $p = p_0 + \mathbf p$, write

$$
p_\parallel \;=\; p_0 + \left(\mathbf p\cdot\hat{\mathbf v}\right)\hat{\mathbf v},
\qquad
p_\perp \;=\; \mathbf p - \left(\mathbf p\cdot\hat{\mathbf v}\right)\hat{\mathbf v},
$$

for the components coplanar with the boost and orthogonal to it. Then the rotor conjugation gives

$$
L\,p\,L^\dagger \;=\; u\,p_\parallel + p_\perp .
$$

**Proof.** The two components transform separately. First, $p_\perp$ anticommutes with $\hat{\mathbf v}$, because two orthogonal paravector-vectors anticommute: $\hat{\mathbf v}p_\perp = -p_\perp\hat{\mathbf v}$. Hence

$$
L\,p_\perp\,L^\dagger
= \left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf v}\right)p_\perp\left(\cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf v}\right)
= \left(\cosh^2\frac{w}{2} - \sinh^2\frac{w}{2}\right)p_\perp = p_\perp,
$$

the reversion being the identity on the rotor, and the cross terms cancelling. Second, $p_\parallel$ commutes with $\hat{\mathbf v}$, because it is a scalar plus a multiple of $\hat{\mathbf v}$; hence it commutes with $L$, and

$$
L\,p_\parallel\,L^\dagger = L\,p_\parallel\,L = L^2\,p_\parallel = u\,p_\parallel .
$$

Adding the two gives the rule.

The corresponding statement in the series' conventions is the rotor conjugation on the Hermitian subspace. Writing $p$ for the Hermitian element $p_0e_0 + i\mathbf p_e$ and $\tilde\Lambda$ for the corpus boost rotor, the two are the same element ($L = \tilde\Lambda$) and the same operation ($L\,p\,L^\dagger = \tilde\Lambda\,p\,\tilde\Lambda^{*}$, the reversion being the identity on $\mathbb{M}_+$), so that

$$
\tilde\Lambda\,\tilde{Q}\,\tilde\Lambda^{*} = u\,p_\parallel + p_\perp,
\qquad \tilde{Q} = p = p_0e_0 + i\mathbf p_e ,
$$

with $u = \tilde\Lambda^2$. The rule is therefore not a new transformation law but the corpus's own law, written without the second factor.

**Why the rule is useful.** The rule multiplies only the part of $p$ coplanar with the boost plane and leaves the orthogonal part fixed. Unlike the sandwich it requires only a product with the proper velocity, and unlike a matrix it needs no basis in which the boost is aligned. The source uses it for the standard kinematical statements — the composition of velocities, the contraction of a moving rod, the relativity of simultaneity, the transformation of the electromagnetic field — and each becomes a one-line computation in the algebra.

## Composite Systems: Biparavectors and the Six Planes

A **biparavector** is the product of two orthogonal paravectors; it represents a **plane in spacetime**, in the same way that a bivector of the algebra of physical space represents a plane in physical space. Because spacetime is four-dimensional, there are $\binom{4}{2} = 6$ independent planes, and a basis of the biparavector space is

$$
\left\{e_0\gamma_1,\ e_0\gamma_2,\ e_0\gamma_3,\ \gamma_2\gamma_1,\ \gamma_3\gamma_2,\ \gamma_1\gamma_3\right\}
= \left\{\gamma_1,\ \gamma_2,\ \gamma_3,\ -e_2e_1,\ -e_3e_2,\ -e_1e_3\right\},
$$

the last three using $\gamma_j\gamma_k = -e_je_k$. The first three planes contain the time direction: they are the **timelike** (or boost) planes, and in the corpus basis they are the imaginary vectors $i e_k$ of $\mathbb{M}_+$. The last three are the **spacelike** (or rotation) planes, and they are the real quaternion bivectors $e_je_k$ of $\mathbb{H}_{\mathbb{B}}$. A general biparavector is a sum of one plane of each type, and its two parts are the two generators of the Lorentz group: the timelike planes generate the boosts and the spacelike planes the rotations (*Biquaternion Lie Algebra*, *The Lorentz Group in Biquaternionic Form*). The corpus's statement that boosts have rotors in $\mathbb{M}_+$ and rotations in $\mathbb{H}_{\mathbb{B}}$ is the statement that the two families of planes live in the two halves of $\mathbb{B} = \mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$, read through the paravector identification.

The pay-off of the biparavector reading is that the electromagnetic field strength is one of these objects. Baylis writes it as $F = \mathbf E + ic\mathbf B$, a sum of a spacelike and a timelike plane, and the corpus's pure-vector field strength $\tilde F = i\sqrt{\epsilon}\,\mathbf E - \sqrt{\mu}\,\mathbf H$ is the same object up to the normalization and the placement of the central $i$. The plane reading of the field — which plane is the electric field, which is the magnetic, and how the two sit in the two halves of the algebra — is set out in *The Field-Strength Biquaternion and Its Invariants*, where it is used to explain the asymmetric position of the electric and magnetic parts.

## The Multiparavector Grading and the Compactness of the Algebra

Baylis names every graded subspace of $\mathrm{Cl}_{3,0}$ after the spacetime object it carries, and the names make the compactness of the algebra visible. With the scalar unit $e_0$, the three vectors $\gamma_k = ie_k$ (so that $\gamma_j\gamma_k+\gamma_k\gamma_j = 2\delta_{jk}e_0$) and the central volume element $i = \gamma_1\gamma_2\gamma_3$, a **multiparavector** is a graded element, and the four grades group into five spacetime objects:

| object | grades | basis | real dim | spacetime reading |
|---|---|---|---|---|
| scalar | $0$ | $e_0$ | $1$ | Lorentz scalar |
| vector | $1$ | $\gamma_k$ | $3$ | spatial vector (a relative notion) |
| **paravector** | $0+1$ | $e_0,\ \gamma_k$ | $4$ | spacetime vector |
| **biparavector** | $1+2$ | $\gamma_k,\ \gamma_j\gamma_k$ | $6$ | spacetime plane: a boost or a rotation |
| **triparavector** | $2+3$ | $\gamma_j\gamma_k,\ i\gamma_k$ | $4$ | the dual of a spacetime vector |
| pseudoscalar | $3$ | $i$ | $1$ | Lorentz pseudoscalar |

The table is the whole content of the statement that the algebra of physical space is **compact**: its eight real dimensions carry the physics that spacetime algebra carries in sixteen, because each grade plays a double role. The scalar part of a multiparavector is one number serving both a Lorentz scalar and the time component of a spacetime vector; the vector part is three numbers serving both the space part of a spacetime vector and the timelike half of a spacetime plane. In the sixteen-dimensional spacetime algebra the same objects are separated by the chirality of the grade — a spacetime vector is a single grade-one element, a spacetime plane a single grade-two element — and the representation theory of the Lorentz group is consequently twice as wide. The algebra of physical space is not a truncation of spacetime algebra but the same content in a basis in which two of the sixteen components of a multivector are identified by the central $i$; the process is the one the spacetime-algebra article examines under *The Even Subalgebra as a Clifford Algebra* and *The Clifford-Odd $\gamma_0$ and the Right Action*. The compactness is what makes the corpus's single pure-vector field strength carry both invariants, and what makes its single $\mathbb{M}_-$ four-vector carry both the coordinate and the four-momentum.

**A caution about the wedge.** The symbol $\wedge$ carries two meanings in this literature and they must not be conflated. In the algebra of physical space, $\tilde P\wedge\tilde Q = \tfrac12(\tilde P\tilde Q - \tilde Q\tilde P)$ is the **commutator**, with values in the bivector (plane) part; in the exterior algebra of a four-dimensional vector space it is the **antisymmetric product**, a bivector of $\Lambda^2\mathbb{C}^4$, a six-component object. On three-dimensional *vectors* the two agree once a bivector is identified with an axial vector, which is why the cross product reading usually works; on general multiparavectors they do not agree as objects, although their components agree as a matter of degree count. Baylis records the caution explicitly: an identity proved for the three-dimensional wedge of vectors holds for the four-dimensional wedge only after the appropriate translation, and treating the two as the same symbol without it is a common source of error. The corpus uses $\wedge$ in the first sense throughout and reserves the exterior product of the spacetime algebra for the articles that need it; the bridge between the two is the identification of a decomposable bivector with the two-plane its factors span.

## Velocity Composition

The proper velocity is the natural variable of the composition law. If a frame $B$ moves with proper velocity $u_{BA}$ relative to $A$ and a frame $C$ moves with proper velocity $u_{CB}$ relative to $B$, then the proper velocity of $C$ relative to $A$ is the **product**

$$
u_{CA} \;=\; u_{CB}\,u_{BA},
$$

an equation that follows from the composition of the rotor conjugations, or directly from the associativity of the algebra of physical space. Writing each factor as $\gamma(e_0+\beta\hat{\mathbf v})$ and multiplying, the scalar part gives the composition of the Lorentz factors and the vector part the composition of the velocities. For collinear velocities the vector parts are parallel and the product is the familiar addition law

$$
\beta = \frac{\beta_1 + \beta_2}{1+\beta_1\beta_2},
\qquad
\gamma = \gamma_1\gamma_2\left(1+\beta_1\beta_2\right),
$$

while for non-collinear velocities the vector part acquires the extra term that is the **Wigner (Thomas) rotation**, the algebraic reason the composition of two boosts is not a boost. The corpus develops the hyperbolic-geometry reading of the same law, with the rapidity as the geodesic distance and the Wigner rotation as the curvature, in *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* and *Exercise: Boosting a Four-Velocity and Rapidity Composition*, and treats the rotation itself in *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form*; the product form is the one-line statement of the same content, and it is recorded here to fix the dictionary.

## What the Paravector Reading Adds, and What It Does Not

**It adds three things.** A **real time**: the geometry is posed on a four-dimensional real space with an indefinite form, and the null cone is a cone in that space rather than the image of one under multiplication by $i$. A **computational rule**: the boost is a product with the proper velocity, $p\mapsto up_\parallel+p_\perp$, which is one multiplication instead of a conjugation, and a plane-geometric bookkeeping in which a boost is the multiplication by a function of the timelike plane and a rotation by a function of the spacelike plane. And a **plane-valued field**: the field strength is a biparavector, a sum of two planes, which is the algebraic reason the electric and magnetic parts are not on the same footing.

**It does not add a different theory.** The paravector space is the Hermitian subspace $\mathbb{M}_+$ of the corpus, the Clifford conjugate is the quaternion conjugate, the reversion is the Hermitian conjugation, and the Lorentz group is the same group of unit-norm biquaternions. Every external result written in the algebra of physical space is a result of the corpus in a different basis, and the dictionary above is the whole of the translation. In particular the corpus's choice of the material sector, with its $ict$ and its real vectors, is the choice to write the *anti-Hermitian* reading of the same four-vector; the paravector reading writes the *Hermitian* one, and the two are exchanged by the central $i$.

The one genuinely new object in the source's programme is not a change of basis at all: the **electromagnetic plane wave as a rotation and a dilation**, which is an identity of the null cone and is treated in its own article (*The Boost of a Plane Wave as a Rotation and a Dilation*). The paravector reading is what makes that identity one line of algebra.

## Summary

The algebra of physical space, $\mathrm{Cl}_{3,0}$, is the Hermitian subspace $\mathbb{M}_+$ of the biquaternion algebra under the identification $\gamma_k = ie_k$; its paravector space is the four-dimensional real space $\{p_0e_0 + \mathbf p\}$, its Clifford conjugate is the quaternion conjugate, its reversion the Hermitian conjugation, and its Minkowski form $p\bar p = p_0^2 - \mathbf p^2$ is the negative of the corpus norm of $ip$. The proper velocity $u = \gamma(e_0+\beta\hat{\mathbf v})$ is unimodular and equals the square of the boost rotor $L = \cosh\frac{w}{2}+\sinh\frac{w}{2}\hat{\mathbf v}$. The boost of a paravector is the **rule** $p\mapsto up_\parallel+p_\perp$, which fixes the component orthogonal to the boost plane and multiplies the coplanar component by the proper velocity; in the series' conventions this is exactly the rotor conjugation of the Hermitian subspace. Biparavectors are spacetime planes, six in all, three timelike and generating boosts and three spacelike and generating rotations, and the field strength is a biparavector. The paravector reading is a presentation of the corpus's own algebra with a real time and a product rule for the boost; it introduces no new physics, and the one new identity of the source's programme is the boost of a plane wave.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$, $e_0 = 1, e_k$ | Biquaternion algebra, quaternion basis with $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$, central |
| $\gamma_k = i e_k$ | Generators of the algebra of physical space, $\gamma_j\gamma_k + \gamma_k\gamma_j = 2\delta_{jk}e_0$ |
| $\mathrm{APS} = \mathrm{span}\{e_0,\gamma_k\} = \mathbb{M}_+$ | Paravector space |
| $p = p_0 + \mathbf p$ | Paravector (spacetime vector), $p_0,\mathbf p$ real |
| $\bar p = p_0 - \mathbf p$ | Clifford conjugate $=$ quaternion conjugate $=$ Hermitian conjugate on $\mathbb{M}_+$ |
| $p\bar p = p_0^2 - \mathbf p^2$ | Minkowski interval |
| $\tilde Q = ip \in \mathbb{M}_-$ | The same vector in the corpus's material sector; $N(\tilde Q) = -p\bar p$ |
| $\hat{\mathbf v}$ | Unit paravector-vector, $\hat{\mathbf v}^2 = e_0$ |
| $L = \cosh\frac{w}{2} + \sinh\frac{w}{2}\hat{\mathbf v}$ | Boost rotor (a paravector); equals the corpus rotor $\cosh\frac{w}{2}+i\sinh\frac{w}{2}\hat{\mathbf u}$ |
| $u = L^2 = \cosh w + \sinh w\,\hat{\mathbf v}$ | Proper velocity, unimodular |
| $p_\parallel$, $p_\perp$ | Coplanar and orthogonal components of $p$ relative to the boost plane |
| $p\mapsto up_\parallel+p_\perp$ | The boost rule |
| Biparavector | Product of two orthogonal paravectors; a spacetime plane |
| $\{e_0\gamma_k,\ \gamma_j\gamma_k\}$ | The six independent planes: three timelike, three spacelike |
| $u_{CA} = u_{CB}u_{BA}$ | Composition of proper velocities |

## Further Reading

- William E. Baylis, "Relativity in Introductory Physics", *Canadian Journal of Physics* **82** (2004) 853–873 (arXiv:physics/0406158), for the paravector formalism, the boost rule and the plane-wave identity.
- William E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the full development of the algebra of physical space.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$ and the paravector calculus.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of boosts, rotors and the Lorentz group.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra comparison, in which the paravectors of $\mathrm{Cl}_{3,0}$ are the even elements of $\mathrm{Cl}_{1,3}$.
