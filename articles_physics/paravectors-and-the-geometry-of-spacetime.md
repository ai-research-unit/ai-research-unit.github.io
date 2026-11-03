# __Paravectors and the Geometry of Spacetime__

## Introduction

The biquaternion algebra is, as a real algebra, the **algebra of physical space** — the real Clifford algebra $\mathrm{Cl}_{3,0}$. The corpus records this identification (*The Number Systems as Clifford Algebras*: $\mathbb{B}\cong\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$), but it works throughout in the material sector $\mathbb{M}_-$, whose time coordinate is the imaginary $ict'$. This article works instead in the **paravectors** of the algebra of physical space: the four-dimensional real space spanned by the scalar $e_t$ and the three positive-definite generators. That space is exactly the Hermitian subspace $\mathbb{M}_+$ of the corpus, and the material sector is its central-imaginary multiple, $\mathbb{M}_-=i\mathbb{M}_+$. A paravector is thus a spacetime vector written with a **real** time; the $i$ of the $ict'$ convention is not removed but relocated, and the geometry becomes a geometry of physical space and its null elements.

The purpose of the article is threefold. First, it fixes the dictionary between the source's paravectors and the corpus's objects, so that results written in the algebra of physical space can be read in the series' conventions. Second, it states and proves the source's **boost rule**, $p\mapsto\tilde V_{\mathrm p}p_\parallel+p_\perp$, the computational device that replaces the rotor sandwich by a single multiplication, and shows it to be exactly the rotor congruence already used on the material sector. Third, it records the interpretation of **biparavectors** as spacetime planes, which is what makes the electromagnetic field a plane-valued object and which the field-strength article then uses.

The source is William E. Baylis, *Relativity in Introductory Physics*, Can. J. Phys. **82** (2004) 853–873 (arXiv:physics/0406158), and his *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), where the paravector formalism is developed. The article presents the paravector interpretation as a **presentation** of the corpus's own algebra, not as a different theory: the Lorentz group, the null cone, the field and its invariants are the same objects under a change of basis, and nothing below contradicts a result of the companion articles.

**Notation, once.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with $e_t=1,\vec e_x,\vec e_y,\vec e_z$, the cyclic products $\vec e_x\vec e_y=\vec e_z$ and its cyclic images, and $i$ central with $i^2=-1$. A **paravector** is

$$
p=p_te_t+i\vec p,\qquad \vec p=p_x\vec e_x+p_y\vec e_y+p_z\vec e_z ,
$$

with $p_t,p_x,p_y,p_z\in\mathbb{R}$. Its **vector part** is the imaginary vector $i\vec p$, whose algebra square is

$$
(i\vec p)(i\vec p)=i^2\,\vec p\,\vec p=+\left(\vec p\cdot\vec p\right)e_t ,
$$

because $\vec e_k^2=-e_t$ gives the algebra product $\vec p\,\vec p=-(\vec p\cdot\vec p)e_t$ and the two factors of $i$ undo that sign. Three squares are in play and they must not be confused: the **Euclidean square** $\vec p\cdot\vec p=p_x^2+p_y^2+p_z^2$ is a number and is positive definite; the **algebra square** $\vec p\,\vec p=-(\vec p\cdot\vec p)e_t$ is an element and is negative definite, because $\vec e_k^2=-e_t$; and the square of the **vector part**, $(i\vec p)(i\vec p)=+(\vec p\cdot\vec p)e_t$, is the third, positive again. The article writes $\vec p\cdot\vec p$ when a number is meant and $i\vec p$ when an element is meant. The letter $p$ is the source's and is reserved here for paravectors of $\mathcal{P}$; the corpus's canonical momentum is the tilded $\tilde p$, and its position four-vector is $\tilde R$. The symbol $c$ is the speed of light in the medium, $\vec v$ is the particle velocity, $\vec u_v=\vec v/v$ and $\vec u_{\mathrm b}$ the unit directions of the velocity and of the boost, and $\psi$ the rapidity.

## The Algebra of Physical Space Inside the Biquaternions

The three imaginary vectors $i\vec e_k$, $k=x,y,z$, satisfy

$$
(i\vec e_j)(i\vec e_k)+(i\vec e_k)(i\vec e_j)=2\delta_{jk}\,e_t ,
$$

because $(i\vec e_j)(i\vec e_k)=i^2\vec e_j\vec e_k=-\vec e_j\vec e_k$, the quaternion units anticommute for $j\neq k$, and $\vec e_k^2=-e_t$ gives $(i\vec e_k)^2=+e_t$. They therefore generate a three-dimensional positive-definite Clifford algebra, and that algebra is all of $\mathbb{B}$, as the corpus records. The **paravector space** is the real span of the scalar unit and the three positive-definite generators,

$$
\mathcal{P}=\operatorname{span}_\mathbb{R}\{e_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z\}
=\left\{p_te_t+i\vec p\;:\;p_t\in\mathbb{R},\ \vec p\in\mathbb{R}^3\right\},
$$

and it is the Hermitian subspace $\mathbb{M}_+=\{\tilde Q : \tilde Q^{*}=\tilde Q\}$ of the corpus, with $p_te_t+i\vec p$ written in either reading. The two interpretations are one decomposition, the scalar part $p_te_t$ and the vector part $i\vec p$: the corpus reads them as the Hermitian half of $\mathbb{B}$ and the source as the time and space components of a spacetime vector.

**The conjugations.** The quaternion conjugation ${}^{\natural}$ is the anti-automorphism fixed on $e_t$ and $i$ and negating the three vector units, $(ab)^{\natural}=b^{\natural}a^{\natural}$. On the generators of $\mathrm{Cl}_{3,0}$ it acts as

