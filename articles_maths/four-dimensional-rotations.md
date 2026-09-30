# __Four-Dimensional Rotations__

## Introduction

The rotations of $\mathbb{H}\cong\mathbb{R}^4$ about the origin form the group $SO(4)$, and they are classified by a pair of angles rather than by a single angle. In three dimensions a rotation has an axis, that is a fixed line, and one angle; in four dimensions a rotation fixes no line in general, and its normal form is a pair of planar rotations in two completely orthogonal planes. The two angles separate the three types: the **simple** rotations, which fix a plane pointwise, the **double** rotations, whose two angles differ, and the **isoclinic** rotations, whose two angles are equal and which therefore have infinitely many invariant planes.

Everything in the article is a consequence of one formula. A rotation is $\tilde x\mapsto\tilde q\,\tilde x\,\tilde p^{-1}$ for a pair of unit quaternions, and if the two factors are written in polar form $\tilde q = e^{\nu\theta}$ and $\tilde p = e^{\mu\phi}$ with $0\le\theta,\phi\le\pi$, then the eigenvalues of the rotation are $e^{\pm i(\theta+\phi)}$ and $e^{\pm i(\theta-\phi)}$. The two angles of the rotation are therefore the sum and the difference of the two half-angles. It follows that the simple rotations are those with $\theta = \phi$, that the isoclinic rotations are exactly those with one of the two factors equal to $\pm1$, so that they are the left and the right multiplications, and that everything depends on the two factors only through two angles and two axes.

The isoclinic rotations form two three-dimensional spheres inside $SO(4)$. The two spheres commute elementwise, each is a normal subgroup, and no rotation conjugates one of them into the other; the reflection $\tilde x\mapsto\bar{\tilde x}$ does exchange them. This is the exceptional position of dimension four among the rotation groups, and it is the reason $SO(4)$ is not simple. The last section reads the two angles in the Hopf coordinates of the unit sphere, where the rotation becomes a translation on a family of tori with the Clifford torus in the middle.

The parametrisation is not derived here. The two-sided action $\Phi_{(q_1,q_2)}(\tilde x) = q_1\tilde xq_2^{-1}$, its kernel $\{\pm(1,1)\}$ and the covering $Sp(1)\times Sp(1)\to SO(4)$ are *Quaternion Rotations and Reflections*, §*The Two-Sided Action and $SO(4)$*, and the group-theoretic statement $SO(4)\cong(SU(2)\times SU(2))/\{\pm1\}$ is *Matrix Groups and Classical Groups*. The normal form of an orthogonal map of a definite space is *The Rotation Group and Orientation*, §*The Normal Form of a Rotation*; only its reading in four dimensions is used here. The Hopf fibration of the unit sphere is *Quaternion Geometry*, the topology of the unit sphere and of the rotation group is *Quaternion Topology*, and the indefinite analogue of the classification, in which the circular blocks are replaced by hyperbolic ones, is *Biquaternion Rotations and Lorentz Transformations*.

The treatment is mathematical throughout: a rotation is an element of $SO(4)$ and no physical object is introduced. The three names are the classical ones of the geometry of four dimensions; what is added here is their quaternion content.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$ and $e_1e_2 = e_3$; a quaternion is $\tilde q = q_0e_0+q_1e_1+q_2e_2+q_3e_3$ with scalar part $q_0$ and vector part $\mathbf q = q_1e_1+q_2e_2+q_3e_3$, the conjugate is $\bar{\tilde q} = q_0e_0-\mathbf q$, the norm is $N(\tilde q) = \tilde q\bar{\tilde q}$, and the unit quaternions form $Sp(1) = S^3$. For a unit imaginary quaternion $\nu$ write $\mathbb{C}_\nu = \operatorname{span}(1,\nu)$ for the plane of the subalgebra it generates, and $\mathbb{C}_\nu^\perp = \operatorname{span}(w,\nu w)$ for its orthogonal complement, where $w$ is a unit vector orthogonal to $1$ and to $\nu$; then $we^{\nu\psi} = e^{-\nu\psi}w$ for every real $\psi$. The operators of left and right multiplication are $L_q(\tilde x) = \tilde q\tilde x$ and $\rho_q(\tilde x) = \tilde x\tilde q$, and they commute, $L_p\rho_q = \rho_qL_p$; the symbol $\rho_q$ is used here for right multiplication, written $R_q$ in *Quaternion 4x4 Regular Matrix Element Representation*. The planar rotation through $\alpha$ is the matrix $R(\alpha)$. Two square matrices are **orthogonally similar** when they differ by the change of an orthonormal basis, that is by conjugation by an element of $O(4)$, and they are **conjugate in $SO(4)$** when the change may be taken to be a rotation. Two planes are **completely orthogonal** when every line of the first is orthogonal to every line of the second.

## The Two Angles of a Rotation

### Invariant and Fixed Planes

**Definition.** Let $T\in SO(4)$. A plane $P$ through the origin is **invariant** for $T$ when $T(P) = P$, and **fixed** for $T$ when $T$ is the identity on $P$. A line is an **axis** of $T$ when it is fixed pointwise.

The restriction of a rotation to an invariant plane is an orthogonal map of that plane, hence a rotation or a reflection; the reflection case occurs only for planes that are not among those of the normal form below. For the planes of the normal form the restriction is a rotation, and its angle is called the **rotation angle** of that plane.

### The Normal Form in Four Dimensions

**Theorem (normal form; four dimensions).** Let $T\in SO(4)$. Then $T$ is orthogonally similar to the block diagonal matrix

$$
\mathrm{diag}\bigl(R(\alpha), R(\beta)\bigr), \qquad 0\le\beta\le\alpha\le\pi ,
$$

