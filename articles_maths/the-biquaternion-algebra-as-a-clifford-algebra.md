
# __The Biquaternion Algebra as a Clifford Algebra__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the even subalgebra of the real Clifford algebra $\mathrm{Cl}_{3,1}$ of a four-dimensional form of signature $(3,1)$, and it is likewise the real Clifford algebra $\mathrm{Cl}_{3,0}$ of a three-dimensional positive definite form, the complex Clifford algebra $\mathbb{C}\mathrm{l}_2$ of a two-dimensional complex form, and the complexification of the quaternion algebra $\mathbb{H}$. These descriptions differ in which structure is regarded as scalar — the real numbers, the complex numbers, or the quaternion units — and holding them apart is the key to using the algebra correctly. This article establishes the identification $\mathbb{B}\cong\mathrm{Cl}_{3,1}^{+}$ together with its competing labelling $\mathrm{Cl}_{1,3}$, computes the volume element, fixes the outer product and the four geometric grades, exhibits the idempotents and the zero divisors, and derives the Peirce decomposition and the minimal left ideals that carry the defining module.

The Clifford-algebra facts used here are those of the classification layer: $\mathrm{Cl}_{3,0}\cong M_2(\mathbb{C})$, the even parts of $\mathrm{Cl}_{3,1}$ and $\mathrm{Cl}_{1,3}$ are the same algebra $M_2(\mathbb{C})$, the volume element of an odd-dimensional algebra is central, and any idempotent $p$ of an algebra $A$ produces a Peirce decomposition $A=pAp\oplus pAq\oplus qAp\oplus qAq$ with $q=1-p$, together with the left ideal $Ap$. The algebra $\mathbb{B}$ itself, its multiplication, its four conjugations and its norm form $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_\mu Q_\mu^2$ are those of ; the idempotents $p,q$, the matrix units and the Peirce decomposition are those; and the zero divisors, with their norm-form description, are those. These, all of them, are cited rather than re-derived, and the computations below are included only to fix the conventions of the Clifford description. The module-theoretic statement about the defining module is the subject of *The Defining Module of the Biquaternion Algebra* and the spinor statement , and what is added here is the origin of both in the Clifford structure.

## The Identifications

**Theorem (the Clifford identification).** The biquaternion algebra is the even subalgebra of the real Clifford algebra of signature $(3,1)$:

$$
\mathbb{B}\cong\mathrm{Cl}_{3,1}^{+}.
$$

It is the even part of an even-dimensional Clifford algebra that acts on the spinor module, so this is the description in which the algebra and its module belong together; the module itself is not covered here.

**Proof.** Let $\Gamma_1,\Gamma_2,\Gamma_3,\Gamma_4$ generate $\mathrm{Cl}_{3,1}$, so that $\Gamma_k^2=+1$ for $k=1,2,3$, $\Gamma_4^2=-1$, and $\Gamma_i\Gamma_j=-\Gamma_j\Gamma_i$ for $i\neq j$. In the even part the three products $\Gamma_1\Gamma_2$, $\Gamma_1\Gamma_3$, $\Gamma_2\Gamma_3$ pairwise anticommute and each squares to $-1$, since $(\Gamma_i\Gamma_j)^2=-\Gamma_i^2\Gamma_j^2=-1$; three pairwise anticommuting elements of square $-1$ generate a copy of the quaternion algebra $\mathbb{H}$. The volume element $\Omega=\Gamma_1\Gamma_2\Gamma_3\Gamma_4$ anticommutes with each generator and therefore commutes with every even element of $\mathrm{Cl}_{3,1}$, and it satisfies $\Omega^2=-1$, because it is the product of four anticommuting generators whose squares multiply to $-1$; hence $\mathbb{R}[\Omega]\cong\mathbb{C}$ is a central subfield of $\mathrm{Cl}_{3,1}^{+}$ commuting with that copy of $\mathbb{H}$. Therefore $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ embeds in $\mathrm{Cl}_{3,1}^{+}$. Both sides have real dimension $8$, so the embedding is an isomorphism. $\square$

**Remark (the competing labelling and its sign).** The notation $\mathrm{Cl}_{3,1}$ records that three generators square to $+1$ and one to $-1$; the opposite convention is written $\mathrm{Cl}_{1,3}$, with one generator of square $+1$ and three of square $-1$. The two *even* subalgebras are the same algebra,