$$
(i\vec e_k)^{\natural}=-i\vec e_k,
\qquad
(\vec e_x\vec e_y)^{\natural}=\vec e_y^{\natural}\vec e_x^{\natural}=\vec e_y\vec e_x=-\vec e_x\vec e_y,
\qquad
i^{\natural}=i .
$$

Grade one and grade two are negated; grade zero and the volume element $i=(i\vec e_x)(i\vec e_y)(i\vec e_z)$ are fixed. That is exactly the **Clifford conjugate** of $\mathrm{Cl}_{3,0}$: it is the grade-reversing conjugation composed with the grade involution, so it negates grades one and two while fixing grades zero and three. The source writes this operation with an overbar, $\bar p$; this article writes ${}^{\natural}$, so that the overbar keeps its corpus sense of complex conjugation.

The **Hermitian conjugation** is the complex conjugation followed by the quaternion one, ${}^{*}=\overline{\cdot^{\natural}}$. On the same generators it acts as

$$
(i\vec e_k)^{*}=\overline{(i\vec e_k)^{\natural}}=\overline{-i\vec e_k}=+i\vec e_k ,
\qquad
(\vec e_x\vec e_y)^{*}=-\vec e_x\vec e_y ,
\qquad
i^{*}=-i .
$$

Grades zero and one are fixed, grades two and three are negated: in the Clifford vocabulary this is the **reversal**, the grade-reversing anti-automorphism, and it is the corpus's **Hermitian conjugation** ${}^{*}$. The corpus keeps the word *reversal* for the fourth involution $\flat=-{}^{*}$, so this article names ${}^{*}$ the star and never the reversal alone. On $\mathcal{P}$ the star is the identity, $p^{*}=p$, because grade one is fixed; that is the defining property of $\mathbb{M}_+$, not a coincidence.

The two conjugations must not be interchanged. They agree on the real scalars and on nothing else: on $i$ they already differ, $i^{\natural}=i$ and $i^{*}=-i$, and on the vector part of a paravector ${}^{\natural}$ negates while ${}^{*}$ fixes. The one that acts on a paravector is ${}^{\natural}$, and it is the source's Clifford conjugate; the one that appears in the boost below is ${}^{*}$, and it appears only because the boost rotor is fixed by it, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$.

**The form.** The quaternionic norm of a paravector is real,

$$
p\,p^{\natural}=(p_te_t+i\vec p)(p_te_t-i\vec p)=p_t^2e_t-(i\vec p)^2=\left(p_t^2-\vec p\cdot\vec p\right)e_t ,
$$

and its scalar coefficient is the corpus's **quaternionic norm**,

$$
\langle p\rangle_{\natural}=p_t^2-\vec p\cdot\vec p,\qquad\text{so that}\qquad p\,p^{\natural}=\langle p\rangle_{\natural}\,e_t .
$$

The norm is a number and the product is the number times $e_t$; the article keeps that distinction throughout. On a paravector the norm is real, and it is the Minkowski form of signature $(+,-,-,-)$ of the informational sector $\mathbb{M}_+$. The material sector carries the same form with the opposite overall sign: for $\tilde Q=ip\in\mathbb{M}_-$,

$$
\langle\tilde Q\rangle_{\natural}=\langle i\,p\rangle_{\natural}=i^2\langle p\rangle_{\natural}=-\left(p_t^2-\vec p\cdot\vec p\right),
$$

because the norm is multiplicative and $i$ is fixed by ${}^{\natural}$. The corpus's metric is the $ict'$ metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$, which is $-(+,-,-,-)$. A paravector is therefore timelike, lightlike or spacelike exactly when the corresponding material element is, the two conventions differing by the sign of the interval and by nothing else. The null cone is the same set in both readings, and the corpus's four-velocity normalisation $\langle\tilde V\rangle_{\natural}=-c^2$ is the material face of the paravector normalisation $\langle\tilde V_{\mathrm p}\rangle_{\natural}=1$ derived below.

**The dictionary.** The two readings name the same eight dimensions, one row to an object:

| paravector reading | corpus object | corpus notation |
|---|---|---|
| scalar unit $1$ | time unit | $e_t$ |
| vector $e_k$, $e_k^2=+e_t$ | imaginary vector | $i\vec e_k$ |
| paravector $p_t+p_xe_x+p_ye_y+p_ze_z$ | Hermitian element | $p_te_t+i\vec p$ |
| material four-vector $ct'+\vec x$ | element of $\mathbb{M}_-$ | $i\,p^{\natural}$ |
| Clifford conjugate $\bar p$ | quaternion conjugate | $p^{\natural}$ |
| Clifford reversal $p^\dagger$ | Hermitian conjugate ${}^{*}$, the identity on $\mathbb{M}_+$ | $p^{*}=p$ |
| volume element $e_1e_2e_3$ | central imaginary | $i$ |
| interval $p\bar p$ | quaternionic norm of the material element, sign reversed | $\langle i\,p^{\natural}\rangle_{\natural}=-(p_t^2-\vec p\cdot\vec p)$ |

The material four-vectors are $\tilde R=i\,p^{\natural}$ with $p$ a paravector. In coordinates, $\tilde R=ict'e_t+x\vec e_x+y\vec e_y+z\vec e_z$ corresponds to

$$
p=ct'e_t+i\left(x\vec e_x+y\vec e_y+z\vec e_z\right),
\qquad\text{so that}\qquad
i\,p^{\natural}=ict'e_t+x\vec e_x+y\vec e_y+z\vec e_z .
$$

That is $p_t=ct'$ and $\vec p=(x,y,z)$: the two readings carry the **same** numbers, the paravector with a real time and the material element with an imaginary one.