and the pair $(\alpha,\beta)$ is determined by $T$: the eigenvalues of $T$ are $e^{\pm i\alpha}$ and $e^{\pm i\beta}$, an eigenvalue $1$ counting as the angle $0$ and an eigenvalue $-1$ as the angle $\pi$. Consequently $T$ fixes a plane pointwise if and only if $\beta = 0$.

*Proof.* The theorem of *The Rotation Group and Orientation*, §*The Normal Form of a Rotation*, applied with $n = 4$: either $m = 2$, the fixed subspace has dimension $0$ and the normal form is the displayed one with the two angles of the non-real eigenvalue pairs, or $m = 1$, the fixed subspace has dimension $2$ and the normal form is $\mathrm{diag}(R(\alpha),1,1)$, which is the displayed one with $\beta = 0$. The angles lie in $[0,\pi]$ by the choice of the argument of each non-real eigenvalue pair, and their multiset is determined by the eigenvalues of $T$.

**Definition.** The **two angles** of $T\in SO(4)$ are the numbers $\alpha\ge\beta\ge0$ of the normal form; the **angle pair** is the unordered pair $\{\alpha,\beta\}$.

**Remark (the two planes).** The change of basis of the theorem is by an element of $O(4)$, so the two invariant planes of the normal form are orthonormal planes on which $T$ acts as $R(\alpha)$ and $R(\beta)$ respectively, and they are completely orthogonal. The pair of planes is unique for a generic rotation and far from unique for an isoclinic one, as the next sections show.

### The Three Types

**Definition.** A rotation $T\in SO(4)$ is **simple** when $\beta = 0$, **isoclinic** when $0<\beta = \alpha$, and **double** when $0<\beta<\alpha$.

The degenerate cases are the identity, $\alpha = \beta = 0$, whose angle pair is $\{0,0\}$, and the central inversion $-I$, whose angle pair is $\{\pi,\pi\}$; the central inversion is isoclinic and has no fixed vector.

The three types are tabulated with their fixed spaces and their planes.

| Type | Angle pair | Fixed space | The two planes of the normal form |
|---|---|---|---|
| Identity | $\{0,0\}$ | all of $\mathbb{H}$ | any pair of completely orthogonal planes |
| Simple | $\{\alpha,0\}$, $0<\alpha\le\pi$ | a plane | the fixed plane and its complement |
| Double | $\{\alpha,\beta\}$, $0<\beta<\alpha$ | $\{0\}$ | the only pair of invariant planes when $\alpha<\pi$ |
| Isoclinic | $\{\theta,\theta\}$, $0<\theta<\pi$ | $\{0\}$ | one pair among infinitely many |
| Central inversion | $\{\pi,\pi\}$ | $\{0\}$ | one pair among infinitely many |

**Proposition.** Let $T$ be a double rotation with angles $0<\beta<\alpha<\pi$. Then the two planes of its normal form are the only invariant planes of $T$.

*Proof.* Let $P$ be an invariant plane and extend scalars to $\mathbb{C}$. Since the four eigenvalues $e^{\pm i\alpha}, e^{\pm i\beta}$ are distinct, $T$ is diagonalisable with four eigenspaces of complex dimension one, and the invariant complex plane $P\otimes\mathbb{C}$ is the sum of two of them. A complex subspace is the complexification of a real one exactly when it is stable under complex conjugation, so the two eigenvalues involved are conjugate, and the two possibilities are $e^{i\alpha}, e^{-i\alpha}$ and $e^{i\beta}, e^{-i\beta}$. The first gives the plane of the angle $\alpha$ and the second the plane of the angle $\beta$.

## The Quaternion Parametrisation and the Two Angles

### The Parametrising Pair

**Definition.** For unit quaternions $\tilde q,\tilde p$ the **two-sided action** is the map

$$
\Phi_{(\tilde q,\tilde p)} : \mathbb{H}\longrightarrow\mathbb{H}, \qquad \Phi_{(\tilde q,\tilde p)}(\tilde x) = \tilde q\,\tilde x\,\tilde p^{-1} = L_q\rho_{p^{-1}}(\tilde x) .
$$

**Theorem.** Every element of $SO(4)$ is $\Phi_{(\tilde q,\tilde p)}$ for some pair of unit quaternions, and the pair is determined up to the simultaneous change of sign $(\tilde q,\tilde p)\mapsto(-\tilde q,-\tilde p)$.

*Proof.* This is the two-sided action and its kernel $\{\pm(1,1)\}$ of *Quaternion Rotations and Reflections*, §*The Two-Sided Action and $SO(4)$*.

Thus a rotation is exactly a pair $(\tilde q,\tilde p)$ of unit quaternions modulo the simultaneous sign, and the geometry of the rotation is the arithmetic of the pair. The rest of the article computes quantities of the rotation from the pair.

### The Two Isoclinic Families

**Proposition.** Let $\tilde q = e^{\nu\theta}$ with $\nu$ a unit imaginary quaternion and $\theta = \arccos(\operatorname{Re}\tilde q)\in[0,\pi]$. Then $L_q$ rotates both $\mathbb{C}_\nu$ and $\mathbb{C}_\nu^\perp$ through $\theta$.

*Proof.* On $\mathbb{C}_\nu = \operatorname{span}(1,\nu)$ the operator $L_q$ is multiplication by $\tilde q$ in the subalgebra $\mathbb{C}_\nu$, hence the rotation through $\theta$ in the basis $1,\nu$. On $\mathbb{C}_\nu^\perp = \operatorname{span}(w,\nu w)$ every element is $yw$ with $y\in\mathbb{C}_\nu$, and $L_q(yw) = \tilde qyw = (\tilde qy)w$, because $\tilde q$ and $y$ commute; the map $y\mapsto\tilde qy$ is the rotation through $\theta$ on $\mathbb{C}_\nu$, so $L_q$ rotates $\mathbb{C}_\nu^\perp$ through $\theta$ as well.