$$
\mathrm{Cl}_{3,1}^{+}\cong\mathrm{Cl}_{1,3}^{+}\cong M_2(\mathbb{C})\cong\mathbb{B},
$$

but the labelling is not cosmetic, and the sign consequence is explicit. In $\mathrm{Cl}_{3,1}$ the generator squares are $(+,+,+,-)$, so it is the three bivectors $\Gamma_1\Gamma_2,\Gamma_2\Gamma_3,\Gamma_3\Gamma_1$ that square to $-1$ and generate the copy of $\mathbb{H}$, while the three bivectors $\Gamma_k\Gamma_4$ square to $+1$ and generate a copy of $\mathrm{Cl}_{3,0}$; in $\mathrm{Cl}_{1,3}$ the generator squares are $(+,-,-,-)$, and although the combinatorial pattern of the even part is the same, the sign of the form on three of the four generators is reversed, so the sign of the norm form on the corresponding real subspace is reversed and the signature is $(1,3)$ rather than $(3,1)$. The full algebras differ and are not isomorphic over $\mathbb{R}$: $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, whereas $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$; they share the even part, and it is the even part that is the biquaternion algebra. A choice between the two labellings is therefore a choice of which real subspace of $\mathbb{B}$ carries the positive-definite part of the norm, and it must be fixed once and held throughout.

**Theorem (the companion identifications).** There are algebra isomorphisms

$$
\mathbb{B}\cong\mathrm{Cl}_{3,0}\quad(\text{as real algebras}), \qquad \mathbb{B}\cong\mathbb{C}\mathrm{l}_2\quad(\text{as complex algebras}),
$$

and the latter is the complexification of the quaternion algebra, $\mathbb{B}\cong\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$. The first is consistent with the Clifford identification above, because $\mathrm{Cl}_{3,1}^{+}\cong\mathrm{Cl}_{3,0}$: the three bivectors $\Gamma_k\Gamma_4$ generate a copy of $\mathrm{Cl}_{3,0}$ inside $\mathrm{Cl}_{3,1}^{+}$.

**Proof.** For the first, let $\gamma_1,\gamma_2,\gamma_3$ be the Clifford generators of $\mathrm{Cl}_{3,0}$, with $\gamma_k^2=+1$ and $\gamma_j\gamma_k=-\gamma_k\gamma_j$ for $j\neq k$, and let $e_k$ be the quaternion units of $\mathbb{B}$, with $e_k^2=-e_0$. The assignment $\gamma_k\mapsto ie_k$ sends generators to elements of square $(ie_k)^2=i^2e_k^2=(-1)(-1)=+1$ that anticommute, so it extends to an algebra homomorphism $\mathrm{Cl}_{3,0}\to\mathbb{B}$ by the universal property; both algebras are eight-dimensional over $\mathbb{R}$, so it is an isomorphism. For the second, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is a complex algebra of complex dimension four; it is central simple over $\mathbb{C}$ (its center is $\mathbb{C}$ and it has no proper two-sided ideals, being $\mathbb{C}\otimes$ a central simple real algebra), and the unique central simple complex algebra of dimension four is $M_2(\mathbb{C})=\mathbb{C}\mathrm{l}_2$. Finally $\mathbb{C}\mathrm{l}_2=\mathrm{Cl}_{2,0}\otimes_{\mathbb{R}}\mathbb{C}$, and the complexification of the quaternion algebra is $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}=\mathbb{B}$. $\square$

**Remark.** The two identifications are not interchangeable. As a real algebra $\mathbb{B}$ is $\mathrm{Cl}_{3,0}$, with a three-dimensional space of generators of square $+1$ and a volume element of square $-1$; as a complex algebra it is $\mathbb{C}\mathrm{l}_2$, with a two-dimensional space of generators and a volume element that is the product of two of them. The complex dimension is four in the second description and the real dimension is eight in the first, the ratio being the dimension of $\mathbb{C}$ over $\mathbb{R}$. A statement about $\mathbb{B}$ that uses the real structure — a reality condition on a module, a signature, a conjugation fixed point — belongs to the first description; a statement about the complex-linear structure belongs to the second.

