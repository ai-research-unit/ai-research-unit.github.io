# __Split-Biquaternion Polar Representation__

## Introduction

This article is about the polar representation in the split-biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$, where $\mathbb{D}$ is the split complex algebra. The result is that every split biquaternion is a modulus times a rotor,

$$
\tilde{Q} = \rho\,\tilde{U} , \qquad \rho \in \mathbb{D}, \quad \rho_{\pm} \ge 0, \qquad \tilde{U}\in S^3\times S^3 ,
$$

with the modulus a split complex number whose two components are non-negative reals and the rotor a pair of unit quaternions. The real dimensions are $2+6 = 8$, the modulus being two-dimensional and the rotor six-dimensional, and the modulus further separates into a positive real **scale** and a central **hyperbolic phase**,

$$
\tilde{Q} = \lambda\,e^{j\tau}\,\tilde{U} , \qquad \lambda = \sqrt{\rho_+\rho_-} \ge 0, \qquad \tau = \tfrac{1}{2}\ln\frac{\rho_+}{\rho_-} .
$$

Three features distinguish the case from the three previous algebras of the series, and they are the subject of the article. First, the square root that defines the modulus needs **no branch choice**: the split complex norm form has non-negative real components, each of which has a unique non-negative square root, so the modulus is canonical in a way that the biquaternion modulus, with its branch of $\sqrt{N(\tilde{Q})}$, is not. Second, there is **no boost slot**: the split biquaternion algebra is the direct sum of two copies of the quaternion algebra, its unit sphere is compact and six-dimensional, and its group of units is the direct product of that compact sphere and a central non-compact group, so every direction of non-compactness lies in the centre; the non-compact factors are exactly the scale and the hyperbolic phase. Third, the **degeneration occurs on the zero divisors and not on the null cone of the norm form**: the norm form of a split biquaternion vanishes only at the origin, and the elements on which the rotor is not determined are those with a vanishing idempotent component.

The article is the fourth and last of the series on the polar representations of the four real normed and semi-normed quaternion algebras, and it is organised in parallel with the reference article of the series, *Biquaternion Polar Representation*: the centre and the phase, the two halves, the norm form, the unit group and its two counts, the counting of the four slots, the order of the factors, the modulus, the second factor, the theorem, the algorithm, the meanings of the factors and the degenerate cases run in that order there and here, with four factors in the biquaternion case and two in this one. Two further sections treat what is particular to the present algebra: the behaviour of the decomposition under the conjugations, and the exponential form, which stands in the place of the biquaternion relation to the two partial forms, since this algebra has only one polar decomposition to relate. Conventions are those of *Split-Biquaternion Algebra*: the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the split complex unit is $j$ with $j^2 = +1$, central, the idempotents are $e_\pm = \tfrac12(1\pm j)$, an element is $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu = q_\mu + jq'_\mu \in \mathbb{D}$, and the norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. The isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ and the idempotent decomposition are used throughout. No physics is invoked. Every numerical value below was recomputed in double precision.

## Why Two Factors

### The Centre and the Hyperbolic Phase

The centre of $\mathbb{H}_{\mathbb{D}}$ is $\mathbb{D}$, the split complex scalars: an element commutes with every element of the algebra exactly when it lies in the span of $e_0$ and $j$. A central factor may therefore be moved through the other factors of a product without changing it, and every central direction of the unit group is a free one-parameter factor of any decomposition. The centre is not a field here but the split complex ring, and its group of positive units is
$$
\mathbb{D}_{>0} = \left\{\rho_+e_+ + \rho_-e_- : \rho_+,\rho_->0\right\} \cong \mathbb{R}_{>0}\times\mathbb{R}_{>0} ,
$$
the product of two rays, the two component magnitudes $\rho_+$ and $\rho_-$ of the representation, whose geometric mean and whose half-log-ratio are the scale and the hyperbolic phase. The central unit group therefore contains a non-compact factor, the hyperbola $e^{j\tau} = \cosh\tau + j\sinh\tau$, and this is the structural difference from the biquaternion algebra: there the centre is the complex field, whose unit group is the compact circle, and the centre contributes the compact phase alone.

### The Idempotent Halves

The split complex unit satisfies $j^2 = +1$, so the element

$$
e_+ = \tfrac12(1+j), \qquad e_- = \tfrac12(1-j)
$$

is idempotent: $e_\pm^2 = \tfrac14(1\pm2j+j^2) = \tfrac12(1\pm j) = e_\pm$. They are orthogonal, $e_+e_- = 0$, and they sum to $e_0$. Writing a split biquaternion as $\tilde{Q} = A + jA'$ with $A,A'\in\mathbb{H}$ the quaternion and split-quaternion parts, its two **idempotent components** are

$$
\tilde{Q}_+ = \tilde{Q}\,e_+ = e_+\left(A+A'\right), \qquad \tilde{Q}_- = \tilde{Q}\,e_- = e_-\left(A-A'\right),
$$

and the element is recovered from them by $\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-$, since $e_++e_- = e_0$. The map $\tilde{Q}\mapsto(\tilde{Q}_+,\tilde{Q}_-)$ is the algebra isomorphism $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ of the corpus, and the two components are the two copies. Multiplication is componentwise, so every algebraic question about a split biquaternion is a question about the pair. This split is the counterpart of the Hermitian and anti-Hermitian halves of the biquaternion algebra: there the algebra is split by the involution $\dagger$ into the fixed and the anti-fixed space, here by the central idempotents into two two-sided ideals, and the involution $\dagger$ is what exchanges the two halves.

### The Norm Form and the Zero Divisors

The norm form is

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3}Q_\mu^2 ,
$$

a split complex number, central and multiplicative. In the component form,

$$
N(\tilde{Q}) = N(\tilde{Q})_+e_+ + N(\tilde{Q})_-e_- , \qquad N(\tilde{Q})_{\pm} = \left|\tilde{Q}_{\pm}\right|^2 = \left|A\pm A'\right|^2 ,
$$

where the last quantities are the ordinary quaternion norm forms of the two components; this is the identity