**Proposition.** Let $\tilde p = e^{\mu\phi}$ with $\mu$ a unit imaginary quaternion and $\phi = \arccos(\operatorname{Re}\tilde p)\in[0,\pi]$. Then $\rho_p$ rotates $\mathbb{C}_\mu$ through $\phi$ and $\mathbb{C}_\mu^\perp$ through $-\phi$.

*Proof.* On $\mathbb{C}_\mu$ the right multiplication by $\tilde p$ is multiplication by $\tilde p$, which is the rotation through $\phi$. On $\mathbb{C}_\mu^\perp = \operatorname{span}(w,\mu w)$ with $w$ orthogonal to $1$ and $\mu$, one has $\rho_p(yw) = yw\tilde p = y(w\tilde p) = y\,\bar{\tilde p}\,w$ for $y\in\mathbb{C}_\mu$, because conjugation by the unit vector $w$ reverses the sign of $\mu$ and fixes $1$; the map $y\mapsto y\bar{\tilde p}$ is the rotation through $-\phi$.

So a left multiplication and a right multiplication are the rotations that act with equal angles on a plane and its orthogonal complement, with the two signs in the second case. This is the geometric content of the two factors of the parametrisation.

### The Angles of a General Rotation

**Theorem (the two angles).** Let $T = \Phi_{(\tilde q,\tilde p)}$ with $\tilde q = e^{\nu\theta}$ and $\tilde p = e^{\mu\phi}$, where $0\le\theta,\phi\le\pi$. Then the eigenvalues of $T$ are

$$
e^{i(\theta+\phi)},\quad e^{-i(\theta+\phi)},\quad e^{i(\theta-\phi)},\quad e^{-i(\theta-\phi)} ,
$$

and the angle pair of $T$ is obtained from the two numbers $\theta+\phi$ and $\theta-\phi$ by reduction modulo $2\pi$ into $[0,\pi]$.

*Proof.* The eigenvalues and the angle pair are invariant under conjugation in $SO(4)$, and the reduction by conjugation is to suppose first that the two axes coincide, $\nu = \mu$. In that case the two planes $\mathbb{C}_\nu$ and $\mathbb{C}_\nu^\perp$ are invariant under both factors. On $\mathbb{C}_\nu$ one has $T(\tilde x) = \tilde q\tilde x\tilde p^{-1} = \tilde x\,\tilde q\tilde p^{-1}$ because $\tilde x$ commutes with both factors, so that $T$ is right multiplication by $\tilde q\tilde p^{-1} = e^{\nu(\theta-\phi)}$ there: the rotation through $\theta-\phi$. On $\mathbb{C}_\nu^\perp$ an element is $\tilde yw$ with $\tilde y\in\mathbb{C}_\nu$, and $T(\tilde yw) = \tilde q\tilde y\,w\tilde p^{-1}$; since $w\tilde p^{-1} = w e^{-\nu\phi} = e^{\nu\phi}w = \tilde pw$, this is $\tilde q\tilde y\tilde p\,w = \tilde y\,\tilde q\tilde p\,w$, the rotation through $\theta+\phi$ in the coordinate $\tilde y$. The eigenvalues of a planar rotation through $\gamma$ are $e^{\pm i\gamma}$, so when $\nu = \mu$ the four eigenvalues are those displayed. For the general case choose a unit quaternion $\tilde a$ with $\tilde a\nu\tilde a^{-1} = \mu$, which exists because the adjoint action of $Sp(1)$ on the unit imaginary quaternions is transitive, as in *Quaternion Rotations and Reflections*; conjugation by $L_a$ carries $T$ to $L_{aqa^{-1}}\rho_{p^{-1}} = L_{e^{\mu\theta}}\rho_{p^{-1}}$, a rotation with coinciding axes and hence the same eigenvalue list. Eigenvalues are invariant under conjugation, so the list is that of $T$.

**Corollary (the characteristic polynomial).** For unit quaternions $\tilde q,\tilde p$ the characteristic polynomial of $\Phi_{(\tilde q,\tilde p)}$ depends only on the two real parts,

$$
\chi(\lambda) = \lambda^4 - 4(\operatorname{Re}\tilde q)(\operatorname{Re}\tilde p)\lambda^3 + \bigl(4((\operatorname{Re}\tilde q)^2+(\operatorname{Re}\tilde p)^2-1)+2\bigr)\lambda^2 - 4(\operatorname{Re}\tilde q)(\operatorname{Re}\tilde p)\lambda + 1 ,
$$

so that the two angles of the rotation satisfy

$$
\cos\alpha+\cos\beta = 2\,(\operatorname{Re}\tilde q)(\operatorname{Re}\tilde p), \qquad \cos\alpha\cos\beta = (\operatorname{Re}\tilde q)^2+(\operatorname{Re}\tilde p)^2-1 .
$$

In particular the angles depend only on the real parts of the two factors and not on their axes.

*Proof.* By the theorem the four eigenvalues are $e^{\pm i(\theta+\phi)}, e^{\pm i(\theta-\phi)}$, so the characteristic polynomial is the product of the quadratics $\lambda^2-2\cos(\theta+\phi)\lambda+1$ and $\lambda^2-2\cos(\theta-\phi)\lambda+1$. Expanding and using $\operatorname{Re}\tilde q = \cos\theta$, $\operatorname{Re}\tilde p = \cos\phi$ together with $\cos(\theta+\phi)\cos(\theta-\phi) = \cos^2\theta+\cos^2\phi-1$ gives the display.