**Why the conjugation.** Multiplication by the central $i$ alone exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, but it does not preserve the labels: it sends the space generator $i\vec e_k$ to $-\vec e_k$. The dictionary that keeps the labels is $i$ **composed with the Clifford conjugate**, $\tilde Q=i\,p^{\natural}$, because the conjugate negates the imaginary vector part and the multiplication negates it back. The plain dual $\star p=ip$ is the material element of the **parity-reflected** event. This is the whole cost of the change of time convention: the factor $i$ alone carries the space part to the wrong sign, and the Clifford conjugate is what undoes it.

## The Paravector as a Spacetime Vector

A paravector $p=p_te_t+i\vec p$ has a real time component $p_t$ and a spatial vector part $i\vec p$ with real components, and it represents the spacetime vector whose time component is $p_t$ and whose space components are $p_x,p_y,p_z$. The corpus writes the same vector as a material element with imaginary time; the two carry the same information. The practical difference is that the paravector's time is real: "spacetime" is then a four-dimensional real space with one timelike direction and the metric $(+,-,-,-)$, and a light ray is a generator of the null cone $p_t^2=\vec p\cdot\vec p$ of that space, a genuine cone and not the image of one under multiplication by $i$. The **interval** between two events is $p\,p^{\natural}=\langle p\rangle_{\natural}e_t$. The **modulus** of the displacement, $\Rho=\sqrt{\langle p\rangle_{\natural}}$ on the principal branch, is its invariant length, so the **proper time** along a timelike worldline is $\tau=\Rho/c$.

**The product of two paravectors.** The interval is the diagonal case of the one product the formalism needs. For two paravectors $p$ and $q$,

$$
p\,q^{\natural}
=(p_t+i\vec p)(q_t-i\vec q)
=\left(p_tq_t-\vec p\cdot\vec q\right)e_t+\vec p\times\vec q+i\left(q_t\vec p-p_t\vec q\right),
$$

and the three pieces are the three objects of the algebra. The coefficient of $e_t$ is the **Minkowski inner product** of the two spacetime vectors; the rest is **pure**, a biparavector, with the real vector part $\vec p\times\vec q$ and the imaginary part $i(q_t\vec p-p_t\vec q)$. Setting $q=p$ kills the pure part and leaves the interval, which is why $p\,p^{\natural}$ is the form and not a coincidence of the notation; setting the two vectors orthogonal, $p_tq_t=\vec p\cdot\vec q$, kills the scalar part and leaves the plane they span. The signs are worth checking once against the computation: the real vector $\vec p\times\vec q$ carries a plus, because the two factors of $i$ in the term $(i\vec p)(-i\vec q)$ cancel, and each mixed term carries a single $i$, since only one factor of the pair is imaginary.

**Proper velocity.** For a particle of velocity $\vec v=v\vec u_v$, with $\beta=v/c$ and $\gamma=(1-\beta^2)^{-1/2}$, the **proper velocity** is the paravector

$$
\tilde V_{\mathrm p}=\gamma\left(e_t+\beta\,i\vec u_v\right),
\qquad
\tilde V_{\mathrm p}\,\tilde V_{\mathrm p}^{\natural}
=\gamma^2\left(e_t+\beta i\vec u_v\right)\left(e_t-\beta i\vec u_v\right)
=\gamma^2\left(1-\beta^2\right)e_t=e_t ,
$$

using $(i\vec u_v)^2=e_t$ for a unit real vector. The unimodularity $\langle\tilde V_{\mathrm p}\rangle_{\natural}=1$ is the paravector form of the constant length of the four-velocity. The corpus's four-velocity is the material element $\tilde V=\gamma(ic\,e_t+\vec v)=\gamma c(ie_t+\beta\vec u_v)\in\mathbb{M}_-$, and the two are related by

$$
\tilde V=ic\,\tilde V_{\mathrm p}^{\natural},
\qquad\text{equivalently}\qquad
\tilde V_{\mathrm p}=-\frac{i}{c}\,\tilde V^{\natural},
$$

which is the corpus's polar-word statement $\tilde V=ic\,\mathcal B$ with $\mathcal B=\tilde U_{\mathrm b}^{-2}$ the four-vector factor. The paravector $\tilde V_{\mathrm p}$ is Hermitian and its time component is real; the four-velocity $\tilde V$ is anti-Hermitian and its time component is imaginary. The two are not related by the central $i$ alone: $i\tilde V_{\mathrm p}=\gamma(ie_t-\beta\vec u_v)$ carries the space part with the wrong sign, because $(i)(i\vec u_v)=-\vec u_v$. The factor $i$ and the Clifford conjugate act together, $ic\tilde V_{\mathrm p}^{\natural}$, exactly as in the dictionary of the previous section.

**The boost rotor is a paravector.** The corpus's boost rotor is

$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}
=\cosh\frac{\psi}{2}\,e_t+\sinh\frac{\psi}{2}\,i\vec u_{\mathrm b},
$$

a scalar plus an imaginary vector, so $\tilde U_{\mathrm b}\in\mathbb{M}_+=\mathcal{P}$: the rotor is itself a paravector, the half-angle one. Its square is the proper velocity, and with $\vec u_{\mathrm b}=\vec u_v$,

$$
\tilde U_{\mathrm b}^{2}
=\cosh^2\frac{\psi}{2}+\sinh^2\frac{\psi}{2}+2\cosh\frac{\psi}{2}\sinh\frac{\psi}{2}\,i\vec u_v
=\cosh\psi\,e_t+\sinh\psi\,i\vec u_v=\tilde V_{\mathrm p},
$$