$$
N(\tilde{Q}) = \left(|A|^2+|A'|^2\right) + 2j\,\langle A,A'\rangle ,
$$

whose two components are $|A|^2+|A'|^2 \pm 2\langle A,A'\rangle = |A\pm A'|^2$. Both components are positive definite as real quadratic forms, so

$$
N(\tilde{Q}) = 0 \quad\Longrightarrow\quad \tilde{Q} = 0 ,
$$

and the norm form does not detect the zero divisors. This is the sharpest structural difference from the biquaternion algebra, where the norm form is complex and vanishes on a cone of codimension two, and it is the reason the polar representation of this article has no null cone to fail on.

The zero divisors are instead the elements with a vanishing idempotent component. If $\tilde{Q}_+ = 0$ and $\tilde{Q}\neq0$ then $\tilde{Q} = \tilde{Q}_-$ is annihilated on the right by $e_+$, since $\tilde{Q}e_+ = \tilde{Q}_+e_+ = 0$; and dually for $\tilde{Q}_- = 0$. The invertible elements are exactly those with both components nonzero, and the group of units is

$$
\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{H}^{\times}\times\mathbb{H}^{\times} \cong \left(\mathbb{R}_{>0}\times Sp(1)\right)^2 ,
$$

of real dimension eight. The set of elements of unit norm form is smaller: it is the unit sphere $\{N(\tilde{Q}) = e_0\}\cong S^3\times S^3$ of dimension six, because a unit of $\mathbb{H}_{\mathbb{D}}$ may carry a scale in either component. Neither the norm form nor the zero divisors is where the polar representation fails, and the section on the domain isolates what is.

### The Unit Group and Its Two Counts

Since the algebra is the direct sum $\mathbb{H}\oplus\mathbb{H}$, its group of units is the direct product of the two unit groups of the halves,

$$
\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{H}^{\times}\times\mathbb{H}^{\times} \cong \left(\mathbb{R}_{>0}\times Sp(1)\right)\times\left(\mathbb{R}_{>0}\times Sp(1)\right) \cong \mathbb{D}_{>0}\times\left(S^3\times S^3\right) ,
$$

and the last form exhibits the group as a central non-compact factor times a compact one: the two rays of $\mathbb{D}_{>0}$ are the two scalar magnitudes of the halves, and $S^3\times S^3$ is the unit sphere. The four factors of the product are the four slots of the representation — two scalar rays and two spheres — with the two rays combining into the scale and the hyperbolic phase, and the two spheres into the rotor. The factorisation of a unit as $\tilde{Q} = \rho\,\tilde{U}$ with $\rho\in\mathbb{D}_{>0}$ and $\tilde{U}\in S^3\times S^3$ is the multiplication map
$$
\mathbb{D}_{>0}\times\left(S^3\times S^3\right)\longrightarrow\mathbb{H}_{\mathbb{D}}^{\times} ,
$$
and it is a bijection, not merely a factorisation of manifolds: if $\rho\tilde{U} = \rho'\tilde{U}'$ then $\rho^{-1}\rho' = \tilde{U}\tilde{U}'^{-1}$ lies in the intersection of $\mathbb{D}_{>0}$ with the unit sphere, which is $\{e_0\}$ — a central element $\rho_+e_+ + \rho_-e_-$ has norm form $\rho_+^2e_+ + \rho_-^2e_-$, equal to $e_0$ with non-negative components only when $\rho_+ = \rho_- = 1$ — so that $\rho = \rho'$ and $\tilde{U} = \tilde{U}'$. This is the point at which the split biquaternion case is simpler than the biquaternion case, where the corresponding multiplication map on $\mathbb{C}^*\times SL(2,\mathbb{C})$ is two-to-one, the two preimages differing by the sign of the modulus and of the unitary factor, and the branch $\alpha\in(-\pi/2,\pi/2]$ is what removes the doubling.

The Lie algebra of the unit group is $\mathbb{R}^2\oplus\mathfrak{su}(2)\oplus\mathfrak{su}(2)$: the abelian summand $\mathbb{R}^2$ is central and non-compact, and the two $\mathfrak{su}(2)$ summands are compact, one for each half. The correct statement of what the centrality of $\mathbb{R}^2$ implies is not that every non-compact one-parameter subgroup is central, which is false: the generator $e_0 + e_1$ of the unit group's Lie algebra has a central component and a non-central one, and the subgroup it generates,
$$
\exp\left(t(e_0+e_1)\right) = e^t\left(\cos t + \sin t\,e_1\right) , \qquad \left|\exp\left(t(e_0+e_1)\right)\right| = e^t ,
$$
is neither central — it fails to commute with $e_2$, since $\left[e_1,e_2\right] = 2e_3$ — nor relatively compact, since the quaternion modulus of its terms grows as $e^t$. What is true is that the **non-compact part of the unit group is central**: the group is the direct product of its maximal compact subgroup $S^3\times S^3$ and the central group $\mathbb{D}_{>0}$, so a one-parameter subgroup is non-compact exactly when its generator has a non-zero central component. There is therefore no non-central non-compact factor of the decomposition, and hence no boost slot: the analogue of the biquaternion boost is absent, and in its place the decomposition carries the hyperbolic central phase.

The contrast with the biquaternion algebra is exact and is worth stating in one line. There the centre is $\mathbb{C}$, whose unit group is the compact circle, and the non-compactness lives in the non-central Hermitian positive boosts; here the centre is $\mathbb{D}$, whose positive part is the non-compact product of two rays, and the non-central part is compact.

### The Counting

The real dimensions of the four slots are

$$
\dim\lambda = 1, \qquad \dim e^{j\tau} = 1, \qquad \dim(\text{boost}) = 0, \qquad \dim\tilde{U} = 6 ,
$$

and their sum is the real dimension of the algebra,

$$
1+1+0+6 = 8 = \dim_{\mathbb{R}}\mathbb{H}_{\mathbb{D}} .
$$

The additivity is the structural statement that the four slots are independent, exactly as in the biquaternion case; the difference is that the biquaternion distribution $1+1+3+3$ fills the two middle slots with two non-central three-dimensional families, whereas here the boost slot is empty and the rotor takes both of its dimensions, $6 = 3+3$. The companion articles on $\mathbb{H}$, $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ obtain $1+0+0+3$, $1+0+2+1$ and $1+1+3+3$ in the same four slots, and the comparison section below reads the four rows together.

### The Order of the Factors

**The order is not part of the word here, because the two factors commute.** In the biquaternion case the four factors are unique as an ordered quadruple, and the non-central boost forbids the transposition of the last two; here the modulus is central, so
$$
\rho\,\tilde{U} = \tilde{U}\,\rho
$$
exactly, in exact arithmetic because $\rho$ is central and to machine precision in the recomputation, where over three thousand random elements the largest coefficient difference of the two products was $8.9\times10^{-16}$. The rotor is non-central — its two halves are unit quaternions and the pair acts on the algebra by the two-sided action of the rotations section — but its non-centrality does not obstruct the reordering, because its partner in the word is central. The two halves of the rotor also commute with one another, and exactly so, because they lie in the two ideals:
$$
\left(u_+e_+\right)\left(u_-e_-\right) = u_+u_-\,e_+e_- = 0 = u_-u_+\,e_-e_+ = \left(u_-e_-\right)\left(u_+e_+\right) .
$$
So the representation may be written in any order of its three commuting exponentials — the scale, the hyperbolic phase and the rotor — and the rotor may be written as the product of its halves in either order. The condition that makes a word order-free is not that every factor be central but that the factors commute pairwise, and here they do. This is the second structural consequence of the empty boost slot: the biquaternion word is ordered because one of its factors is Hermitian positive and non-central, and this algebra has no such factor.

## The Split Complex Modulus

### The Componentwise Square Root

The modulus of the decomposition is defined by taking the square root of the norm form in the split complex algebra, componentwise:

$$
\rho = \sqrt{N(\tilde{Q})} \ \text{componentwise}, \qquad
\rho_+ = \sqrt{N(\tilde{Q})_+} = \left|A+A'\right|, \qquad \rho_- = \sqrt{N(\tilde{Q})_-} = \left|A-A'\right| .
$$

Both components of the norm form are non-negative reals, so both square roots exist and are the unique non-negative ones, and the modulus is

$$
\rho = \rho_+e_+ + \rho_-e_- = \tfrac12\left(\rho_++\rho_-\right) + \tfrac12\left(\rho_+-\rho_-\right)j ,
$$

whose square is the norm form, $\rho^2 = N(\tilde{Q})$, by construction.

### Uniqueness Without a Branch

In the biquaternion algebra the square root of the norm form requires a branch: the norm form is a complex number, its two square roots are exchanged by a sign, and the decomposition fixes the branch by requiring the modulus to be non-negative real after a phase is factored out. Here no such choice arises. Each component of the norm form is a non-negative real, each has a unique non-negative square root, and the modulus is therefore unique among the split complex numbers with non-negative components whose square is $N(\tilde{Q})$. The only element with vanishing modulus is the zero element, since $\rho_+ = \rho_- = 0$ forces $A+A' = 0$ and $A-A' = 0$ and hence $A = A' = 0$; and $\rho = 0$ for $\tilde{Q} = 0$ alone.

The absence of the branch is the algebraic content of the remark in the corpus that the norm form of $\mathbb{H}_{\mathbb{D}}$ is **anisotropic on each component**: what in the biquaternion case was a closed curve of choices of argument is here two disconnected rays, each of which has a distinguished point.

### The Modulus Is Not the Euclidean Norm

The modulus $\rho$ must be distinguished from the two other positive quantities attached to the algebra, and the article uses them in the comparison section. The **Euclidean norm** of the corpus is

$$
\|\tilde{Q}\|_E = \sqrt{\sum_\mu\left(q_\mu^2+q'^2_\mu\right)} = \sqrt{|A|^2+|A'|^2} ,
$$

which is definite and not multiplicative. The **split complex modulus** of the norm form is

$$
\left|N(\tilde{Q})\right| = \sqrt{N(\tilde{Q})_+N(\tilde{Q})_-} = \rho_+\rho_- ,
$$

a non-negative real, multiplicative because the norm form is. Neither is the modulus of the polar representation: $\rho$ is the componentwise square root of the norm form, it is split complex rather than real, and it is the object that the decomposition multiplies by the rotor.

## The Scale and the Hyperbolic Phase

### The Factorisation of the Modulus

The modulus is a split complex number with non-negative components, and such a number factors uniquely into a positive real and a hyperbolic phase. For $\rho_+,\rho_- > 0$, put

$$
\lambda = \sqrt{\rho_+\rho_-}, \qquad \tau = \tfrac12\ln\frac{\rho_+}{\rho_-} ,
$$

so that

$$
\lambda\,e^{j\tau} = \lambda\left(\cosh\tau + j\sinh\tau\right) = \rho_+e_+ + \rho_-e_- = \rho ,
$$

by the identities $\lambda\cosh\tau = \tfrac12(\rho_++\rho_-)$ and $\lambda\sinh\tau = \tfrac12(\rho_+-\rho_-)$, which are immediate from the definitions. The pair $(\lambda,\tau)$ is determined by $\rho$ and determines it, and the map is a group isomorphism

$$
\mathbb{D}_{>0} = \left\{\rho \in \mathbb{D} : \rho_+>0,\ \rho_->0\right\} \longrightarrow \mathbb{R}_{>0}\times\mathbb{R}, \qquad \rho\mapsto(\lambda,\tau) ,
$$

because $(\lambda e^{j\tau})(\lambda' e^{j\tau'}) = \lambda\lambda' e^{j(\tau+\tau')}$. The scale is the geometric mean of the two component moduli and the hyperbolic phase is half the logarithm of their ratio.