**Verification.** The statements of the article have been recomputed exactly, in rational arithmetic, on $100$ random elements for each check: the characteristic polynomial and its coefficients in terms of the two real parts; the two rotation angles in the case of coinciding axes, including the assignment of $\theta-\phi$ to the first plane and $\theta+\phi$ to the second; the translation law in the Hopf coordinates; the conjugation formula $\Phi_{(\tilde a,\tilde b)}\Phi_{(\tilde q,\tilde p)}\Phi_{(\tilde a,\tilde b)}^{-1} = \Phi_{(\tilde a\tilde q\tilde a^{-1},\tilde b\tilde p\tilde b^{-1})}$, against which the statement on the two spheres and the maximality of the tori are checked; the dimension of the fixed space against the criterion $\operatorname{Re}\tilde q = \operatorname{Re}\tilde p$; the isocliny criterion; and the exchange of the two spheres by the conjugation $\tilde x\mapsto\bar{\tilde x}$. The period of a trajectory of rational ratio has been recomputed in floating point, and the identification of the isoclinic trajectories with the circles $t\mapsto e^{e_1at}\tilde q_0$ likewise. The equidistribution of an irrational flow, the last clause of the periodicity proposition, is not recomputed and is cited as the classical equidistribution of a linear flow on a torus.

## The Three Types in Quaternion Terms

### The Simple Rotations

**Theorem.** Let $T = \Phi_{(\tilde q,\tilde p)}$ and suppose $T\neq\pm\mathrm{id}$. Then $T$ is a simple rotation if and only if $\operatorname{Re}\tilde q = \operatorname{Re}\tilde p$, that is if and only if the two half-angles are equal. The fixed plane is then the plane of the normal form with the angle $0$, and $T$ rotates the completely orthogonal plane through $2\theta$, read modulo $2\pi$, where $\theta = \arccos(\operatorname{Re}\tilde q)$.

*Proof.* By the theorem on the angles the pair is obtained from $\theta+\phi$ and $\theta-\phi$. A simple rotation has $\beta = 0$, that is one of the two numbers reduces to $0$ modulo $2\pi$; the sum reduces to $0$ exactly when $\theta+\phi$ is $0$ or $2\pi$, that is when $T$ is the identity or the central inversion, which are excluded; so the difference reduces to $0$, and $|\theta-\phi| = 0$ because both numbers lie in $[0,\pi]$, whence $\theta = \phi$ and, conversely, $\theta = \phi$ gives the difference $0$ and a fixed plane. The remaining angle is the sum $2\theta$, with the understanding that a value above $\pi$ is read modulo $2\pi$. For a unit quaternion the real part is $\cos\theta$ with $\theta\in[0,\pi]$, so $\operatorname{Re}\tilde q = \operatorname{Re}\tilde p$ is the same condition.

**Proposition (the rotations fixing the real line).** The assignments $\tilde q\mapsto\Phi_{(\tilde q,\tilde q)}$ are exactly the rotations of $\mathbb{H}$ that fix the real line pointwise, and they form the adjoint action, $\Phi_{(\tilde q,\tilde q)}(\tilde x) = \tilde q\tilde x\tilde q^{-1}$, a subgroup of $SO(4)$ isomorphic to $SO(3)$.

*Proof.* The map $\tilde x\mapsto\tilde q\tilde x\tilde q^{-1}$ fixes every real multiple of $1$ because $\tilde q$ and $\tilde q^{-1}$ commute past a real scalar, and it preserves the imaginary subspace, on which it is the adjoint action of *Quaternion Rotations and Reflections*, whose image is the copy of $SO(3)$ there; the kernel of the assignment on the diagonal is $\{\pm1\}$, so the image is $SO(3)$, and the fixed plane is the plane $\mathbb{C}_\nu$ of the subalgebra generated by $\tilde q$, because a quaternion commutes with $\tilde q$ exactly when it lies in that plane. Conversely, if a rotation $T = \Phi_{(\tilde q,\tilde p)}$ fixes the real line pointwise, then $T(1) = \tilde q\tilde p^{-1}$ is $1$, so $\tilde q = \tilde p$ and $T$ is the adjoint action.

### The Isoclinic Rotations

**Theorem.** Let $T = \Phi_{(\tilde q,\tilde p)}$. Then $T$ is isoclinic if and only if $\operatorname{Re}\tilde q = \pm1$ or $\operatorname{Re}\tilde p = \pm1$, that is if and only if $\tilde q = \pm1$ or $\tilde p = \pm1$. The isoclinic rotations are therefore exactly the left and the right multiplications.

*Proof.* The angle pair is obtained from $\theta+\phi$ and $\theta-\phi$, and a rotation is isoclinic when the two angles are equal and nonzero, which happens exactly when $\cos(\theta+\phi) = \cos(\theta-\phi)$, since the cosine is injective on $[0,\pi]$. The identity $\cos(\theta+\phi)-\cos(\theta-\phi) = -2\sin\theta\sin\phi$ vanishes with $\theta,\phi\in[0,\pi]$ exactly when $\theta\in\{0,\pi\}$ or $\phi\in\{0,\pi\}$, that is when $\tilde q = \pm1$ or $\tilde p = \pm1$. If $\tilde q = \pm1$ then $T = \rho_{p^{-1}}$ is a right multiplication and if $\tilde p = \pm1$ then $T = L_q$ is a left multiplication, and each of these is isoclinic by the two propositions on the factors.

**Definition.** An isoclinic rotation is **left-isoclinic** when it is a left multiplication and **right-isoclinic** when it is a right multiplication.

A left-isoclinic rotation $L_q$ rotates every plane of a certain family through $\theta$ with the same sense; a right-isoclinic rotation $\rho_p$ rotates its two planes through $\phi$ and $-\phi$. Both have the angle pair $\{\theta,\theta\}$ and $\{\phi,\phi\}$ respectively, which is the reason the normal form alone cannot separate them.