with $\gamma=\cosh\psi$ and $\gamma\beta=\sinh\psi$. The rotor is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, and unimodular, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$; its inverse is its Clifford conjugate, $\tilde U_{\mathrm b}^{-1}=\tilde U_{\mathrm b}^{\natural}$, so the four-vector factor is $\mathcal B=\tilde U_{\mathrm b}^{-2}=\tilde V_{\mathrm p}^{\natural}$. The two relations together give the chain $\tilde V_{\mathrm p}=\tilde U_{\mathrm b}^{2}$, $\mathcal B=\tilde V_{\mathrm p}^{-1}$, $\tilde V=ic\,\tilde V_{\mathrm p}^{\natural}$.

## The Boost Rule

The computational advantage of the paravector interpretation is that the boost of a spacetime vector is a *product* rather than a sandwich with two factors.

**Theorem (boost rule).** Let $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+\sinh\frac{\psi}{2}i\vec u_{\mathrm b}$ be a boost rotor and $\tilde V_{\mathrm p}=\tilde U_{\mathrm b}^{2}$ the corresponding proper velocity. For a paravector $p=p_te_t+i\vec p$, split it into the part coplanar with the boost plane and the part orthogonal to it,

$$
p_\parallel=p_te_t+i\left(\vec p\cdot\vec u_{\mathrm b}\right)\vec u_{\mathrm b} ,
\qquad
p_\perp=i\left(\vec p-\left(\vec p\cdot\vec u_{\mathrm b}\right)\vec u_{\mathrm b}\right).
$$

Then the rotor congruence gives

$$
\boxed{\;\tilde U_{\mathrm b}\,p\,\tilde U_{\mathrm b}^{*}=\tilde V_{\mathrm p}\,p_\parallel+p_\perp\;}
$$

**Proof.** The two parts transform separately, because the rotor is a scalar plus a multiple of $i\vec u_{\mathrm b}$ and each part is a fixed element under commutation or anticommutation with that direction.

*The orthogonal part.* Two orthogonal imaginary vectors anticommute,

$$
(i\vec u_{\mathrm b})(i\vec p_\perp)=-\vec u_{\mathrm b}\vec p_\perp=+\vec p_\perp\vec u_{\mathrm b}=-(i\vec p_\perp)(i\vec u_{\mathrm b}),
$$

so the cross terms in the congruence cancel and the squared term contributes a minus sign:

$$
\tilde U_{\mathrm b}\,p_\perp\,\tilde U_{\mathrm b}^{*}
=\left(\cosh\frac{\psi}{2}+\sinh\frac{\psi}{2}i\vec u_{\mathrm b}\right)p_\perp\left(\cosh\frac{\psi}{2}+\sinh\frac{\psi}{2}i\vec u_{\mathrm b}\right)
=\left(\cosh^2\frac{\psi}{2}-\sinh^2\frac{\psi}{2}\right)p_\perp=p_\perp .
$$

*The coplanar part.* The element $p_\parallel$ is a scalar plus a multiple of $i\vec u_{\mathrm b}$, hence commutes with $i\vec u_{\mathrm b}$ and with the rotor, and the congruence collapses to a square:

$$
\tilde U_{\mathrm b}\,p_\parallel\,\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}\,p_\parallel\,\tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{2}\,p_\parallel=\tilde V_{\mathrm p}\,p_\parallel .
$$

Adding the two parts gives the rule.

**The cell form.** A left multiplication is the cell $L_a\psi=a\psi$ and a right multiplication the cell $R_b\psi=\psi b$, so the congruence is the single two-sided operator $L_{\tilde U_{\mathrm b}}R_{\tilde U_{\mathrm b}^{*}}$. The rule says what that operator does to each part,

$$
L_{\tilde U_{\mathrm b}}R_{\tilde U_{\mathrm b}^{*}}\,p_\parallel=L_{\tilde V_{\mathrm p}}\,p_\parallel ,
\qquad
L_{\tilde U_{\mathrm b}}R_{\tilde U_{\mathrm b}^{*}}\,p_\perp=R_{e_t}\,p_\perp ,
$$

so a two-sided operator on the paravector space is a one-sided operator on each of the two parts: the left cell of the proper velocity on the coplanar part, the identity on the orthogonal part. That is the operator content of the rule, and the reason a boost of a plane wave is a pair of one-sided operations rather than a conjugation.

**What was gained.** The rule multiplies only the coplanar part and leaves the orthogonal part fixed. Against the sandwich it needs one factor instead of two; against a matrix it needs no basis in which the boost is aligned. The source uses it for the standard kinematical statements — the composition of velocities, the contraction of a moving rod, the relativity of simultaneity, the transformation of the field — and each becomes a one-line computation.

## Composite Systems: Biparavectors and the Six Planes

A **biparavector** is a product of two orthogonal paravectors, and it represents a **plane in spacetime**, in the same way that a bivector of the algebra of physical space represents a plane in physical space. Spacetime has four dimensions, so there are $\binom{4}{2}=6$ independent planes, and in the corpus's basis they are simply the three imaginary vector units and the three real ones:

$$
\left\{i\vec e_x,\ i\vec e_y,\ i\vec e_z\right\}\ \cup\ \left\{\vec e_x,\ \vec e_y,\ \vec e_z\right\},
$$

because $(i\vec e_j)(i\vec e_k)=-\vec e_j\vec e_k$ is a real vector for $j\neq k$: $(i\vec e_y)(i\vec e_x)=\vec e_z$, and the cyclic images give $\vec e_x$ and $\vec e_y$. The first triple consists of the planes that contain the time direction, the **timelike** (boost) planes; the second triple consists of the **spacelike** (rotation) planes. The biparavector space is therefore the corpus's six-dimensional **pure** subspace,

$$
\mathrm{Vect}(\mathbb{B})=\left\{\tilde Q : \tilde Q^{\natural}=-\tilde Q\right\},
$$

the space of the elements with no scalar part. A biparavector with a part in each triple generates a general Lorentz transformation: the timelike planes boost and the spacelike planes rotate.