**The complexification of $\mathbb{H}$.** In $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ the quaternion units remain and the scalars are doubled: every biquaternion is a quaternion with complex coefficients, and there is a decomposition $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ into the complexification's "real" and "imaginary" quaternionic parts. The central scalar $i$ commutes with the quaternion units, so the complexification is by a central element, and the resulting complex algebra is simple. By contrast, the complexification of $\mathrm{Cl}_{3,0}$ itself splits: $\mathbb{C}\mathrm{l}_3=\mathrm{Cl}_{3,0}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})\times M_2(\mathbb{C})$. The reason is that $\mathrm{Cl}_{3,0}$ is already a complex algebra with center $\mathbb{C}$, and for a complex algebra $A$ one has $A\otimes_{\mathbb{R}}\mathbb{C}\cong A\otimes_{\mathbb{C}}(\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C})\cong A\times A$, the splitting coming from $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$. The complex algebra $\mathbb{B}$ is one of the two factors rather than their product, and it is simple because $\mathrm{Cl}_{3,0}$ is central simple over its complex center.

## The Volume Element and the Central Scalar

**Theorem.** Let $\gamma_1,\gamma_2,\gamma_3$ generate $\mathrm{Cl}_{3,0}$ and let $\omega=\gamma_1\gamma_2\gamma_3$ be the volume element. Then $\omega$ is central, $\omega^2=-1$, and under the isomorphism $\gamma_k\mapsto ie_k$ the volume element is the central scalar imaginary, $\omega\mapsto i$.

**Proof.** The volume element of an odd-dimensional Clifford algebra is central: in a product of $n$ generators the monomial $\omega$ can be moved past each $\gamma_k$ at the cost of the sign $(-1)^{n-1}$, so for $n=3$ one has $\omega\gamma_k=(-1)^{n-1}\gamma_k\omega=\gamma_k\omega$ for every $k$, and $\omega$ commutes with all of them. Its square is $\omega^2=(-1)^{n(n-1)/2}\prod_kq(\gamma_k)=(-1)^{3}(+1)^3=-1$. Under $\gamma_k\mapsto ie_k$ one gets $\omega\mapsto (ie_1)(ie_2)(ie_3)=i^3e_1e_2e_3=(-i)(-1)=i$, using $e_1e_2e_3=-e_0$. $\square$

**Corollary.** The center of $\mathbb{B}$ is $\mathbb{C}$, spanned by $e_0$ and $i$, and the central scalar imaginary is the Clifford volume element. The algebra $\mathbb{B}$ is therefore central simple over $\mathbb{C}$: as a complex algebra it is $M_2(\mathbb{C})$, with one isomorphism class of irreducible module, of complex dimension two.

**Remark.** Because $\omega$ is central and of square $-1$, it defines a complex structure on $\mathrm{Cl}_{3,0}$ as a real algebra. This is the same complex structure that makes $\mathbb{B}$ a complex algebra, and it is the reason the real and complex descriptions agree so well in this dimension: the volume element supplies the scalar imaginary, so no exterior complexification is needed to reach $\mathbb{C}\mathrm{l}_2$. In even dimensions the volume element is not central, and the corresponding statement fails.

## The Outer Product and the Grades

The antisymmetric part of the biquaternion product is the outer product, and in this section's identification it is the cross product of the vector parts:
$$
p\wedge q := \tfrac12\bigl(pq-qp\bigr) = V(p)\times V(q),
$$
where $V(p)$ is the vector part of the algebra article, the components of $p$ along $e_1,e_2,e_3$, and $\times$ is the cross product on those three components. The scalar parts cancel in the commutator, so the identity holds for **all** pairs of biquaternions and not only for vector-like ones; it was verified on random pairs. The grading becomes visible on explicit values. Taking $V(p) = ie_1$ and $V(q) = ie_2$ gives $p\wedge q = -e_3$, a real pure quaternion; taking $V(p) = e_1$ and $V(q) = e_2$ gives $+e_3$, again real pure; and taking $V(p) = ie_1$ with $V(q) = e_2$ gives $ie_3$, imaginary pure. In the paper's language the product of two vectors is a bivector, the product of two bivectors is a bivector, and the product of a vector with a bivector is a vector, which is the content of the identity once the grades are named: geometric *vectors* are the imaginary pure quaternions and the *bivectors* the real pure quaternions.