**Proposition (the four isoclinic rotations).** Let $\nu$ be a unit imaginary quaternion and $0<\theta<\pi$. Then the four rotations

$$
L_{e^{\nu\theta}},\qquad L_{e^{-\nu\theta}} = L_{e^{\nu\theta}}^{-1},\qquad \rho_{e^{\nu\theta}},\qquad \rho_{e^{-\nu\theta}} = \rho_{e^{\nu\theta}}^{-1}
$$

are pairwise distinct, and they are all the isoclinic rotations of the angle pair $\{\theta,\theta\}$ whose two planes of the normal form are the planes $\mathbb{C}_\nu$ and $\mathbb{C}_\nu^\perp$.

*Proof.* The two spheres are distinct by the theorem, and the inverses are distinct from the elements because $\theta$ is neither $0$ nor $\pi$. The left multiplications with the angle pair $\{\theta,\theta\}$ are the $L_{\tilde q}$ with $\operatorname{Re}\tilde q = \cos\theta$, a two-sphere of elements, and among them the two whose invariant planes are $\mathbb{C}_\nu$ and $\mathbb{C}_\nu^\perp$ are $L_{e^{\nu\theta}}$ and $L_{e^{-\nu\theta}}$, because the axis of $\tilde q$ must be $\pm\nu$; the same holds on the right.

### The Double Rotations

**Definition.** A rotation that is neither simple, nor isoclinic, nor the identity is a **double rotation**.

**Theorem.** Let $T = \Phi_{(\tilde q,\tilde p)}$. Then $T$ is a double rotation if and only if $\operatorname{Re}\tilde q\neq\operatorname{Re}\tilde p$ and $|\operatorname{Re}\tilde q|\neq1$ and $|\operatorname{Re}\tilde p|\neq1$; the angle pair is then obtained from $\theta+\phi$ and $|\theta-\phi|$ by reduction modulo $2\pi$ into $[0,\pi]$, and the two planes of the normal form are the only invariant planes when both angles are less than $\pi$.

*Proof.* The two exclusions are the criteria of the two preceding theorems, and the uniqueness of the planes is the proposition following the normal form.

The criteria are collected in a table.

| Type | Criterion on the pair $(\tilde q,\tilde p)$ | Angle pair |
|---|---|---|
| Identity | $\tilde q = \tilde p = \pm1$ | $\{0,0\}$ |
| Simple, not the identity | $\operatorname{Re}\tilde q = \operatorname{Re}\tilde p$ and $|\operatorname{Re}\tilde q|<1$ | $\{\alpha,0\}$ with $0<\alpha\le\pi$ |
| Left-isoclinic | $\tilde p = \pm1$ and $\tilde q\neq\pm1$ | $\{\theta,\theta\}$ with $0<\theta<\pi$ |
| Right-isoclinic | $\tilde q = \pm1$ and $\tilde p\neq\pm1$ | $\{\phi,\phi\}$ with $0<\phi<\pi$ |
| Central inversion | $\tilde q = -\tilde p = \pm1$ | $\{\pi,\pi\}$ |

## The Two Isoclinic Spheres

The isoclinic rotations carry the geometry of the parametrisation, and they form two subgroups.

**Definition.** The **left-isoclinic sphere** and the **right-isoclinic sphere** are

$$
S^3_L = \{L_q : \tilde q\in Sp(1)\}, \qquad S^3_R = \{\rho_q : \tilde q\in Sp(1)\}.
$$

**Theorem.** $S^3_L$ and $S^3_R$ are subgroups of $SO(4)$ isomorphic to $Sp(1)\cong S^3$; they commute elementwise, $L_q\rho_p = \rho_pL_q$; they meet in the centre of $SO(4)$, $S^3_L\cap S^3_R = \{\pm\mathrm{id}\}$; each is a normal subgroup of $SO(4)$, and $SO(4) = S^3_L\,S^3_R$ in the sense that every rotation is a product of one element of each.

*Proof.* The assignments $\tilde q\mapsto L_q$ and $\tilde p\mapsto\rho_p$ are injective homomorphisms with image a three-dimensional sphere because $N(L_q\tilde x) = N(\tilde x)$ on the unit sphere; the commutation is the identity $L_p\rho_q = \rho_qL_p$ of *Quaternion 4x4 Regular Matrix Element Representation*; the intersection statement is the criterion $L_q = \rho_p$ if and only if $\tilde q = \tilde p = \pm1$; normality and the product statement are the covering $SO(4)\cong(Sp(1)\times Sp(1))/\{\pm(1,1)\}$, in which the two factors are the images of the two spheres.

**Theorem (no conjugation between the two spheres).** Let $X = \Phi_{(\tilde a,\tilde b)}\in SO(4)$ be a rotation. Then

$$
X\,L_q\,X^{-1} = L_{\tilde a\tilde q\tilde a^{-1}} ,
$$

so conjugation by a rotation preserves each of the two spheres. The conjugacy class of a left-isoclinic rotation $L_q$ in $SO(4)$ is the two-sphere $\{L_{\tilde w} : \operatorname{Re}\tilde w = \operatorname{Re}\tilde q\}$, and no rotation conjugates a left-isoclinic rotation to a right-isoclinic one except the identity and the central inversion.

*Proof.* The conjugation identity follows from the commutation of left and right multiplication: $L_a\rho_bL_qL_{a^{-1}}\rho_{b^{-1}} = L_{aqa^{-1}}$ because the right factors cancel. Every element of $SO(4)$ is $\Phi_{(\tilde a,\tilde b)}$ by the parametrisation theorem of the previous section, so the whole conjugacy class is the displayed family, and it lies in $S^3_L$. The last statement is then the criterion $\rho_p = L_q$ if and only if $\tilde q = \tilde p = \pm1$: a right multiplication lies in $S^3_L$ only for $\pm\mathrm{id}$.