This is the exact analogue of the factorisation $R = re^{i\alpha}$ of the biquaternion modulus, with the compact unit circle $e^{i\alpha}$ replaced by the hyperbola $e^{j\tau}$. The replacement is not cosmetic: $e^{j\tau}$ is not bounded, so the phase factor here is a non-compact factor and carries a non-compact direction of the algebra.

### The Phase Is Central and Hyperbolic

Both factors of the modulus are central, and the second is not compact. In the biquaternion representation the modulus is central and the boost is not, and it is the non-centrality of the boost that makes the order of the four factors part of the statement; here the modulus commutes with the rotor, and the section on the order of the factors draws the consequence.

The phase factor is the hyperbola rather than the circle, and in components it is a pair of reciprocal dilations:

$$
e^{j\tau} = \cosh\tau + j\sinh\tau = e^{\tau}e_+ + e^{-\tau}e_- ,
$$

so the hyperbolic phase multiplies one half by $e^\tau$ and the other by $e^{-\tau}$, while the scale multiplies both halves by the same $\lambda$. The two factors of the modulus are therefore the two independent dilations of the two halves, and the factorisation of $\rho$ into a scale and a phase is the statement that an arbitrary pair of positive dilations is a common dilation times a reciprocal pair. The hyperbolic phase is the algebra's boost-like one-parameter group: it is one-dimensional and non-compact, it acts on the whole algebra by dilation of the two halves, and because it is central it produces no second-order effect of the kind a non-central boost produces. The Thomas-Wigner rotation of the biquaternion case requires two non-commuting non-central boosts, and this algebra has no non-central non-compact factor to supply them.

## The Rotor

### The Component Rotors

Dividing each idempotent component by its modulus gives a unit quaternion:

$$
u_+ = \frac{A+A'}{\rho_+} \in Sp(1), \qquad u_- = \frac{A-A'}{\rho_-} \in Sp(1) ,
$$

defined when the corresponding component of $\tilde{Q}$ is nonzero, and of quaternion norm one, since $|A\pm A'| = \rho_\pm$. Collecting them in the algebra,

$$
\tilde{U} = u_+e_+ + u_-e_- ,
$$

which is an element of the unit sphere: $N(\tilde{U}) = |u_+|^2e_+ + |u_-|^2e_- = e_+ + e_- = e_0$, and every element of the unit sphere arises this way, so

$$
\left\{\tilde{U} : N(\tilde{U}) = e_0\right\} = Sp(1)\times Sp(1) = S^3\times S^3 ,
$$

the product being taken through the idempotents. The set is compact and six-dimensional, and it is the double cover of the rotation group $SO(4)$ of the four-dimensional space $\mathbb{H}$ under the two-sided action $X\mapsto u_+Xu_-^{-1}$ of the companion article on rotations.

### The Rotor as an Exponential

Each half of the rotor is a unit quaternion, and each unit quaternion is the exponential of a pure quaternion. For each sign, write

$$
u_\pm = \cos\theta_\pm + \mu_\pm\sin\theta_\pm , \qquad \theta_\pm\in[0,\pi] ,
$$

with $\mu_\pm$ a unit pure real quaternion; the angle is unique, the axis is unique whenever $\sin\theta_\pm\neq0$, and the data degenerate exactly at the two central points $u_\pm = \pm e_0$, where the axis is arbitrary and the angle is $0$ or $\pi$. In the algebra the same statement reads

$$
\tilde{U} = \exp\left(\theta_+\mu_+e_+ + \theta_-\mu_-e_-\right) ,
$$

and the argument is an element of the Lie algebra of the unit group: the rotor is the exponential of an element of the compact part, and with the modulus it makes the polar representation a single exponential, as the section on the exponential form shows. The two angles are real, unlike the complex angle of the biquaternion Hamilton form; the angle data of the rotor is a pair of real numbers and not a split complex number. The axis of each half is a unit pure quaternion, so $\mu_+e_+ + \mu_-e_-$ is a root of $-e_0$ in the algebra, and the axes of the rotor are exactly the four-dimensional family $S^2\times S^2$ classified in *Split-Biquaternion Roots of Minus One*. Over three thousand random rotors the reconstruction $\tilde{U} = \exp(\theta_+\mu_+e_+ + \theta_-\mu_-e_-)$ had largest coefficient residual $4.3\times10^{-15}$.

### The Rotor Is the Compact Factor

The rotor is compact and six-dimensional, and it is the whole non-central part of the group of units: the unit group is the direct product of $S^3\times S^3$ with the central group $\mathbb{D}_{>0}$, so that a general unit is a rotation of the two halves together with a scale and a hyperbolic phase, and the two operations commute. In the biquaternion algebra the non-central part of the unit group is $SU(2)\times H^3$ — a rotor and a boost — and only half of it is compact; here the non-central part is compact and carries no non-compact direction at all. The two-sided action $X\mapsto u_+Xu_-^{-1}$ is the double cover $Sp(1)\times Sp(1)\to SO(4)$ of the companion article on rotations, and it is the action by which the rotor factor of a polar representation rotates a split biquaternion.