Two consequences are worth stating, because they are what the paravector reading contributes to the rest of the series. First, the six planes are exactly the union of the vector parts of the two sectors: $i\vec e_k$ is the vector part of the paravector $p\in\mathbb{M}_+$, and $\vec e_k$ is the vector part of the material element $\tilde Q\in\mathbb{M}_-$. A plane is thus a vector part read in whichever sector one is working in, which is the algebraic reason a boost and a rotation are two readings of one six-dimensional object. Second, the **field strength** is a biparavector. Baylis writes it as $F=\vec E+ic\vec B$, one element of each triple, and the corpus's pure-vector field strength $\tilde F=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ is the same object up to normalization: multiplying $\tilde F$ by $-i/\sqrt{\epsilon}$ and using $\vec B=\mu\vec H$ and $c=1/\sqrt{\epsilon\mu}$ gives $\vec E+i\vec B/\sqrt{\epsilon\mu}=\vec E+ic\vec B$. The two readings put the factor $i$ on opposite halves. The source's $F$ makes the electric part real and the magnetic part imaginary; the corpus's $\tilde F$ makes the electric part imaginary and the magnetic part real, because in the $ict'$ convention the electric field carries the time index. The two triples are exchanged, and that exchange is the algebraic content of the asymmetry that *The Field-Strength Biquaternion and Its Invariants* records.

## The Grading, the Two Sectors, and the Compactness

Baylis names every graded subspace of $\mathrm{Cl}_{3,0}$ after the spacetime object it carries. In the corpus's basis the naming turns out to reproduce the corpus's own decomposition of $\mathbb{B}$ into a centre and a pure part, and the correspondence is exact:

| object | grades | basis | real dim | corpus subspace |
|---|---|---|---|---|
| scalar | $0$ | $e_t$ | $1$ | centre $\mathbb{C}_{\mathbb{B}}$ |
| pseudoscalar | $3$ | $i$ | $1$ | centre $\mathbb{C}_{\mathbb{B}}$ |
| vector | $1$ | $i\vec e_k$ | $3$ | vector part of $\mathbb{M}_+$ |
| bivector | $2$ | $\vec e_k$ | $3$ | vector part of $\mathbb{M}_-$ |
| **paravector** | $0+1$ | $e_t,\ i\vec e_k$ | $4$ | $\mathbb{M}_+$ |
| **biparavector** | $1+2$ | $i\vec e_k,\ \vec e_k$ | $6$ | $\mathrm{Vect}(\mathbb{B})$ |
| **triparavector** | $2+3$ | $\vec e_k,\ i$ | $4$ | $\mathbb{M}_-$ |

The four single grades carry the eight real dimensions between them, and each named object is a sum of consecutive grades. The last three rows are the three four- and six-dimensional objects of the algebra, and each of them is a subspace the corpus already names: the paravector is the informational sector, the biparavector is the pure subspace, and the triparavector is the material sector. The two four-dimensional sectors intersect in nothing but zero, and their vector parts are complementary halves of the pure subspace $\mathrm{Vect}(\mathbb{B})$.

Some care is needed with the word "dual". The Hodge star of $\mathrm{Cl}_{3,0}$ sends grade $k$ to grade $3-k$, so it sends a paravector to a triparavector and a vector to a bivector:

$$
\star p=p\,i=i\,p=p_ti-\vec p ,
$$

the scalar part becoming the pseudoscalar part $p_ti$ and the vector part becoming the real vector $-\vec p$. The image is the four-dimensional real space spanned by $\{i,\vec e_k\}$, which is exactly $\mathbb{M}_-$, the triparavector space: the dual carries $\mathbb{M}_+$ onto $\mathbb{M}_-$ and a paravector onto a triparavector. The space part changes sign under the dual, so $\star p$ is the material element of the **reflected** event; the material element of the event itself is $i\,p^{\natural}=\star\,p^{\natural}$, the dual of the conjugate. The corpus's four-current $\tilde J=ic\rho\,e_t+\vec J$ is the standing example of a triparavector — its scalar part is imaginary and its vector part real, which is the signature of $\mathbb{M}_-$.

The compactness has a cost, and it is a cost in the grading rather than in the algebra. In $\mathrm{Cl}_{1,3}$ the even subalgebra is graded $0,2,4$, and its bivectors split into three spacelike and three timelike ones; in $\mathrm{Cl}_{3,0}$ the same eight dimensions are regraded $0,1,2,3$. The identification $\mathrm{Cl}_{3,0}\cong\mathrm{Cl}^{+}_{1,3}$ is therefore a **regrading**, and the pairing follows the physics: a boost is generated in the algebra of physical space by the timelike plane $i\vec u_{\mathrm b}$ and in spacetime algebra by the timelike bivector that plane becomes, so grade one of the former corresponds to the **timelike** bivectors of the latter; grade two corresponds to the **spacelike** bivectors, grade zero to the scalar and grade three to the pseudoscalar. The opposite pairing is the same isomorphism composed with the Hodge star, and the physics fixes which one is meant. A vector of $\mathrm{Cl}_{3,0}$ is a plane of $\mathrm{Cl}_{1,3}$, and the two algebras hold the same eight components in grades of different names. The **compactness** the source claims is this saving: in $\mathrm{Cl}_{3,0}$ the eight real dimensions are all there is, the frame rotors are paravectors of the same algebra, the six planes are its pure part, and the two sectors exhaust it; in $\mathrm{Cl}_{1,3}$ the same rotors and planes are read in the even half of a sixteen-dimensional algebra. That is the whole trade: the cost is a renaming of the grades, and the saving is that nothing is duplicated.

**A caution about the wedge.** The symbol $\wedge$ is the corpus's **antisymmetric bilinear product**, the half-difference of the two orders:

$$
\tilde Q_1\wedge\tilde Q_2=\tfrac12\left(\tilde Q_1\tilde Q_2-\tilde Q_2\tilde Q_1\right).
$$

The scalar parts cancel in the commutator, so the wedge of two paravectors depends on the vector parts alone and is always pure,

$$
p\wedge q=-\vec p\times\vec q ,
$$

the negative cross product of the spatial parts: a pure element, with no component along $e_t$. It is not the exterior product of $\Lambda^2\mathbb{C}^4$: the commutator is not associative, whereas the exterior product is, and the wedge is valued in the algebra rather than in a space of two-forms. The corpus uses $\wedge$ in the first sense throughout, and the bridge to the exterior reading is the identification of a decomposable bivector with the two-plane its factors span.

## Velocity Composition

Let $B$ move with proper velocity $\tilde V_{\mathrm p,BA}=\tilde U_{\mathrm b,BA}^{2}$ relative to $A$, and $C$ with $\tilde V_{\mathrm p,CB}=\tilde U_{\mathrm b,CB}^{2}$ relative to $B$. The velocity of $C$ relative to $A$ is the velocity of $C$ relative to $B$ with the frame transformation from $B$ to $A$ applied to it, so the rotor of $C$ relative to $A$ is the product with the rotor of $B$ on the left:

$$
\tilde U_{CA}=\tilde U_{\mathrm b,BA}\,\tilde U_{\mathrm b,CB},
\qquad
\tilde U_{CA}\tilde U_{CA}^{*}=\tilde U_{\mathrm b,BA}\,\tilde U_{\mathrm b,CB}\tilde U_{\mathrm b,CB}^{*}\,\tilde U_{\mathrm b,BA}^{*}
=\tilde U_{\mathrm b,BA}\,\tilde V_{\mathrm p,CB}\,\tilde U_{\mathrm b,BA}^{*},
$$

where $\tilde U_{\mathrm b,CB}\tilde U_{\mathrm b,CB}^{*}=\tilde U_{\mathrm b,CB}^{2}$ uses the Hermiticity of the boost. The boost rule applied to the paravector $\tilde V_{\mathrm p,CB}$ then gives the composition law

$$
\boxed{\;\tilde V_{\mathrm p,CA}=\tilde V_{\mathrm p,BA}\,\tilde V_{\mathrm p,CB}^{\parallel}+\tilde V_{\mathrm p,CB}^{\perp}\;}
$$

with the split taken relative to $\vec u_{\mathrm b,BA}$. The box is the boost rule read as a composition law: the second velocity is boosted by the first, and its transverse part is untouched. For the standard example $\vec v_{BA}=0.5c\,\vec e_x$ and $\vec v_{CB}=0.4c\,\vec e_y$, the rule gives

$$
\tilde V_{\mathrm p,CA}=1.2599\left(e_t+i\left(0.5\,\vec e_x+0.34641\,\vec e_y\right)\right),
\qquad
\vec v_{CA}=\left(0.5,\ 0.34641,\ 0\right)c ,
$$

which is the textbook value $v_{y}=v_{y}'/[\gamma_{BA}(1+\beta_{BA}\beta_{x}')]$ with $\beta_{x}'=0$, the composed Lorentz factor being $\gamma_{CA}=1/\sqrt{1-0.5^2-0.34641^2}=1.2599$. The transverse part keeps its direction and loses the factor $\gamma_{BA}$, and no transverse velocity appears in the denominator because the component of $\vec v_{CB}$ along $\vec v_{BA}$ vanishes.

**The composite is not a boost.** $\tilde U_{CA}$ is a product of two Hermitian elements, hence Hermitian only when they commute. It is nevertheless of norm one, $\langle\tilde U_{CA}\rangle_{\natural}=1$, because the norm is multiplicative and each factor has norm one. Its polar word in the corpus's fixed order is

$$
\tilde U_{CA}=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

with $\tilde U_{\mathrm b}$ the Hermitian positive factor and $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ a real unit rotor. Then $\tilde U_{CA}\tilde U_{CA}^{*}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}^{2}=\tilde V_{\mathrm p,CA}$, and the rotor factor is the **Wigner (Thomas) rotation**: the algebraic reason the composition of two boosts is not a boost. In the example above it is a rotation of $6.40^{\circ}$ about $-\vec e_z$, the sign and the axis being fixed by the order of the two factors. The naive reading $\tilde V_{\mathrm p,CA}=\tilde U_{CA}^{2}$ is right only in the collinear case, where $\tilde u_{\mathrm r}=e_t$.

For **collinear** boosts the two factors commute, $\tilde U_{CA}$ is itself Hermitian, the rotor factor is the identity, and the law collapses to the product

$$
\tilde V_{\mathrm p,CA}=\tilde V_{\mathrm p,BA}\,\tilde V_{\mathrm p,CB},
$$

the order of the factors being immaterial. Writing each factor as $\gamma(e_t+\beta i\vec u_v)$ with a common direction and multiplying, the scalar part gives the composition of the Lorentz factors and the vector part the composition of the velocities,

$$
\beta_{CA}=\frac{\beta_{BA}+\beta_{CB}}{1+\beta_{BA}\beta_{CB}},
\qquad
\gamma_{CA}=\gamma_{BA}\gamma_{CB}\left(1+\beta_{BA}\beta_{CB}\right),
$$

which is the source's collinear composition law, written with the frame labels rather than with the indices $1,2$ of the source.

For **non-collinear** boosts the product $\tilde V_{\mathrm p,BA}\tilde V_{\mathrm p,CB}$ is not a proper velocity at all, and the naive product of the two proper velocities is the standard trap. The corpus develops the hyperbolic-geometry reading of the same law, with the rapidity as the geodesic distance and the Wigner rotation as the curvature, in *Velocity Space as Hyperbolic Geometry in Biquaternionic Form* and *Exercise: Boosting a Four-Velocity and Rapidity Composition*, and treats the rotation itself in *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form*.