The naming is where the literature is easily misled, and Sangwine, Ell and Le Bihan say so. The scalar/vector part terminology standard for quaternions labels the three quaternion units vectors, whereas in the Clifford reading they are directed areas; the axial and polar terminology of physics, they add, has caused further confusion, "because the two terms suggest different types of vector, rather than fundamentally different types of quantity", and even the authors had used "vector" in earlier work for what are now seen to be bivectors. Suter's summary is quoted with approval: "A quaternion is a scalar plus a bivector." The two terminologies in this corpus are reconciled by the identification of the article's Theorem: the generators are $\gamma_k = ie_k$, so the *imaginary* pure quaternion units are the Clifford vectors of the positive-definite form and the *real* pure quaternion units are its bivectors. The quaternion "vector part" is therefore the bivector grade of the Clifford dictionary, and the name is a convention of the quaternion literature rather than a grade statement. The four grades are exactly the four components isolated by the character projections of the involution article: $\Re S$ the scalar, $\Re V$ the bivector, $i\Im V$ the vector, and $i\Im S$ the pseudoscalar, which is also the volume element $i = \omega$.

**The dual operation.** Multiplication by the pseudoscalar is duality in this dictionary: it maps a bivector to a vector and a scalar to a pseudoscalar, and conversely; in the physics articles the same operation appears with a sign convention as the Hodge dual $\tilde F_\star = -i\tilde F$. **An open point.** The paper is explicit that the geometric reading is incomplete: after writing the general product as $pq = S(p)S(q) + S(p)V(q) + S(q)V(p) + V(p)V(q)$ and splitting the last term into its inner and outer parts, it states that "a deeper analysis of the biquaternions as a geometric algebra requires further work". The corpus records the grades, the outer product and the duality; it claims no interpretation of a general product beyond them.

## The Matrix Model

An explicit matrix model makes the invariants computable.

**Theorem.** The assignment

$$
e_k\longmapsto-i\sigma_k \qquad (k=1,2,3), \qquad i\longmapsto iI, \qquad e_0\longmapsto I,
$$

where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices and $I$ the identity, extends to an isomorphism $\Phi\colon\mathbb{B}\to M_2(\mathbb{C})$. With it, the norm form is the determinant:

$$
\det\Phi(\tilde Q)=N(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2.
$$

Consequently an element $\tilde Q\in\mathbb{B}$ is invertible if and only if $N(\tilde Q)\neq0$, and the zero divisors of $\mathbb{B}$ are exactly the nonzero elements with $N(\tilde Q)=0$. The model is the one, where the same isomorphism fixes $\Phi(e_k)=-i\sigma_k$ and $\Phi(i\tilde Q)=i\Phi(\tilde Q)$.

**Proof.** The images of $e_k$ satisfy $-i\sigma_k$ squared $=-I$ and anticommute pairwise, and their products reproduce the quaternion multiplication: with the convention $e_1e_2=e_3$ of the category,

$$
\Phi(e_1)\Phi(e_2)=(-i\sigma_1)(-i\sigma_2)=-\sigma_1\sigma_2=-i\sigma_3=\Phi(e_3),
$$

and cyclically. The image of $i$ is central with square $-I$, the image of $e_0$ is $I$, and the images generate $M_2(\mathbb{C})$, so $\Phi$ is an isomorphism. For the determinant, write $\Phi(\tilde Q)=Q_0I-iQ_1\sigma_1-iQ_2\sigma_2-iQ_3\sigma_3$ and expand:

$$
\Phi(\tilde Q)=\begin{pmatrix}Q_0-iQ_3 & -iQ_1-Q_2\\ -iQ_1+Q_2 & Q_0+iQ_3\end{pmatrix}.
$$

Then $\det\Phi(\tilde Q)=(Q_0-iQ_3)(Q_0+iQ_3)-(-iQ_1-Q_2)(-iQ_1+Q_2)=Q_0^2+Q_3^2+Q_1^2+Q_2^2=\sum_\mu Q_\mu^2=N(\tilde Q)$. The invertibility criterion and the description of the zero divisors follow from the fact that a square matrix over a field is invertible exactly when its determinant is nonzero. $\square$

**Corollary.** The norm form is the reduced norm of the central simple complex algebra $\mathbb{B}\cong M_2(\mathbb{C})$, and its vanishing set, the isotropic cone of $N$, is the determinantal quadric of the algebra. The zero divisors of $\mathbb{B}$ are precisely the nonzero elements of that cone.

**Example.** The element $\tilde Q=e_0-ie_3$ has $N=1-1=0$; its matrix is $\Phi(\tilde Q)=I-\sigma_3=\operatorname{diag}(0,2)$, which is singular, so $\tilde Q$ is a zero divisor. The idempotent $p=\tfrac12(e_0+ie_3)$ also has $N=\tfrac14-\tfrac14=0$, its matrix is $\Phi(p)=\tfrac12(I+\sigma_3)=\operatorname{diag}(1,0)$, and the complementary idempotent $\tfrac12(e_0-ie_3)$ has matrix $\operatorname{diag}(0,1)$. Their product vanishes, exhibiting the zero divisor $p$ with $(1-p)p=0$; consistently with the determinant formula, every idempotent other than $e_0$ has vanishing norm, since its matrix has rank one.

## Idempotents and Minimal Ideals

**Definition.** An element $p\in\mathbb{B}$ is an **idempotent** if $p^2=p$. It is **minimal** if $pAp=\mathbb{C}p$ as a complex algebra. A **minimal left ideal** of $\mathbb{B}$ is a left ideal that contains no proper nonzero left ideal. The idempotent structure of $\mathbb{B}$ is standard, and it is recalled here only to identify the module in the Clifford model.

**Theorem.** The idempotents $p=\tfrac12(e_0+ie_3)$ and $q=\tfrac12(e_0-ie_3)$ are orthogonal, $p+q=e_0$ and $pq=0$, and each is minimal. The left ideal $\mathbb{B}p$ is minimal of complex dimension two, and the map

$$
\mathbb{B}p\longrightarrow\mathbb{C}^2, \qquad x\longmapsto x\binom{1}{0},
$$

is an isomorphism of left $\mathbb{B}$-modules when $\mathbb{B}p$ is viewed in the matrix model.

**Proof.** Since $ie_3$ has square $+1$ and commutes with itself, the elements $\tfrac12(1\pm ie_3)$ are the standard orthogonal idempotents of an involution. In the matrix model $\Phi(ie_3)=\sigma_3$ and hence $\Phi(p)=\tfrac12(I+\sigma_3)=\operatorname{diag}(1,0)$ and $\Phi(q)=\operatorname{diag}(0,1)$, so $p$ and $q$ are the two rank-one diagonal projections; a rank-one projection is minimal, and $M_2(\mathbb{C})p$ is its two-dimensional column space, the first column. The map is the identification of that column space with $\mathbb{C}^2$. $\square$

**Remark.** The idempotents are not unique; every rank-one projection of $M_2(\mathbb{C})$ is an idempotent, and they are parametrised by the projective line $\mathbb{CP}^1$. The two diagonal ones are the coordinate choices, and any two minimal idempotents are conjugate by a unit. The minimal left ideals are all isomorphic to the defining module $\mathbb{C}^2$, so the choice of $p$ does not change the module up to isomorphism; the choice is a choice of basis, not of structure.

## The Peirce Decomposition

**Theorem.** Let $p$ be an idempotent of $\mathbb{B}$ with $q=e_0-p$. Then $\mathbb{B}$ decomposes as a direct sum of complex vector spaces

$$
\mathbb{B}=p\mathbb{B}p\oplus p\mathbb{B}q\oplus q\mathbb{B}p\oplus q\mathbb{B}q,
$$

with $p\mathbb{B}p\cong\mathbb{C}p$ when $p$ is minimal, and the four summands have complex dimensions $1,1,1,1$. The left ideal $\mathbb{B}p$ decomposes as $\mathbb{B}p=p\mathbb{B}p\oplus q\mathbb{B}p$, and the right ideal decomposes as $p\mathbb{B}=p\mathbb{B}p\oplus p\mathbb{B}q$.

**Proof.** Write every $x$ as $x=pxq+pxp+qxp+qxq$ using $p+q=1$; the four terms are independent and lie in the four stated subspaces, and the expansion is unique. Since $p\mathbb{B}p=\mathbb{C}p$ for minimal $p$ and the total dimension is four, the remaining three summands are one-dimensional. The decomposition of the left ideal is the statement that the terms with $q$ on the left vanish. $\square$

**Remark.** The Peirce decomposition is the algebraic skeleton of the matrix structure: the four corners of $2\times2$ matrices, of dimensions $1,1,1,1$ over $\mathbb{C}$, correspond to the four blocks, and the off-diagonal blocks are the spaces of intertwiners between the minimal left ideal and its conjugate. In the biquaternion application, the diagonal blocks are the two scalar sectors and the off-diagonal blocks carry the intertwiners between the two idempotents; the module structure of the algebra is read from this decomposition. The decomposition itself is treated elsewhere, where the Peirce spaces are computed from the multiplication table; it is recorded here because the Clifford description uses the same four idempotents.

**The two minimal ideals.** The algebra $\mathbb{B}$ has, up to isomorphism, one simple module, but it has many minimal left ideals, one for each minimal idempotent. The two diagonal choices give the two columns of the matrix model, $\mathbb{B}p$ and $\mathbb{B}q$, which are isomorphic as abstract modules but distinguished by the idempotent. Their direct sum is $\mathbb{B}p\oplus\mathbb{B}q$, which is isomorphic to $\mathbb{B}$ as a left module, the regular representation being the direct sum of two copies of the simple module; $\mathbb{B}$ itself is free of rank one over itself, with $e_0$ a basis, so the two summands are the simple module written twice rather than a free module of rank two. The isomorphism classes of minimal left ideals are classified by the idempotents up to conjugacy, which is to say that there is exactly one class.

## Zero Divisors and the Norm Cone

**Theorem.** An element $\tilde Q\in\mathbb{B}$ is a zero divisor if and only if $\tilde Q\neq0$ and $N(\tilde Q)=0$. The set of zero divisors is the isotropic cone of the complex quadratic form $N$, a complex hypersurface of complex dimension three in $\mathbb{B}\cong\mathbb{C}^4$ defined by one non-degenerate quadratic equation, equivalently a real cone of real dimension six in $\mathbb{B}\cong\mathbb{R}^8$.

**Proof.** The element $\tilde Q$ is a zero divisor exactly when it is not a unit, and in $M_2(\mathbb{C})$ this is exactly the vanishing of the determinant, which by the matrix model is $N(\tilde Q)$. The hypersurface $\{N=0\}$ in $\mathbb{C}^4$ is defined by one non-degenerate quadratic equation, so it has complex dimension three and is singular at the origin; removing the origin gives a cone over a smooth quadric in $\mathbb{CP}^3$, of real dimension six. $\square$

**Corollary.** The zero divisors are exactly the elements of rank one or rank zero in the matrix model; the rank-one elements form the smooth part of the cone, and the rank-zero element is the origin. Every nonzero zero divisor $\tilde Q$ determines a unique minimal left ideal, namely $\mathbb{B}\tilde Q$ up to the choice of the complementary idempotent, and a unique minimal right ideal. In particular the zero divisors are not a defect of the algebra but the geometric manifestation of the two-dimensional module: an element is a zero divisor precisely when it is not invertible on the defining module.

**Remark.** The norm form $N$ is complex-valued, so its vanishing is a complex-analytic condition of codimension one; its real part and its imaginary part are both real quadratic forms on $\mathbb{R}^8$ of signature $(4,4)$. The Hermitian form $\tilde Q\tilde Q^\dagger$, by contrast, is positive definite in its scalar part and never vanishes on nonzero elements; the two forms are the indefinite and the definite shadows of the same algebra, and the zero divisors belong to the indefinite one.

## Ideals and the Structure of the Algebra

**Theorem.** The algebra $\mathbb{B}$ is central simple over $\mathbb{C}$: its center is $\mathbb{C}$ and its only two-sided ideals are $\{0\}$ and $\mathbb{B}$. Its minimal left ideals are the spaces $\mathbb{B}p$ for minimal idempotents $p$, all of complex dimension two and all isomorphic to the defining module $\mathbb{C}^2$ of $M_2(\mathbb{C})$.

**Proof.** Central simplicity is Wedderburn's theorem for $M_2(\mathbb{C})$. A nonzero two-sided ideal contains a nonzero element, hence a nonzero minimal left ideal, and by conjugating by units contains all minimal left ideals; since their sum is $\mathbb{B}$, the ideal is everything. The minimal left ideals have the stated form because $M_2(\mathbb{C})$ is a full matrix algebra. $\square$

**Remark.** The absence of nontrivial two-sided ideals is the statement that $\mathbb{B}$ has no quotient algebras other than $\mathbb{C}$ and $\mathbb{B}$ itself; this is why the algebra is a complete building block and why its module theory is so simple. In the Clifford language it is the statement that $\mathrm{Cl}_{3,0}$ is simple as a real algebra of complex type; in the matrix language it is Wedderburn for a full matrix algebra. The contrast is with the Clifford algebras whose volume element can be rescaled to square $+1$, where $\tfrac12(1\pm\omega)$ are central idempotents and the algebra has two factors: for the complexification of $\mathrm{Cl}_{3,0}$ one has $\mathbb{C}\mathrm{l}_3=M_2(\mathbb{C})\times M_2(\mathbb{C})$, and in the real case $\mathrm{Cl}_{0,3}\cong\mathbb{H}\oplus\mathbb{H}$. This is the structural distinction between the biquaternion algebra and the algebras of the neighbouring entries, and it turns on the sign $\omega^2=-1$ in $\mathrm{Cl}_{3,0}$, not on the parity of the dimension.

## The Defining Module

What the Clifford identification adds to the module is the description of $S$ as a Clifford module; the module-theoretic statement belongs to *The Defining Module of the Biquaternion Algebra* and the spinor statement.

**Theorem.** The minimal left ideal $\mathbb{B}p$ with $p=\tfrac12(e_0+ie_3)$ is a complex vector space of dimension two, and it is the unique simple left $\mathbb{B}$-module up to isomorphism. The action of $\mathbb{B}$ on it is the defining representation of $M_2(\mathbb{C})$.

**Proof.** This is the module theory of the previous theorem: a full matrix algebra has a unique simple module, the column space, of dimension equal to the size of the matrix. The identification with $\mathbb{C}^2$ is the matrix model, and the action is left multiplication. $\square$

**Corollary.** Every finite-dimensional $\mathbb{B}$-module is a direct sum of copies of $\mathbb{C}^2$, so the module category of $\mathbb{B}$ is the category of complex vector spaces. The further module-theoretic consequences — that $\mathbb{B}$ is free of rank one over itself, the decomposition $\mathbb{B}=S\oplus S$, and the fact that the simple module $S$ is projective but not free, so that projectivity does not imply freeness over $\mathbb{B}$ — are established in *The Defining Module of the Biquaternion Algebra* and are not repeated here.

**Remark.** The defining module is the spinor module of the Clifford algebra. For $\mathrm{Cl}_{3,0}$ the volume element has square $-1$, so the module has no real chirality splitting: the spinor module $S$ is irreducible of real dimension four, and it is the module $\mathbb{B}p$ regarded as a real vector space. Chirality appears only after complexification, where $S\otimes_{\mathbb{R}}\mathbb{C}\cong S_+\oplus S_-$ splits into the two chiral halves and these correspond to the two factors of $\mathbb{C}\mathrm{l}_3=M_2(\mathbb{C})\times M_2(\mathbb{C})$; the two minimal left ideals $\mathbb{B}p$ and $\mathbb{B}q$ of the matrix model are isomorphic to one another, and each of them complexifies to the sum $S_+\oplus S_-$; neither is a chiral half. The identification of the spinor module with the defining module of $\mathbb{B}$ is the bridge between the Clifford layer and the applications, and it is treated.

## Summary

The biquaternion algebra is a Clifford algebra in several compatible ways. It is the even subalgebra $\mathbb{B}\cong\mathrm{Cl}_{3,1}^{+}$ of the real Clifford algebra of signature $(3,1)$, and under the competing labelling $\mathrm{Cl}_{1,3}$ the even part is the same algebra while the full algebras differ, $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ and $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$. As a real algebra $\mathbb{B}$ is also $\mathrm{Cl}_{3,0}$, generated by three anticommuting elements of square $+1$ (the bivectors $\Gamma_k\Gamma_4$), and there the isomorphism is $\gamma_k\mapsto ie_k$; as a complex algebra it is $\mathbb{C}\mathrm{l}_2=M_2(\mathbb{C})$, central simple of complex dimension four; and it is the complexification $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ of the quaternions by a central scalar. The volume element $\Omega=\Gamma_1\Gamma_2\Gamma_3\Gamma_4$ is central in the even part, has square $-1$, and together with $e_0$ spans the center; the volume element of the $\mathrm{Cl}_{3,0}$ description, $\omega=\gamma_1\gamma_2\gamma_3$ on three generators, corresponds to the same central scalar imaginary $i$.

In the matrix model $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI$, the norm form is the determinant, $\det\Phi(\tilde Q)=N(\tilde Q)=\sum_\mu Q_\mu^2$, so that the invertible elements are those with $N\neq0$ and the zero divisors are the nonzero elements of the norm cone $\{N=0\}$.

The diagonal idempotents $p=\tfrac12(e_0+ie_3)$ and $q=\tfrac12(e_0-ie_3)$ are orthogonal and minimal, with $p+q=e_0$; the minimal left ideals $\mathbb{B}p$ and $\mathbb{B}q$ have complex dimension two and are the defining module $\mathbb{C}^2$ of $M_2(\mathbb{C})$, realised as the first and the second column of the matrix model. The Peirce decomposition $\mathbb{B}=p\mathbb{B}p\oplus p\mathbb{B}q\oplus q\mathbb{B}p\oplus q\mathbb{B}q$ has four one-dimensional complex summands, the four blocks of the matrix model. The algebra is central simple, so it has no nontrivial two-sided ideals and its module category is that of complex vector spaces, with a unique simple module.

The antisymmetric part of the product is the outer product, $\tfrac12(pq-qp)=V(p)\times V(q)$, so it depends only on the vector parts and holds for every pair of biquaternions. Its output names the grades: the product of two vectors is a bivector, of two bivectors a bivector, and of a vector with a bivector a vector, where the geometric vectors are the imaginary pure quaternions and the bivectors the real pure ones. The quaternion scalar/vector terminology therefore mislabels the grades — Suter's "a quaternion is a scalar plus a bivector" is right, and the axial and polar language of physics has added to the confusion — while the corpus's two usages agree once the identification $\gamma_k\mapsto ie_k$ is kept in view. Multiplication by the pseudoscalar is duality, mapping bivectors to vectors and scalars to pseudoscalars; the physics articles write the Hodge dual with a sign convention as $\tilde F_\star=-i\tilde F$. The paper is explicit that a deeper geometric reading of the full product requires further work, and the article claims no more than the four grades, the outer product and the duality.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathrm{Cl}_{3,1},\ \mathrm{Cl}_{1,3}$ | Real Clifford algebras of the two signature labellings; $\mathbb{B}\cong\mathrm{Cl}_{3,1}^{+}\cong\mathrm{Cl}_{1,3}^{+}$ |
| $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R}),\ \mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ | The full algebras; distinct over $\mathbb{R}$, same even part |
| $\gamma_k\mapsto ie_k$ | Isomorphism $\mathrm{Cl}_{3,0}\to\mathbb{B}$ |
| $\omega=\gamma_1\gamma_2\gamma_3\mapsto i$ | Volume element of $\mathrm{Cl}_{3,0}$, central, $\omega^2=-1$ |
| $\Omega=\Gamma_1\Gamma_2\Gamma_3\Gamma_4\,(\Omega^2=-1)$ | Volume element of $\mathrm{Cl}_{3,1}$, central in the even part |
| $\Phi$ | Matrix isomorphism $\mathbb{B}\to M_2(\mathbb{C})$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI$ |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}=\sum_\mu Q_\mu^2$ | Norm form, equal to $\det\Phi(\tilde Q)$ |
| $\tilde Q\tilde Q^\dagger$ | Hermitian form, positive definite in its scalar part |
| $S(\tilde Q)$, $V(\tilde Q)$ | Scalar and vector parts; geometric names: scalar (real scalar), bivector (real pure), vector (imaginary pure), pseudoscalar (imaginary scalar) |
| $\tfrac12(pq-qp)=V(p)\times V(q)$ | Outer product; the cross product of the vector parts, for any pair |
| $\{N=0\}$ | Isotropic cone of the norm form; the zero divisors |
| $p=\tfrac12(e_0+ie_3)$, $q=e_0-p$ | Orthogonal minimal idempotents |
| $\mathbb{B}=p\mathbb{B}p\oplus p\mathbb{B}q\oplus q\mathbb{B}p\oplus q\mathbb{B}q$ | Peirce decomposition |
| $\mathbb{B}p\cong\mathbb{C}^2$ | Minimal left ideal, the defining module |
| $\sigma_1,\sigma_2,\sigma_3$ | Pauli matrices |
| $\mathbb{C}\mathrm{l}_2=M_2(\mathbb{C})$ | Complex Clifford algebra, the complex-algebra identification |





## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the identification of the biquaternion algebra with the even part of $\mathrm{Cl}_{3,1}$ (equivalently with $\mathrm{Cl}_{3,0}$) and the volume element.
- Richard Brauer and Hermann Weyl, "Spinors in $n$ dimensions," *American Journal of Mathematics* **57** (1935), 425–449, for the matrix models of the Clifford algebras and the volume element.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for the reduced norm of a central simple algebra and its relation to the determinant.
- Theodore Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the Peirce decomposition, minimal left ideals and Wedderburn's theorem.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the structure of the low-dimensional Clifford algebras as matrix algebras, in particular $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ and $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the outer product as the cross product of the vector parts and for the correspondence between the four geometric grades and the biquaternion components.