## The Theorem

### Statement

**Theorem (polar representation).** Let $\tilde{Q}\in\mathbb{H}_{\mathbb{D}}$. Then there are

$$
\rho\in\mathbb{D}, \quad \rho_+\ge0,\ \rho_-\ge0, \qquad \tilde{U}\in S^3\times S^3 ,
$$

such that

$$
\tilde{Q} = \rho\,\tilde{U} ,
$$

and the modulus $\rho$ is unique: it is the componentwise non-negative square root of the norm form. The rotor $\tilde{U}$ is unique if and only if $\tilde{Q}$ is invertible, equivalently if and only if both idempotent components of $\tilde{Q}$ are nonzero; if one component vanishes, the corresponding factor of $\tilde{U}$ is arbitrary, and if $\tilde{Q} = 0$ both factors are arbitrary.

### Existence

For any $\tilde{Q}$, put $\rho_\pm = |A\pm A'|$ and $\rho = \rho_+e_++\rho_-e_-$, and define $\tilde{U}$ by

$$
u_\pm = \frac{A\pm A'}{\rho_\pm} \quad\text{when } \rho_\pm\neq0, \qquad u_\pm\ \text{arbitrary in } Sp(1) \text{ otherwise},
$$

with the sign convention $A+A'$ for $u_+$ and $A-A'$ for $u_-$. Then, using $e_+^2 = e_+$, $e_-^2 = e_-$ and $e_+e_- = e_-e_+ = 0$,

$$
\rho\tilde{U} = \left(\rho_+e_++\rho_-e_-\right)\left(u_+e_++u_-e_-\right) = \rho_+u_+e_+ + \rho_-u_-e_- = \left(A+A'\right)e_+ + \left(A-A'\right)e_- = \tilde{Q},
$$

which is the claim. The verification was also carried out numerically on two thousand random elements, with worst defect $8.9\times10^{-16}$ in the reconstruction and $2.1\times10^{-14}$ in the identity $N(\tilde{Q})_\pm = \rho_\pm^2$.

### Uniqueness

The modulus is unique because each $\rho_\pm$ is the unique non-negative square root of the non-negative real $N(\tilde{Q})_\pm$, and $N(\tilde{Q})$ is determined by $\tilde{Q}$. The rotor is unique when both components of $\tilde{Q}$ are nonzero, because then both $\rho_\pm$ are nonzero and $u_\pm$ is forced to be $(A\pm A')/\rho_\pm$. When $\tilde{Q}_+ = 0$, the element carries no information about $u_+$, and $\tilde{U}$ is determined only in its $e_-$ factor; the verification of the non-uniqueness is the computation $\rho\tilde{U} = \rho_-u_-e_- = \tilde{Q}$ for every choice of $u_+$, which was checked numerically for three different choices on the zero divisor $\tfrac12(1+e_1)(1+j)$.

### The Domain and the Zero Divisors

The decomposition exists for **every** element of the algebra, including the zero element and including the zero divisors; no cone and no component condition is excluded. What the zero divisors lose is uniqueness, and what they lose with it is the scale-phase separation of the modulus, which the degenerate cases below record. The domain of this polar representation is therefore the largest of the four algebras of the series, and the reason is the anisotropy of the norm form: a split complex norm form whose two real components are positive definite can vanish only at the origin, so it cannot cut out a cone on which the modulus would vanish.

## The Algorithm

### The Steps

Given $\tilde{Q} = A + jA'$:

1. Form the two quaternion parts $A+A'$ and $A-A'$.
2. Compute the two non-negative real moduli $\rho_+ = |A+A'|$ and $\rho_- = |A-A'|$.
3. The modulus is $\rho = \rho_+e_+ + \rho_-e_- = \tfrac12(\rho_++\rho_-) + \tfrac12(\rho_+-\rho_-)j$, and it satisfies $\rho^2 = N(\tilde{Q})$.
4. When both moduli are positive, the scale is $\lambda = \sqrt{\rho_+\rho_-}$ and the hyperbolic phase angle is $\tau = \tfrac12\ln(\rho_+/\rho_-)$.
5. The rotor is $\tilde{U} = u_+e_+ + u_-e_-$ with $u_\pm = (A\pm A')/\rho_\pm$ when $\rho_\pm\neq0$, and any unit quaternion in the factors whose modulus vanishes.

No branch choice is required at any step, and the first four steps determine the output uniquely; only step five leaves the freedom described in the theorem, and only on the zero divisors.

### A Worked Example, Step by Step

Take

$$
\tilde{Q} = \left(1+2j\right)e_0 + j\,e_1 ,
$$

so that $A = e_0$ and $A' = 2e_0+e_1$. Then

$$
A+A' = 3e_0+e_1, \qquad A-A' = -e_0-e_1 ,
$$

so

$$
\rho_+ = \sqrt{10} = 3.162277660, \qquad \rho_- = \sqrt{2} = 1.414213562 ,
$$

and the modulus is

$$
\rho = 2.288245611 + 0.874032049\,j .
$$

The norm form is $N(\tilde{Q}) = 6+4j$, and indeed $6 = \tfrac12(10+2)$ and $4 = \tfrac12(10-2)$, which is the display $\rho^2 = N(\tilde{Q})$ in numbers; the split complex modulus of the norm form is $\rho_+\rho_- = \sqrt{20} = 4.472135955$.

The scale and the hyperbolic phase are

$$
\lambda = \sqrt{\rho_+\rho_-} = 20^{1/4} = 2.114742527, \qquad \tau = \tfrac14\ln 5 = 0.402359478 ,
$$

and the identities $\lambda\cosh\tau = 2.288245611$, $\lambda\sinh\tau = 0.874032049$ recover the modulus.

The rotor is $\tilde{U} = u_+e_++u_-e_-$ with

$$
u_+ = \frac{3e_0+e_1}{\sqrt{10}} = 0.948683298\,e_0 + 0.316227766\,e_1, \qquad u_- = -\frac{e_0+e_1}{\sqrt{2}} = -0.707106781\,e_0 - 0.707106781\,e_1 ,
$$

which is $\tilde{U} = \left(0.120788258 - 0.195439508\,e_1\right) + j\left(0.827895040 + 0.511667274\,e_1\right)$ in the form $A + jA'$. The reconstruction holds to $2.2\times10^{-16}$.

In exponential form, by the theorem of the section on the exponential form, the same element is

$$
\tilde{Q} = \exp\left(\ln\lambda + j\tau + \theta_+\mu_+e_+ + \theta_-\mu_-e_-\right) ,
$$

with $\ln\lambda = 0.748933068$, $\tau = 0.402359478$, the angle $\theta_+ = 0.321750554$ about the axis $\mu_+ = e_1$, and the angle $\theta_- = 2.356194490 = \tfrac34\pi$ about the axis $\mu_- = -e_1$; the single exponential reproduces $\tilde{Q}$ to $4.4\times10^{-16}$.

### A Second Example: an Element Already in Polar Form

Take $\tilde{Q} = j$. Then $A = 0$ and $A' = e_0$, so $A\pm A' = \pm e_0$, $\rho_+ = \rho_- = 1$, $\rho = e_0$, $\lambda = 1$, $\tau = 0$ and

$$
\tilde{U} = e_0e_+ - e_0e_- = e_+ - e_- = j ,
$$

so the decomposition is $\tilde{Q} = \tilde{U}$: the element is already a rotor, with modulus one, no scale and no phase. This is the analogue of the observation in the biquaternion case that a Lorentz rotor is already in polar form, and here it holds for every element of the unit sphere, because the unit sphere of the algebra is the rotor group itself. The steps of the algorithm reproduce it at once: $N(\tilde{Q}) = e_0$, $\rho = e_0$, $A+A' = e_0$, $A-A' = -e_0$, so $u_+ = e_0$ and $u_- = -e_0$.

## The Factors and Their Meanings

### The Table of the Factors

| factor | symbol | range | real dimension | what it is |
|---|---|---|---|---|
| scale | $\lambda$ | $(0,\infty)$ | $1$ | the geometric mean $\sqrt{\rho_+\rho_-} = \sqrt{\left|N(\tilde{Q})\right|}$ of the two component moduli |
| phase | $e^{j\tau}$ | $\cosh\tau + j\sinh\tau$, $\tau\in\mathbb{R}$ | $1$ | the central phase, half the logarithm of the ratio $\rho_+/\rho_-$; non-compact |
| boost | — | empty | $0$ | absent: the algebra has no non-central non-compact direction |
| rotor | $\tilde{U}$ | $S^3\times S^3 = Sp(1)\times Sp(1)$ | $6$ | a pair of unit quaternions, one for each idempotent half |

### The Scale

The scale is a positive real, central, and the factor that measures the common size of the two halves. It is the square root of the absolute value of the norm form,

$$
\lambda = \sqrt{\rho_+\rho_-} = \sqrt{\left|N(\tilde{Q})\right|} ,
$$

which is the exact analogue of the biquaternion scale $r = \sqrt{|N(\tilde{Q})|}$; the difference is in the absolute value, which for a complex number is the branch-free modulus and here is the product $\rho_+\rho_-$ of two non-negative reals. Replacing $\tilde{Q}$ by $\mu\tilde{Q}$ with $\mu>0$ multiplies $\lambda$ by $\mu$ and leaves the phase and the rotor unchanged, so the scale is the only factor that changes when the whole element is dilated. Being central, it multiplies both halves equally: the scale is the diagonal part of the pair of dilations of the halves, and the hyperbolic phase is the rest.

### The Hyperbolic Phase

The hyperbolic phase is central, non-compact and one-dimensional, and it is the factor that replaces the biquaternion boost. In components it multiplies the two halves by reciprocal factors,

$$
e^{j\tau} = e^{\tau}e_+ + e^{-\tau}e_- ,
$$

so it dilates one half by $e^\tau$ and contracts the other by $e^{-\tau}$; with the scale it completes the pair of independent dilations. It is determined by the ratio of the component moduli, $\tau = \tfrac12\ln(\rho_+/\rho_-)$, and it vanishes exactly when the two component moduli are equal, which is the condition $\langle A,A'\rangle = 0$ on the quaternion parts. Its non-compactness is the non-compactness of the algebra, and its centrality is why it acts on every element in the same way: a dilation of the halves has no axis to rotate and no sector to single out.

### The Rotor

The rotor is the pair of unit quaternions, of real dimension six, compact, and the only non-central factor of the decomposition. It is the factor that carries the rotations, both halves being rotations of the algebra's own four-dimensional Euclidean space in the two-sided action of the rotations article, and it is the factor whose freedom at a vanishing component is the whole of the non-uniqueness of the representation. Its two halves are independent and commute, so the rotor is a direct product and not a simple group: the rotor is $S^3\times S^3$, each half acting on its own idempotent component alone, and it is the largest of the four slots in every algebra of the series in which the boost slot is empty.

## Degenerate Cases

### The Unit-Norm Elements

If $N(\tilde{Q}) = e_0$ then $\rho = e_0$, $\lambda = 1$ and $\tau = 0$, and the representation reduces to

$$
\tilde{Q} = \tilde{U} , \qquad N(\tilde{Q}) = e_0 .
$$

The element is its own rotor: the unit sphere of the algebra is the rotor group $S^3\times S^3$ itself, of dimension six, and every element of it is already in polar form. This is the case in which the two factors of the decomposition are one, and it is the case the rotation theory of the companion article uses, in which a rotation of $\mathbb{R}^4$ is written by a pair of unit quaternions alone. The element $j = e_+ - e_-$ of the second example above is the least trivial illustration, its two halves being $e_0$ and $-e_0$, and the sign of the second half is the whole of its content.

### The Central Elements

If $\tilde{Q} = a + jb$ with $a,b\in\mathbb{R}$ then $A = ae_0$ and $A' = be_0$, so

$$
\rho_+ = |a+b|, \qquad \rho_- = |a-b|, \qquad u_+ = \operatorname{sgn}(a+b)\,e_0, \qquad u_- = \operatorname{sgn}(a-b)\,e_0 ,
$$

and the rotor is one of the four central elements $\pm e_+\pm e_-$, all of norm form $e_0$. The rotor is trivial, $\tilde{U} = e_0$, exactly when $a+b$ and $a-b$ are both positive, and then the element is its modulus alone. The element

$$
\tilde{Q} = 2e_+ + e_- = \tfrac32e_0 + \tfrac12j
$$

is of this kind: $\rho_+ = 2$, $\rho_- = 1$, $\rho = 1.5 + 0.5j$, $\lambda = \sqrt2 = 1.414213562$, $\tau = \tfrac12\ln2 = 0.346573590$ and $\tilde{U} = e_0$. Its decomposition is by the modulus alone, and it is the sharpest illustration of the empty boost slot: the only non-compact factors of the algebra are central, and this element exhibits one of them at a point where it commutes with everything and does nothing to the rotor.

### The Real Quaternions

If $\tilde{Q} = q\in\mathbb{H}$, that is $A = q$ and $A' = 0$, then $A\pm A' = q$, so $\rho_+ = \rho_- = |q|$, $\rho = |q|e_0$, $\lambda = |q|$, $\tau = 0$ and $\tilde{U} = (q/|q|)e_+ + (q/|q|)e_-$, which is the diagonal element $(u,u)$ with $u = q/|q|$. The polar representation of a real quaternion is therefore the quaternion polar representation itself, with the same unit factor in both halves: the modulus is the real number $|q|$ written as the central element $|q|e_0$, and the rotor is the diagonal element $u\,e_+ + u\,e_-$. The two factors of the present decomposition agree term by term with the two factors of the quaternion polar form of the companion article *Quaternion Polar Representation*. The two-sided rotor group contains the diagonal $S^3$ as the locus of the real quaternions, and a real quaternion carries no hyperbolic phase, its two component moduli being equal.

### The Zero Divisors

If exactly one idempotent component vanishes then $\tilde{Q}$ is a zero divisor, and exactly one component of the modulus vanishes. The scale and the phase degenerate,

$$
\lambda = \sqrt{\rho_+\rho_-} = 0, \qquad \tau = \tfrac12\ln\frac{\rho_+}{\rho_-} = \pm\infty ,
$$

the scale collapsing to zero and the phase diverging. The modulus $\rho$ itself does not degenerate — it remains a split complex number, and the product $\rho\tilde{U}$ remains the element — but it can no longer be separated into a scale and a phase. A zero divisor therefore has no scale, which is the precise sense in which it has no size, and it has no phase either, the ratio of its component moduli being zero or infinite.

For the witness, take

$$
\tilde{Q} = \tfrac12\left(1+e_1\right)\left(1+j\right) = \tfrac12\left(1+e_1\right)e_0 + \tfrac12j\left(1+e_1\right) ,
$$

so that $A = A' = \tfrac12(1+e_1)$ and the second idempotent component vanishes: $A-A' = 0$. Then

$$
\rho_+ = \left|1+e_1\right| = \sqrt2, \qquad \rho_- = 0, \qquad \rho = \sqrt2\,e_+ = 0.707106781 + 0.707106781\,j ,
$$

and the rotor has $u_+ = (1+e_1)/\sqrt2$ in its $e_+$ factor and an arbitrary unit quaternion in its $e_-$ factor: for $u_- = e_0$, $u_- = e_1$ and $u_- = 0.6e_0+0.8e_1$ the product $\rho\tilde{U}$ is the same element $\tilde{Q}$ in all three cases, to $5.6\times10^{-17}$. The element is a zero divisor and not a nilpotent one: its square is $e_1(1+j) = 2e_1e_+$, since $\left(1+e_1\right)^2 = 2e_1$, and it is the vanishing component of the modulus, not any nilpotency, that makes the rotor free.

### The Zero Element

For $\tilde{Q} = 0$ the modulus is $\rho = 0$ and the rotor is arbitrary: $0 = 0\cdot\tilde{U}$ for every $\tilde{U}$ in the rotor group, so the representation exists and is maximally non-unique. The scale and the phase are those of the zero modulus, that is, the scale is zero and the phase is undetermined. This is the only element at which the modulus itself vanishes, since $\rho_+ = \rho_- = 0$ forces $A = A' = 0$ and hence $\tilde{Q} = 0$.

## Behaviour Under the Conjugations

### The Four Conjugations and the Two Factors

The four conjugations act on the pair $(A,A')$ as follows: $\bar{\cdot}$ conjugates the two quaternion parts, $\bar{\tilde{Q}} = \bar{A} + j\bar{A}'$; ${}^{*}$ changes the sign of the split complex part, $\tilde{Q}^{*} = A - jA'$, so that $\tilde{Q}_{\pm}^{*} = \tilde{Q}_{\mp}$; $\dagger = \bar{\cdot}\circ{}^{*}$ does both; and $\flat = -\dagger$. Of these, $\bar{\cdot}$ and $\dagger$ are anti-automorphisms, ${}^{*}$ is an automorphism, and $\flat$ is neither, satisfying $(XY)^{\flat} = -Y^{\flat}X^{\flat}$ in place of an anti-automorphism law.

On the polar data the first three act as follows. Quaternion conjugation fixes the modulus — $\rho$ has real components, so $\bar{\rho} = \rho$ — and inverts each half of the rotor,

$$
\bar{\tilde{Q}} = \rho\,\bar{\tilde{U}} , \qquad \bar{\tilde{U}} = u_+^{-1}e_+ + u_-^{-1}e_- = \left(\cos\theta_+ - \mu_+\sin\theta_+\right)e_+ + \left(\cos\theta_- - \mu_-\sin\theta_-\right)e_- ,
$$

so it reverses both angles and keeps both axes. The split complex conjugation exchanges the two halves of every factor,

$$
\tilde{Q}^{*} = \rho^{*}\tilde{U}^{*} , \qquad \rho^{*} = \rho_-e_+ + \rho_+e_- , \qquad \tilde{U}^{*} = u_-e_+ + u_+e_- ,
$$

so it exchanges the two component moduli, sends $\tau$ to $-\tau$, keeps $\lambda$, and exchanges the halves of the rotor. The Hermitian conjugation does both,

$$
\tilde{Q}^{\dagger} = \rho^{*}\,\tilde{U}^{\dagger} , \qquad \tilde{U}^{\dagger} = u_-^{-1}e_+ + u_+^{-1}e_- ,
$$

reversing both angles and exchanging the halves. Where the biquaternion article records the behaviour of the phase, the boost and the rotor under the same four maps, the data here are correspondingly shorter: the modulus can only have its halves exchanged, and the rotor can only have its halves exchanged or its angles reversed. Over three thousand random elements each of these identities was verified with largest coefficient residual $3.6\times10^{-15}$, and the corresponding angle identities exactly.

### The Exponential

The three conjugations pass through the exponential, being (anti-)automorphisms: if $\sigma$ is $\bar{\cdot}$, ${}^{*}$ or $\dagger$ then $\sigma(\exp\tilde{Q}) = \exp(\sigma(\tilde{Q}))$, because $\sigma$ of a power of $\tilde{Q}$ is the corresponding power of $\sigma(\tilde{Q})$. The flat conjugation does not, and it is the one exception among the four:

$$
\left(\exp\tilde{Q}\right)^{\flat} = -\left(\exp\tilde{Q}\right)^{\dagger} = -\exp\left(\tilde{Q}^{\dagger}\right) = -\exp\left(-\tilde{Q}^{\flat}\right) ,
$$

which is not $\exp(\tilde{Q}^{\flat})$. The smallest counterexample is $\tilde{Q} = j$:

$$
\exp(j)^{\flat} = -\cosh1 + j\sinh1 = -1.543080635 + 1.175201194\,j , \qquad \exp\left(j^{\flat}\right) = \exp(j) = \cosh1 + j\sinh1 ,
$$

the two differing by $3.086161$ in the largest coefficient. The failure is a property of $\flat$ alone and of the sign with which it is defined, and it is the reason a statement that the exponential is preserved by the four conjugations must be narrowed to three, with the relation above in place of the fourth.

## The Exponential Polar Form

### The Exponential of an Element

The exponential is computed componentwise, because the algebra is a direct sum:

$$
\exp\tilde{Q} = \left(\exp\tilde{Q}_+\right)e_+ + \left(\exp\tilde{Q}_-\right)e_- , \qquad \exp\tilde{Q}_\pm = \exp\left(A\pm A'\right) ,
$$

each component being an ordinary quaternion exponential. Writing $\tilde{Q} = Q_0e_0 + \mathbf{Q}$ with the split complex scalar part $Q_0$ and the vector part $\mathbf{Q} = \sum_kQ_ke_k$, the scalar part is central and the vector part satisfies

$$
\mathbf{Q}^2 = -\sum_kQ_k^2 , \qquad \left(Q_0e_0\right)\mathbf{Q} = \mathbf{Q}\left(Q_0e_0\right) ,
$$

so the power series splits and gives

$$
\exp\tilde{Q} = e^{Q_0}\left(\cos\theta\,e_0 + \frac{\sin\theta}{\theta}\,\mathbf{Q}\right) , \qquad \theta^2 = -\mathbf{Q}^2 = \sum_kQ_k^2 ,
$$

with the split complex cosine, sine and square root taken componentwise in the central element $\theta$. This is the form of the de Moivre identity in this algebra: it is the analogue of the quaternion formula $\exp(q) = e^{q_0}(\cos|\mathbf{q}| + \mathbf{q}\sin|\mathbf{q}|/|\mathbf{q}|)$ and of the biquaternion formula with its complex angle, its angle here being split complex. Over three thousand random elements the identity was verified with largest coefficient residual $3.7\times10^{-14}$.

### The Vector Part

The square of the vector part is a split complex number with **non-negative** components:

$$
\theta^2 = \sum_kQ_k^2 = \sum_k\left(q_k^2+q'^2_k\right) + 2j\sum_kq_kq'_k , \qquad \theta^2_\pm = \sum_k\left(q_k\pm q'_k\right)^2 \ge 0 ,
$$

so $\theta$ is a split complex number with non-negative components and the exponential of a vector part is trigonometric in both halves, $\exp(\mathbf{Q})_\pm = \cos\theta_\pm + (\sin\theta_\pm/\theta_\pm)\mathbf{Q}_\pm$. There is therefore **no hyperbolic case for the vector part**. A classification of the exponential of a vector part by the sign of $\theta^2$ is not available in this algebra: the real part of $\theta^2$ is $\sum_k(q_k^2+q'^2_k)$, which is non-negative for every vector part and vanishes only at $\mathbf{Q} = 0$, and a split complex number has no sign to classify against. What distinguishes the two characters of $\theta^2$ is instead the equality of its two components:

$$
\theta^2\in\mathbb{R} \quad\Longleftrightarrow\quad \sum_kq_kq'_k = 0 \quad\Longleftrightarrow\quad \theta^2_+ = \theta^2_- ,
$$

checked against direct computation on four thousand random vector parts; when the mixed term does not vanish, $\theta^2$ is a genuinely split complex number with unequal non-negative components, and even then both halves of the exponential are trigonometric with real angles. The hyperbolic behaviour of the algebra lies in the split complex scalar part and not in the vector part:

$$
e^{Q_0} = e^{q_0}\left(\cosh q'_0 + j\sinh q'_0\right) , \qquad \exp(0.7j) = 1.255169006 + 0.758583702\,j ,
$$

and it is this factor that carries the boost-like direction. A worked instance of the split case, which also shows how little the splitness of $\theta^2$ costs, is

$$
\mathbf{Q} = e_1 + je_1 = 2e_1e_+ , \qquad \theta^2 = 4e_+ + 0\cdot e_- , \qquad \theta = 2e_+ , \qquad \exp(\mathbf{Q}) = \exp(2e_1)e_+ + e_- ,
$$

with $\exp(2e_1) = \cos2 + \sin2\,e_1 = -0.416146837 + 0.909297427\,e_1$. The vector part $\mathbf{Q}$ here is a zero divisor, and its exponential is not: the exponential misses the zero divisors, which is the subject of the last subsection below.

### The Nilpotent Case

It is worth recording the case that a reader may expect and that does not occur. For a vector part, $\mathbf{Q}^2 = 0$ forces $\mathbf{Q} = 0$, because the components of $\theta^2$ are sums of squares and vanish only when every $Q_k$ does; consequently the identity $\exp(\mathbf{Q}) = e_0 + \mathbf{Q}$ holds only at $\mathbf{Q} = 0$. More generally the algebra has no non-zero nilpotent element of any kind, because it is the direct sum $\mathbb{H}\oplus\mathbb{H}$ of two division algebras and a nilpotent of the sum has a nilpotent component in each summand; in the recomputation the smallest ratio $|X^2|/|X|$ over four thousand random non-zero elements was $0.754$. The zero divisors are not nilpotent: the witness of the previous subsection has square $-4e_+$, and the zero divisor witness $\tfrac12(1+e_1)(1+j)$ has square $e_1(1+j)$, both of them non-zero.

### The Logarithm

The logarithm is defined componentwise in the same way,

$$
\log\tilde{Q} = \left(\log\tilde{Q}_+\right)e_+ + \left(\log\tilde{Q}_-\right)e_- ,
$$

with the ordinary quaternion logarithm: for $q = ru$ with $r>0$ and a unit quaternion $u = \cos\theta + \mu\sin\theta$, $\theta\in[0,\pi]$, the logarithm is $\log q = \ln r + \theta\mu$. It is defined exactly on the invertible elements, the complement of the zero divisors, because the quaternion logarithm is defined on $\mathbb{H}\setminus\{0\}$. It is a relation and not a function: the angle of a unit quaternion is determined modulo $2\pi$, and at the two central points of each half the axis is arbitrary, so that

$$
\exp\left(2\pi k\,\mu e_+\right) = e_0 \quad\text{for every unit pure }\mu\text{ and every }k\in\mathbb{Z} , \qquad \exp\left(\ln r + \pi\mu\right) = -r ,
$$

both verified to machine precision. The fibre of the exponential over $e_0$ accordingly contains a two-sphere of directions at every non-zero multiple of $2\pi$. The polar representation fixes a representative of the logarithm by $\lambda>0$ and $\theta_\pm\in[0,\pi]$, the branch that the algorithm uses, and it is the only branch choice in the article.

### The Polar Representation as a Single Exponential

**Theorem.** An element of $\mathbb{H}_{\mathbb{D}}$ is the exponential of an element of the algebra exactly when it is invertible, and for an invertible element the polar representation is the exponential of a single element,

$$
\tilde{Q} = \exp\left(\ln\lambda + j\tau + \theta_+\mu_+e_+ + \theta_-\mu_-e_-\right) ,
$$

whose argument is the sum of the argument of the modulus, $\log\rho = \ln\lambda + j\tau$, and the argument of the rotor, $\log\tilde{U} = \theta_+\mu_+e_+ + \theta_-\mu_-e_-$.

**Proof.** The two summands commute, the first being central and the second lying in the compact part, so the exponential of the sum is the product of the exponentials and the product is $\rho\tilde{U} = \tilde{Q}$. If both components of $\tilde{Q}$ are non-zero then $\rho_\pm>0$, both quaternion logarithms exist, and the argument is defined; if a component vanishes then $\tilde{Q}$ is a zero divisor, and no exponential has a vanishing component, because $\left|\exp q\right| = e^{q_0}>0$ for every quaternion $q$. $\square$

**Consequences.** First, the exponential polar form of the earlier literature is not a second polar form of this algebra: it is the same decomposition with the modulus written as an exponential and each half of the rotor written as an exponential, and the two presentations differ only in the representative they choose for the argument of the modulus. Second, the domain of the exponential polar form is the invertible set and not the whole algebra, in contrast with the two-factor representation, whose domain is the whole algebra: the exponential is surjective onto the invertible elements and misses the zero divisors, which is the precise form of the failure recorded in the degenerate cases. Third, the count of polar forms for this algebra is a count of presentations and not of decompositions. The biquaternion partial forms arise from the three ways of splitting four factors into two pairs; two factors admit one splitting, so this algebra has no partial polar representations, and the two-factor grouping is available for every element of the algebra.

## Comparison with the Other Algebras of the Series

### The Four Slots

The four algebras of the series decompose in the same four slots, with the following real dimensions.

| algebra | scale | phase | boost | rotor | total |
|---|---|---|---|---|---|
| $\mathbb{H}$ | $1$ | $0$ | $0$ | $3$ | $4$ |
| $\mathbb{H}_{\mathrm{s}}$ | $1$ | $0$ | $2$ | $1$ plus a discrete reflection | $4$ |
| $\mathbb{B}$ | $1$ | $1$, elliptic: $e^{i\alpha}$ | $3$ | $3$ | $8$ |
| $\mathbb{H}_{\mathbb{D}}$ | $1$ | $1$, hyperbolic: $e^{j\tau}$ | $0$ | $6$ | $8$ |

The split biquaternion is the case in which the phase slot is non-compact, the boost slot is empty and the rotor slot is the largest. The pattern is not accidental. The rotor is the **compact part of the unit sphere** of the algebra and the boost is its non-compact part: in $\mathbb{H}$ and $\mathbb{H}_{\mathbb{D}}$ there is no boost, so the rotor is the whole unit sphere, of dimension three and six respectively; in $\mathbb{H}_{\mathrm{s}}$ the unit sphere is the three-dimensional group $SL(2,\mathbb{R})$ and splits into the two-dimensional boosts and the one-dimensional rotations, the reflections lying in the other component $\{N = -1\}$; in $\mathbb{B}$ the unit sphere is $SL(2,\mathbb{C})$, of dimension six, and splits into the three-dimensional boosts and the three-dimensional rotor. The two algebras of dimension eight distribute their eight real dimensions differently because in one of them the centre is the complex field and in the other the split complex ring.

### Where the Indefiniteness Goes

Each of the four algebras has an indefinite structure, and the polar representation exhibits it in a different slot.

In $\mathbb{H}$ there is none: the norm form is positive definite, and both the scale and the rotor are as definite as their counterparts in the complex numbers.

In $\mathbb{H}_{\mathrm{s}}$ the norm form has signature $(2,2)$ and its square root requires an absolute value; the indefinite direction is exhibited as a **boost** in the non-central Hermitian subspace, and the sign of the norm form survives as the determinant of the rotor.

In $\mathbb{B}$ the norm form is complex and its square root requires a branch; the two-dimensional family of branches is exhibited as the central **phase**, and the indefinite direction of the algebra is spent on the three-dimensional **boost**.

In $\mathbb{H}_{\mathbb{D}}$ the norm form is split complex and requires no branch; there is no cone on which the modulus vanishes, and there is no boost. The indefinite directions are exactly the two central ones, the scale and the hyperbolic phase, and the rotor is compact. The absence of the boost is the strongest structural statement of the comparison: the algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is semisimple of compact type, it has no non-zero nilpotent element, and the non-compact part of its unit group is central.

## Summary

Every split biquaternion $\tilde{Q} = A + jA'$ has a polar representation

$$
\tilde{Q} = \rho\,\tilde{U} , \qquad \rho = \rho_+e_+ + \rho_-e_- , \qquad \rho_\pm = \left|A\pm A'\right| \ge 0, \qquad \tilde{U} = u_+e_+ + u_-e_- ,
$$

with $u_\pm\in Sp(1)$, in which the modulus $\rho$ is the componentwise non-negative square root of the norm form and satisfies $\rho^2 = N(\tilde{Q})$, and the rotor lies in the unit sphere $S^3\times S^3$, of dimension six. The modulus is unique and needs no branch; the rotor is unique exactly when $\tilde{Q}$ is invertible, and on the zero divisors its vanishing-component factor is free. When both components of the modulus are positive, the modulus factors as $\rho = \lambda e^{j\tau}$ with the scale $\lambda = \sqrt{\rho_+\rho_-}$ and the hyperbolic phase $\tau = \tfrac12\ln(\rho_+/\rho_-)$; on the zero divisors $\lambda = 0$ and $\tau$ diverges, which is the sense in which a zero divisor has no scale. Among the four algebras of the series, $\mathbb{H}_{\mathbb{D}}$ is the one whose polar representation has no boost, whose phase factor is hyperbolic rather than elliptic, whose rotor is the largest, and whose domain is the whole algebra.

The two factors commute, so the order of the product is not part of the statement: $\rho\tilde{U} = \tilde{U}\rho$, and the two halves of the rotor commute with each other and with the modulus. The four conjugations act on the decomposition by exchanging the halves of the modulus and of the rotor or by reversing the two rotor angles; of the four, three pass through the exponential, and the flat conjugation $\flat = -\dagger$ does not, satisfying $(\exp\tilde{Q})^{\flat} = -\exp(\tilde{Q}^{\dagger})$ in place of $\exp(\tilde{Q}^{\flat})$. The representation also has an exponential form. The exponential of an element with split complex scalar part $Q_0$ and vector part $\mathbf{Q}$ is $\exp\tilde{Q} = e^{Q_0}(\cos\theta\,e_0 + (\sin\theta/\theta)\mathbf{Q})$ with $\theta^2 = \sum_kQ_k^2$, a split complex number whose two components are non-negative, so that no hyperbolic case occurs for the vector part; and every invertible element is the exponential of a single element, $\tilde{Q} = \exp(\ln\lambda + j\tau + \theta_+\mu_+e_+ + \theta_-\mu_-e_-)$, which is the polar representation written as one exponential. The exponential is surjective exactly onto the invertible elements and misses the zero divisors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | the split biquaternion algebra, real dimension eight |
| $j$ | the split complex unit, $j^2 = +1$, central |
| $e_\pm = \tfrac12(1\pm j)$ | the idempotents, $e_\pm^2 = e_\pm$, $e_+e_- = 0$, $e_++e_- = e_0$ |
| $\tilde{Q} = A + jA'$ | the quaternion and split-quaternion parts of an element |
| $\tilde{Q}_\pm = \tilde{Q}e_\pm = e_\pm(A\pm A')$ | the idempotent components |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | the norm form, split complex, anisotropic |
| $N(\tilde{Q})_\pm = \rho_\pm^2$ | the two non-negative components of the norm form |
| $\rho = \rho_+e_++\rho_-e_-$ | the modulus, the componentwise non-negative square root |
| $\lambda = \sqrt{\rho_+\rho_-}$ | the scale, a positive real except on the zero divisors |
| $\tau = \tfrac12\ln(\rho_+/\rho_-)$ | the hyperbolic phase angle |
| $\tilde{U} = u_+e_++u_-e_-$ | the rotor, an element of the unit sphere |
| $S^3\times S^3 = Sp(1)\times Sp(1)$ | the unit sphere and rotor group, dimension six, compact |
| $\theta_\pm\in[0,\pi]$, $\mu_\pm$ | the angle and unit axis of the two halves of the rotor, $u_\pm = \cos\theta_\pm + \mu_\pm\sin\theta_\pm$ |
| $\exp$, $\log$ | the exponential and the logarithm, componentwise on the two halves, $\log$ defined exactly on the invertible elements |
| $Q_0$, $\mathbf{Q}$ | the split complex scalar part and the vector part of an element |
| $\theta$ | the split complex angle of the exponential form, $\theta^2 = \sum_kQ_k^2$, with non-negative components |
| $\|\tilde{Q}\|_E$ | the Euclidean norm, $\sqrt{\sum_\mu(q_\mu^2+q'^2_\mu)}$, not multiplicative |

## Further Reading

- *Split-Biquaternion Algebra* (`articles_maths/split-biquaternion-algebra.md`), for the algebra, the idempotents, the conjugations, the norm form and the six subspaces.
- *Split-Biquaternion Norm and Invertibility* (`articles_maths/split-biquaternion-norm-and-invertibility.md`), for the anisotropy of the norm form, the invertibility criterion and the group of units.
- *Split-Biquaternion Zero Divisors* (`articles_maths/split-biquaternion-zero-divisors.md`), for the elements with a vanishing idempotent component on which the rotor is not unique.
- *Split-Biquaternion Roots of Minus One* (`articles_maths/split-biquaternion-roots-of-minus-one.md`), for the roots of $-e_0$, which are the axes of the two halves of the rotor and form the four-dimensional family $S^2\times S^2$.
- *Split-Biquaternion Elementary Functions* (`articles_maths/split-biquaternion-elementary-functions.md`), for the exponential, the logarithm and the elementary functions whose argument the polar decomposition of this article exhibits.
- *Split-Biquaternion Rotations and the Lorentz Group* (`articles_maths/split-biquaternion-rotations-and-the-lorentz-group.md`), for the unit sphere $S^3\times S^3$, the realisation of $SO(4)$ and the absence of parabolic subgroups.
- *Quaternion Polar Representation* (`articles_maths/quaternion-polar-representation.md`), *Split-Quaternion Polar Representation* (`articles_maths/split-quaternion-polar-representation.md`) and *Biquaternion Polar Representation* (`articles_maths/biquaternion-polar-representation.md`), for the other three algebras of the series.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), Chapter 3, for the polar representations of split biquaternions.