## What the Paravector Reading Adds, and What It Does Not

**It adds three things.** A **real time**: the geometry is posed on a four-dimensional real space with an indefinite form, and the null cone is a cone in that space rather than the image of one under multiplication by $i$. A **computational rule**: the boost is a product with the proper velocity, $p\mapsto\tilde V_{\mathrm p}p_\parallel+p_\perp$, one multiplication instead of a congruence, together with a plane-geometric bookkeeping in which a boost is a function of the timelike plane and a rotation a function of the spacelike plane. And a **plane-valued field**: the field strength is a biparavector, a sum of the two triples, which is the algebraic reason the electric and magnetic parts are not on the same footing.

**It does not add a different theory.** The paravector space is the Hermitian subspace $\mathbb{M}_+$, the Clifford conjugate is the quaternion conjugation, the star is the identity there, and the Lorentz group is the same group of unit-norm biquaternions. Every external result written in the algebra of physical space is a result of the corpus in a different basis, and the dictionary above is the whole of the translation. The corpus's choice of the material sector, with its $ict'$ and its real vectors, is the choice to write the *anti-Hermitian* reading of the same four-vector; the paravector interpretation writes the *Hermitian* one, and the two are exchanged by the central $i$ composed with the Clifford conjugate.

The one genuinely new object in the source's programme is not a change of basis at all: the **electromagnetic plane wave as a rotation and a dilation**, an identity of the null cone treated in its own article (*The Boost of an Electromagnetic Plane Wave as a Rotation and a Dilation*). The paravector reading is what makes that identity one line of algebra.

## The Gamma Formulation

The gammas of this section are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, and they are **cells**, not elements. The section of the same name in *The Number Systems as Clifford Algebras* uses the word for the **elements** $i\vec e_k$; here it names the cells that represent those elements on the Dirac module. The module is what tells the two apart, and the cells act on it while the elements are multiplied. In the corpus's notation they are

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad
\gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad
\gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad
\gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad
\gamma_5=-iL_{e_t}R_{\vec e_z},
$$

Their Clifford relations, their chirality and their volume product are

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}L_{e_t}R_{e_t},
\qquad
g=\mathrm{diag}(1,-1,-1,-1),
\qquad
\gamma_5^{2}=L_{e_t}R_{e_t},
\qquad
\{\gamma_\mu,\gamma_5\}=0,
\qquad
\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5=-L_{e_t}R_{\vec e_z}.
$$

The metric here is the mostly-minus $g=\mathrm{diag}(1,-1,-1,-1)$, in which $\gamma_0^2=L_{e_t}R_{e_t}$ and $\gamma_k^2=-L_{e_t}R_{e_t}$. It is not the $\eta=\mathrm{diag}(-1,+1,+1,+1)$ of the material sector; the two differ by an overall sign, $\eta=-g$, and the sign shows up as the sign of $\gamma_0^2$. A frame whose time cell squares to $+1$ carries $g$; one whose time cell squares to $-1$ carries $\eta$.

The letter $\gamma$ is also used, in the algebra-of-physical-space literature, for the three **generators** of that algebra. That is a different object: the element

$$
i\vec e_k,\qquad k=x,y,z,
$$

generates $\mathrm{Cl}_{3,0}$ inside $\mathbb{B}$, with $(i\vec e_j)(i\vec e_k)+(i\vec e_k)(i\vec e_j)=2\delta_{jk}e_t$, $(i\vec e_k)^2=+e_t$ and $(i\vec e_x)(i\vec e_y)(i\vec e_z)=i$. The two uses of the letter are irreconcilable and both are standard, so this article keeps them apart: the four gamma cells appear only in this section, and everywhere else the three generators are written $i\vec e_k$. Read as an operator, a generator is the single left cell $L_{i\vec e_k}$, and the Clifford relations of the elements are the relations of those cells:

$$
L_{i\vec e_j}L_{i\vec e_k}+L_{i\vec e_k}L_{i\vec e_j}=2\delta_{jk}\,L_{e_t}R_{e_t}.
$$

The paravector calculus is therefore the calculus of *one-sided* cells of a three-dimensional Clifford set, and that is exactly what the boost rule of this article uses.

**The two Dirac equations.** The corpus carries two, and the paravector reading sits against both. The first is **one-sided** and chiral,

$$
L_{\tilde\nabla}\tilde\Psi_R=m\tilde\Psi_L,
\qquad
L_{\tilde\nabla^{\natural}}\tilde\Psi_L=m\tilde\Psi_R,
$$

a pair of lines in which the gradient acts from the left on each chiral half and the mass is the off-diagonal pairing that mixes them. The second is **two-sided**,