**Proposition (the exchanging reflection).** The map $\tilde x\mapsto\bar{\tilde x}$ is an element of $O(4)$ with determinant $-1$ and it conjugates $L_q$ to $\rho_{\bar{\tilde q}}$; hence it exchanges the two isoclinic spheres and reverses the isoclinic angle.

*Proof.* The map is the identity on the real line and minus the identity on the imaginary subspace, so its determinant is $-1$; and $\overline{\tilde q\,\bar{\tilde x}} = \tilde x\bar{\tilde q}$ shows $C L_q C^{-1} = \rho_{\bar{\tilde q}}$ for $C(\tilde x) = \bar{\tilde x}$.

**Remark (the exceptional position of dimension four).** The two spheres are normal subgroups of $SO(4)$, and their existence is exactly the failure of simplicity of $SO(4)$ recorded in *Matrix Groups and Classical Groups*. An isoclinic rotation of a given angle therefore lies in one of two conjugacy classes with the same normal form, and no rotation passes from one to the other; the reflection of the proposition passes from one to the other at the cost of leaving $SO(4)$ for $O(4)$. This splitting is the special feature of the four-dimensional rotation group.

## Hopf Coordinates and the Invariant Tori

### Hopf Coordinates of the Unit Sphere

**Definition.** Write a unit quaternion as $\tilde q = \tilde q_1+\tilde q_2e_2$ with $\tilde q_1,\tilde q_2\in\mathbb{C}_{e_1}$; the **Hopf coordinates** $(\xi_1,\eta,\xi_2)$ are the angles

$$
\tilde q = \sin\eta\;e^{e_1\xi_1} + \cos\eta\;e^{e_1\xi_2}e_2 , \qquad \eta\in\Bigl[0,\frac{\pi}{2}\Bigr], \quad \xi_1,\xi_2\in[0,2\pi) ,
$$

so that in the coordinates $(u,x,y,z)$ of $\tilde q = ue_0+xe_1+ye_2+ze_3$ one has $u = \sin\eta\cos\xi_1$, $x = \sin\eta\sin\xi_1$, $y = \cos\eta\cos\xi_2$ and $z = \cos\eta\sin\xi_2$.

**Proposition.** The Hopf coordinates are coordinates on the unit sphere, and $|\tilde q_1| = \sin\eta$ while $|\tilde q_2| = \cos\eta$; consequently the level set $\eta = \mathrm{const}$ with $0<\eta<\frac{\pi}{2}$ is a torus, the sets $\eta = 0$ and $\eta = \frac{\pi}{2}$ are circles, and the level set $\eta = \frac{\pi}{4}$ is the **Clifford torus** $|\tilde q_1| = |\tilde q_2| = \frac{1}{\sqrt2}$.

*Proof.* The sum of the squares of the four coordinates is $\sin^2\eta+\cos^2\eta = 1$, so every triple of angles gives a unit quaternion, and the four coordinates recover the angles in the stated ranges. The two blocks are $\tilde q_1 = \sin\eta\,e^{e_1\xi_1}$ and $\tilde q_2 = \cos\eta\,e^{e_1\xi_2}$, of the stated moduli, and each is an independent circle when $\eta$ is fixed and intermediate.

### The Rotation as a Translation

**Theorem.** Let $T$ be a rotation whose two invariant planes of the normal form are $\operatorname{span}(1,e_1)$ and $\operatorname{span}(e_2,e_3)$, with the angles $a$ and $b$ respectively. Then in Hopf coordinates $T$ acts as

$$
(\xi_1,\eta,\xi_2)\longmapsto(\xi_1+a,\ \eta,\ \xi_2+b).
$$

In particular the tori $\eta = \mathrm{const}$ and the Clifford torus are invariant, and the two angles of the rotation are the two angular velocities of the translation.

*Proof.* A rotation with these two invariant planes is $\Phi_{(\tilde q,\tilde p)}$ with $\tilde q = e^{e_1\theta}$ and $\tilde p = e^{e_1\phi}$, both factors in $\mathbb{C}_{e_1}$, and by the computation of the angle theorem the angle on $\operatorname{span}(1,e_1)$ is $\theta-\phi = a$ while the angle on $\operatorname{span}(e_2,e_3)$ is $\theta+\phi = b$, so that $\theta = \frac12(a+b)$ and $\phi = \frac12(b-a)$. On the first block the map is right multiplication by $\tilde q\tilde p^{-1} = e^{e_1a}$, so that $\sin\eta\,e^{e_1\xi_1}$ becomes $\sin\eta\,e^{e_1(\xi_1+a)}$; on the second block the coordinate is multiplied by $\tilde q\tilde p = e^{e_1b}$, so that $\cos\eta\,e^{e_1\xi_2}e_2$ becomes $\cos\eta\,e^{e_1(\xi_2+b)}e_2$. That is the display.

### The Trajectories

The orbit of a point of the unit sphere under the one-parameter group of the rotations with the angles $at$ and $bt$ is the curve $t\mapsto(\xi_1+at,\ \eta,\ \xi_2+bt)$ on the torus $\eta = \mathrm{const}$; the rotation is the linear flow of the two angles. The classical description of a linear flow on a torus applies.

**Proposition (periodicity).** The orbit of a point is periodic if and only if the ratio $a/b$ of the two angular velocities is rational, and if $a/b = p/q$ in lowest terms the flow returns to the identity after the time $2\pi|q|/|b| = 2\pi|p|/|a|$. If the ratio is irrational the orbit is dense in the torus.

*Proof.* The point returns to its starting value exactly when both $at$ and $bt$ are multiples of $2\pi$, that is when $t$ is a common period of the two translations; such a $t$ is $2\pi k/a = 2\pi l/b$ for integers $k,l$, which forces $k/l = a/b$, so if $a/b = p/q$ in lowest terms the common periods are the multiples of $2\pi q/b = 2\pi p/a$ and the orbit closes; if the ratio is irrational the two periods $2\pi/a$ and $2\pi/b$ are incommensurable and the orbit is dense, which is the equidistribution of a linear flow on a torus.

**Proposition (the isoclinic orbits).** If the rotation is isoclinic, $a = \pm b$, the orbit of a point is a great circle of the unit sphere; if the point lies on the Clifford torus the circle lies on that torus and is a Villarceau circle of it.

*Proof.* For $a = b$ the curve is $t\mapsto(\xi_1+at,\eta,\xi_2+at)$, which is $\tilde q(t) = e^{e_1at}\tilde q(0)$, the left translate of the starting point by a one-parameter subgroup, hence a great circle; for $a = -b$ it is the right translate, and the same argument applies. On the Clifford torus the left and right translates stay on the torus by the invariance of $\eta$.

### The Maximal Tori

**Definition.** The **stabiliser** of a pair of completely orthogonal planes is the set of rotations mapping each of the two planes to itself.

**Proposition.** Let $P$ and $Q$ be completely orthogonal planes. The identity component of the set of rotations mapping $P$ to $P$ and $Q$ to $Q$ is a two-dimensional torus $SO(2)\times SO(2)$, namely the group of the rotations $\Phi_{(\tilde q,\tilde p)}$ with both factors in the subalgebra plane of $P$; the stabiliser has a second component, the rotations that reverse both planes. These tori are the maximal tori of $SO(4)$ and they are all conjugate.

*Proof.* For $\tilde q,\tilde p\in\mathbb{C}_\nu$, where $\nu$ is the unit imaginary quaternion with $P = \mathbb{C}_\nu$ and $Q = \mathbb{C}_\nu^\perp$, the rotation $\Phi_{(\tilde q,\tilde p)}$ acts on $P$ as right multiplication by $\tilde q\tilde p^{-1}$ and on $Q$ as multiplication of the coordinate by $\tilde q\tilde p$, by the computation of the angle theorem; so the displayed group acts as a rotation in each plane, it is a torus of dimension two, and it is closed. The set of rotations preserving the two planes has dimension two, because $SO(4)$ acts transitively on the pairs of completely orthogonal planes, a set of dimension four, and $6-4 = 2$ by the orbit–stabiliser theorem; an element of the stabiliser restricts to an orthogonal map of each plane and the product of the two determinants is $1$, so either both restrictions are rotations, and the element lies in the displayed torus, or both are reflections: the second case is non-empty, an example being the rotation that reverses each plane and has determinant $(-1)(-1) = 1$. Hence the identity component is the torus and there is exactly one further component. No abelian subgroup is larger, because an abelian subgroup is contained in the centraliser of each of its elements, and the centraliser of a rotation whose two angles are distinct is the two-dimensional torus of the factors along its two axes, as the conjugation formula of the theorem on the two spheres shows. Finally all the pairs of planes are conjugate, hence so are the tori; the general theory of the maximal tori is that of *Lie Groups*.

## Comparison with the Neighbouring Articles

| Object | Article |
|---|---|
| The parametrisation, its kernel, the covering $Sp(1)\times Sp(1)\to SO(4)$ | *Quaternion Rotations and Reflections* |
| The normal form of an orthogonal map and its invariant planes | *The Rotation Group and Orientation* |
| $SO(4)\cong(SU(2)\times SU(2))/\{\pm1\}$ and the failure of simplicity | *Matrix Groups and Classical Groups* |
| The Hopf fibration and the quaternionic projective geometry | *Quaternion Geometry* |
| The unit sphere, the rotation group and their homotopy groups | *Quaternion Topology* |
| The Lorentz group and its hyperbolic blocks | *Biquaternion Rotations and Lorentz Transformations* |

**Remark (the indefinite contrast).** The classification of this article belongs to the definite form of $\mathbb{H}$. Over the indefinite form the same parametrisation produces the Lorentz group, the normal form of an element has hyperbolic blocks in place of the circular ones, and the analogue of the isoclinic pair is the pair of the rotations and the hyperbolic rotations; the compactness of $S^3$ is replaced by the non-compactness of the hyperboloid, and the flow on a torus by a flow on a cylinder. That theory is *Biquaternion Rotations and Lorentz Transformations* and *Split-Biquaternion Rotations and the Lorentz Group*.

## Summary

A rotation of $\mathbb{H}\cong\mathbb{R}^4$ is a pair of unit quaternions up to simultaneous sign, $\tilde x\mapsto\tilde q\tilde x\tilde p^{-1}$, and its normal form is a pair of planar rotations in two completely orthogonal planes with the angles $\alpha\ge\beta\ge0$. The eigenvalues of the rotation are $e^{\pm i(\theta+\phi)}$ and $e^{\pm i(\theta-\phi)}$, where $\theta$ and $\phi$ are the half-angles of the two factors; equivalently the characteristic polynomial depends only on the two real parts, $\operatorname{Re}\tilde q$ and $\operatorname{Re}\tilde p$, and the two angles satisfy $\cos\alpha+\cos\beta = 2\operatorname{Re}\tilde q\operatorname{Re}\tilde p$ and $\cos\alpha\cos\beta = (\operatorname{Re}\tilde q)^2+(\operatorname{Re}\tilde p)^2-1$. The two angles depend only on the two real parts and not at all on the two axes.