$$
\Bigl(i\frac{\partial}{\partial t'}+D_3\Bigr)F=mi\,\overline F\,\vec e_z ,
\qquad
D_3=\sum_{k=1}^{3}\vec e_k\frac{\partial}{\partial Q_k},
$$

a single equation on $\mathbb{B}$ whose left side is one-sided and whose mass term is a right multiplication by $\vec e_z$ accompanied by the componentwise complex conjugation. The distinction is not decoration. In the first equation the chirality is the splitting of the field into two halves, and on the Dirac module that splitting is carried by the $\gamma_5$ cell; in the second equation there is no split at all, and the chirality is the volume cell $-L_{e_t}R_{\vec e_z}$. The first is one-sided in the operator and doubled in the field; the second is two-sided in the operator and single in the field.

The paravector reading supplies the one-sided half: a paravector multiplying from the left is a cell $L_p$, and the whole of the boost rule is one-sided. What it does not supply is the doubling. A chirality is a grading: it must separate the module into two halves, so it must be an operator that anticommutes with the generators and squares to the identity. The volume element $i$ of the algebra of physical space is central and squares to $-1$; it multiplies every element by the same scalar and separates nothing. The two objects are often confused, and the confusion has a visible cause: in the cell formulation $\gamma_5^{2}=L_{e_t}R_{e_t}$ while $\gamma_5$ anticommutes with the four generating cells, and in the element formulation $i^2=-e_t$ while $i$ commutes with everything. A scalar and a grading cannot be the same object, and it is the reason the paravector literature writes one Dirac equation where the cell formulation writes two. The full account is in *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, §*The Two Equations of the Corpus*.

## Summary

The algebra of physical space, $\mathrm{Cl}_{3,0}$, is the biquaternion algebra read as a real algebra, and its paravector space is the Hermitian subspace $\mathbb{M}_+$, with the imaginary vectors $i\vec e_k$ as its three vector directions. Its Clifford conjugate is the quaternion conjugation, which negates grades one and two; its grade-reversing conjugation is the corpus's star, which fixes grades zero and one and is the identity on $\mathbb{M}_+$. Its Minkowski form $p\,p^{\natural}=(p_t^2-\vec p\cdot\vec p)e_t$ is the negative of the corpus norm of the material element $i\,p^{\natural}$, and the scalar part of $p\,q^{\natural}$ is the Minkowski inner product of two spacetime vectors.

The proper velocity $\tilde V_{\mathrm p}=\gamma(e_t+\beta i\vec u_v)=\tilde U_{\mathrm b}^{2}$ is unimodular, and the four-velocity is its material image, $\tilde V=ic\,\tilde V_{\mathrm p}^{\natural}$. The boost of a paravector is the **rule** $p\mapsto\tilde V_{\mathrm p}p_\parallel+p_\perp$, which fixes the part orthogonal to the boost plane and multiplies the coplanar part by the proper velocity; in the series' conventions this is the rotor congruence $\tilde U_{\mathrm b}p\tilde U_{\mathrm b}^{*}$, and in the cell notation the two-sided cell $L_{\tilde U_{\mathrm b}}R_{\tilde U_{\mathrm b}^{*}}$ is the left cell of the proper velocity on the coplanar part and the identity on the orthogonal part. Biparavectors are the six planes — the pure subspace $\mathrm{Vect}(\mathbb{B})$, three imaginary vector units and three real ones — and the field strength is one of them.

Rotors compose by multiplication and the composite is a norm-one element whose polar word has the Wigner rotation as its rotor factor; proper velocities compose by a product only for collinear boosts. The paravector interpretation is a presentation of the corpus's algebra with a real time and a one-sided boost; it introduces no new physics, and the one new identity of the source's programme is the boost of a plane wave.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$, $e_t=1,\ \vec e_k$ | Biquaternion algebra, quaternion basis with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$, central |
| $i\vec e_k$ | The three generators of the algebra of physical space; an object distinct from the gamma cells |
| $\mathcal{P}=\mathbb{M}_+$ | Paravector space, $\operatorname{span}_\mathbb{R}\{e_t,i\vec e_k\}$ |
| $p=p_te_t+i\vec p$ | Paravector, $p_t$ and $\vec p$ real |
| ${}^{\natural}$ | Quaternion conjugation, the Clifford conjugate of $\mathrm{Cl}_{3,0}$ |
| ${}^{*}=\overline{\cdot^{\natural}}$ | Hermitian conjugation, the grade-reversing conjugation of $\mathrm{Cl}_{3,0}$; the identity on $\mathbb{M}_+$ |
| $p\,p^{\natural}=(p_t^2-\vec p\cdot\vec p)e_t$ | Minkowski interval |
| $i\,p^{\natural}$ | Material element of the same event; $\star p=ip$ is the dual, the reflected event |
| $\vec u_v$, $\vec u_{\mathrm b}$ | Unit directions of the velocity and of the boost |
| $\tilde U_{\mathrm b}$ | Boost rotor, $\cosh\frac{\psi}{2}e_t+\sinh\frac{\psi}{2}i\vec u_{\mathrm b}$, a paravector |
| $\tilde V_{\mathrm p}=\tilde U_{\mathrm b}^{2}$ | Proper velocity, unimodular, $\gamma(e_t+\beta i\vec u_v)$ |
| $\tilde V=ic\,\tilde V_{\mathrm p}^{\natural}$ | Four-velocity, in $\mathbb{M}_-$ |
| $\mathcal B=\tilde U_{\mathrm b}^{-2}$ | Four-vector factor of the polar word |
| $p_\parallel,\ p_\perp$ | Coplanar and orthogonal parts relative to the boost plane |
| $p\mapsto\tilde V_{\mathrm p}p_\parallel+p_\perp$ | The boost rule |
| $\mathrm{Vect}(\mathbb{B})$ | Pure subspace, the biparavectors |
| $\tilde U_{CA}=\tilde U_{\mathrm b,BA}\tilde U_{\mathrm b,CB}$ | Composite rotor, norm one |
| $\tilde U_{CA}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | Polar word; $\tilde u_{\mathrm r}$ the Wigner rotation |

## Further Reading

- William E. Baylis, "Relativity in Introductory Physics", *Canadian Journal of Physics* **82** (2004) 853–873 (arXiv:physics/0406158), for the paravector formalism, the boost rule and the plane-wave identity.
- William E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the full development of the algebra of physical space.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the classification $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$ and the paravector calculus.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of boosts, rotors and the Lorentz group.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra comparison, in which $\mathrm{Cl}_{3,0}$ is the even subalgebra $\mathrm{Cl}^{+}_{1,3}$.