The classification follows from the two angles. A rotation is simple, that is it fixes a plane pointwise, exactly when the two real parts are equal, and it then rotates the completely orthogonal plane through twice the half-angle; it is a double rotation when the two real parts differ and neither is $\pm1$; it is isoclinic, that is its two angles are equal and nonzero, exactly when one of the real parts is $\pm1$, so that the rotation is a left or a right multiplication. The simple rotations fixing the real line are the adjoint action, a copy of $SO(3)$.

The isoclinic rotations form the two spheres $S^3_L$ and $S^3_R$ of the left and the right multiplications. The two spheres commute elementwise, meet in $\{\pm\mathrm{id}\}$, are normal subgroups of $SO(4)$, and generate it. Conjugation by a rotation carries $L_q$ to $L_{\tilde a\tilde q\tilde a^{-1}}$ and hence never leaves a sphere: no rotation conjugates a left-isoclinic rotation to a right-isoclinic one, and the conjugacy class of $L_q$ inside $SO(4)$ is the two-sphere of the left multiplications with the same real part. The reflection $\tilde x\mapsto\bar{\tilde x}$ exchanges the two spheres, and it has determinant $-1$, so the exchange is not available inside the rotation group. This splitting of the isoclinic rotations into two classes with the same normal form is the exceptional position of dimension four among the rotation groups, and the reason $SO(4)$ is not simple.

In the Hopf coordinates $\tilde q = \sin\eta\,e^{e_1\xi_1}+\cos\eta\,e^{e_1\xi_2}e_2$ of the unit sphere a rotation with the planes $\operatorname{span}(1,e_1)$ and $\operatorname{span}(e_2,e_3)$ invariant is the translation $(\xi_1,\xi_2)\mapsto(\xi_1+a,\xi_2+b)$ with $\eta$ unchanged. The level sets of $\eta$ are the invariant tori, the Clifford torus is $\eta = \frac{\pi}{4}$, the orbit of a point is periodic exactly when the ratio of the two angles is rational, and the isoclinic orbits are the great circles of the sphere, which on the Clifford torus are its Villarceau circles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}\cong\mathbb{R}^4$ | Quaternion algebra, the rotating space |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$, $e_1e_2 = e_3$ |
| $\tilde q = q_0e_0+\mathbf q$ | Quaternion, scalar part $q_0$, vector part $\mathbf q$ |
| $Sp(1) = S^3$ | Unit quaternions |
| $L_q(\tilde x) = \tilde q\tilde x$, $\rho_q(\tilde x) = \tilde x\tilde q$ | Left and right multiplication (right multiplication is $R_q$ elsewhere) |
| $\Phi_{(\tilde q,\tilde p)}(\tilde x) = \tilde q\tilde x\tilde p^{-1}$ | Two-sided action, a general rotation of $\mathbb{H}$ |
| $\mathbb{C}_\nu = \operatorname{span}(1,\nu)$, $\mathbb{C}_\nu^\perp$ | Plane of a unit imaginary quaternion $\nu$ and its complement |
| $R(\alpha)$ | Planar rotation through $\alpha$ |
| $\alpha\ge\beta\ge0$ | The two angles of a rotation, its normal form |
| simple / double / isoclinic | $\beta = 0$ / $0<\beta<\alpha$ / $0<\beta = \alpha$ |
| $\theta = \arccos(\operatorname{Re}\tilde q)$, $\phi = \arccos(\operatorname{Re}\tilde p)$ | The two half-angles of the parametrising pair |
| $S^3_L = \{L_q\}$, $S^3_R = \{\rho_q\}$ | The left- and right-isoclinic spheres |
| $(\xi_1,\eta,\xi_2)$ | Hopf coordinates of the unit sphere |
| $\eta = \frac{\pi}{4}$ | The Clifford torus |

## Further Reading

- Ludwig Schoute, *Mehrdimensionale Geometrie*, Volume 1 (Göschensche Verlagshandlung, Leipzig, 1902), for the classical account of the simple and the double rotations of four-dimensional space.
- Henry Parker Manning, *Geometry of Four Dimensions* (Macmillan, 1914; reprint Dover, 1954), for the synthetic treatment of the rotations of four-dimensional Euclidean space and of their invariant planes.
- L. van Elfrinkhof, "Eene eigenschap van de orthogonale substitutie van de vierde orde", *Handelingen van het 6e Nederlandsch Natuurkundig en Geneeskundig Congres* (Delft, 1897), for the factorisation of a four-dimensional rotation into a left-isoclinic and a right-isoclinic factor.
- Felix Klein, *Elementary Mathematics from an Advanced Standpoint*, Volume 1 (Macmillan, 1932), for the attribution of the factorisation of the four-dimensional rotation to Cayley.
- H. S. M. Coxeter, *Regular Polytopes* (Methuen, 3rd edition 1973; Dover reprint), for the double rotations, the Clifford torus and the regular figures of four dimensions.
- M. Erdoğdu and M. Özdemir, "Simple, Double and Isoclinic Rotations with Applications", *Mathematical Sciences and Applications E-Notes* (2020), for the classification of the four-dimensional rotations with the Rodrigues and Cayley formulae.
- H. Kim and G. Rote, "Congruence Testing of Point Sets in 4 Dimensions", arXiv:1603.07269 (2016), for the relations of the isoclinic rotations to the Clifford parallelism.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the rotation groups, their double covers and the failure of simplicity of $SO(4)$.
- Simon L. Altmann, *Rotations, Quaternions and Double Groups* (Oxford University Press, 1986), for the quaternion parametrisation of the four-dimensional rotations and the two-sided action.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition, 2001), for the isoclinic rotations, the Clifford torus and the Hopf fibration in the Clifford algebra setting.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion description of the four-dimensional rotation group and its finite subgroups.
