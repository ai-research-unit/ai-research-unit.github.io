# __The Exponential of the Traceless Anti-Hermitian Part: $SU(4)$ and the Rotors of the Six-Space__

## Introduction

**The two linear conditions that single out $\mathfrak{su}(4)$ inside $M_4(\mathbb{C})$, traceless and anti-Hermitian, are the two conditions that single out $\mathfrak{su}(2)$ inside $M_2(\mathbb{C})$ at order two, and they do the same work at order four: the trace removes the scale and the phase, the anti-Hermitian condition removes the stretch, and the exponential of what remains is a group of rotors.** The group is $SU(4)$, of real dimension fifteen. Its action on the bivector space is the rotation group of a six-dimensional real space, so that one rotation of that space has two preimages in $SU(4)$, exactly as one rotation of three-space has two preimages in $SU(2)$.

**The difference from order two is the count.** At order two the exponentiated subspace has dimension three and its three parameters are three angles. At order four there are fifteen parameters and only three of them are angles. Three act as the independent angles of six-space; the other twelve choose the planes those angles turn, and each of the twelve turns one coordinate plane of $\mathbb{C}^4$ at a time, fixing the other two coordinates.

**The article** defines the subspace and splits it into the torus and the twelve root families, proves the closed form, the surjectivity and the compactness of the exponential, computes the action of the fifteen on the carrier, on the bivector space and on the symmetric square, proves $\mathfrak{su}(4)\cong\mathfrak{so}(6)$ and reads the fifteen as three angles plus twelve planes, describes the adjoint orbits and the chiral split $15=7+8$, and states what the two conditions forbid.

**The subspace** is *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*; the exponential of the whole algebra is *The Exponential and the Lie Group of $M_4(\mathbb{C})$*; the form on the bivector space is *The Antisymmetric Sector, the Pfaffian and the Klein Quadric of $M_4(\mathbb{C})$*; the rotations of four-space and their two angles are *Simple and Non-Simple Rotations at $n=4$: the Two Angles and the Isoclinic Families*; the order-two statement of the same theorem is *The Exponential of the Traceless Anti-Hermitian Part: Determinant One, Unitarity and the Rotation*.

## The Traceless Anti-Hermitian Part

**Definition.** The **traceless anti-Hermitian part** of $M_4(\mathbb{C})$ is

$$
\mathfrak{su}(4)=\{K\in M_4(\mathbb{C}):K^*=-K,\ \operatorname{tr}K=0\},
$$

with $K^*=\bar K^{\mathsf T}$. It is a real subspace, closed under the commutator, of real dimension $15$ and rank $3$. Its elements are the **generators**; its exponential is the subject of the next section.

**Proposition (the dimension).** $\dim_\mathbb{R}M_4(\mathbb{C})=32$, $\dim_\mathbb{R}\mathfrak{u}(4)=16$, $\dim_\mathbb{R}\mathfrak{su}(4)=15$.

**Proof.** The condition $K^*=-K$ is a real-linear condition: it fixes the diagonal entries to be purely imaginary, four real parameters, and pairs the twelve off-diagonal entries into six conjugate pairs, twelve real parameters more. So $\mathfrak{u}(4)$ has real dimension $16$. The trace of an anti-Hermitian matrix is purely imaginary, so $\operatorname{tr}K=0$ is one further real condition, and $\dim\mathfrak{su}(4)=15$. The dimension of the whole algebra is $2\cdot16=32$.

**Proposition (the complexification).** $\mathfrak{su}(4)\otimes_\mathbb{R}\mathbb{C}=\mathfrak{sl}_4(\mathbb{C})$, and $\mathfrak{su}(4)$ is the compact real form of $\mathfrak{sl}_4$.

**Proof.** The traceless condition is complex-linear and the anti-Hermitian condition is not, so the complexification of the real subspace $\mathfrak{su}(4)$ is the complex subspace $\mathfrak{sl}_4$. The form $\operatorname{tr}(K^*K)=\sum_{ij}\lvert K_{ij}\rvert^2$ is positive definite on $\mathfrak{su}(4)$, so the real form is compact; a compact real form of a complex semisimple algebra is unique up to conjugacy.

**The two conditions read apart.** Traceless alone gives $\mathfrak{sl}_4$, of real dimension $30$: it removes the scalar $I$, that is, one complex parameter, the scale and the phase together. Anti-Hermitian alone gives $\mathfrak{u}(4)$, of real dimension $16$: it removes the traceless Hermitian part, which is the stretch. The intersection removes both, and what is left is the part of the algebra whose exponential neither scales nor changes phase.

**The complementary half.** The traceless Hermitian matrices $i\mathfrak{su}(4)=\{H:H^*=H,\operatorname{tr}H=0\}$ have the same real dimension $15$, and

$$
\mathfrak{sl}_4=\mathfrak{su}(4)\oplus i\,\mathfrak{su}(4),
$$

the Cartan decomposition of $\mathfrak{sl}_4$. The first summand is the compact half and the second is the stretch half. The split is the one the whole article turns on: the exponential of the first is unitary, the exponential of the second is Hermitian and positive definite.

**The basis.** The subspace has the following fifteen elements, and they are the ones the article uses throughout.

$$
H_k=i\,(E_{kk}-E_{44}),\quad k=1,2,3,
$$

$$
A_{ij}=i\,(E_{ij}+E_{ji}),\qquad B_{ij}=E_{ij}-E_{ji},\qquad 1\le i<j\le4 .
$$

The three $H_k$ are diagonal and traceless; the twelve $A_{ij}$ and $B_{ij}$ have a single coordinate plane each. The fifteen are linearly independent over $\mathbb{R}$, and every element of $\mathfrak{su}(4)$ is a unique real combination of them.

## The Exponential onto $SU(4)$

**Definition.** $SU(4)=\{U\in M_4(\mathbb{C}):U^*U=I,\ \det U=1\}$, the special unitary group, of real dimension $15$ and compact.

**Proposition (the image is unitary and of determinant one).** For every $K\in\mathfrak{su}(4)$, the matrix $U=e^{K}$ satisfies $U^*U=I$ and $\det U=1$.

**Proof.** Since $K^*=-K$, the conjugate transpose of the exponential is $e^{K^*}=e^{-K}=(e^{K})^{-1}$, so $U$ is unitary. The determinant is $\det e^{K}=e^{\operatorname{tr}K}=e^{0}=1$.

**Proposition (the image is all of $SU(4)$).** The exponential maps $\mathfrak{su}(4)$ onto $SU(4)$.

**Proof.** A unitary matrix is normal, so by the spectral theorem it is $U=V\operatorname{diag}(e^{i\theta_1},\dots,e^{i\theta_4})V^*$ with $V$ unitary and $\theta_a$ real. The condition $\det U=1$ reads $\sum_a\theta_a\in2\pi\mathbb{Z}$. Put $\mu_a=\theta_a-\frac{1}{4}\sum_b\theta_b$; then $\sum_a\mu_a=0$, the numbers $\mu_a$ are real, and

$$
U=V\operatorname{diag}(e^{i\mu_1},\dots,e^{i\mu_4})V^*\cdot e^{\frac{i}{4}\sum_b\theta_b}I
=V\,e^{i\operatorname{diag}(\mu_1,\dots,\mu_4)}\,V^*,
$$

because the scalar $e^{\frac{i}{4}\sum\theta_b}$ is a fourth root of unity times a phase and is absorbed into the $\mu_a$ without changing the sum. The exponent $i\operatorname{diag}(\mu)$ is anti-Hermitian and traceless, and $V(i\operatorname{diag}\mu)V^*$ is its conjugate, which is again in $\mathfrak{su}(4)$. So $U$ is the exponential of an element of the subspace.

**Proposition (boundedness).** Every $U\in SU(4)$ has all singular values equal to $1$, so $\lVert U\rVert=1$ and $SU(4)$ is closed and bounded in $M_4(\mathbb{C})$.

**Proof.** The singular values of $U$ are the square roots of the eigenvalues of $U^*U=I$, which are all $1$.

**Proposition (the fibre over the identity).** The exponential is not injective on $\mathfrak{su}(4)$. Its fibre over $I$ is the set of traceless anti-Hermitian $K$ whose eigenvalues lie in $2\pi i\mathbb{Z}$.

**Proof.** If $K=V\operatorname{diag}(i\theta_a)V^*$ with $\theta_a\in2\pi\mathbb{Z}$ then $e^{K}=I$; conversely $e^{K}=I$ forces every eigenvalue of $e^{K}$ to be $1$, and the eigenvalues of $e^{K}$ are $e^{\eta}$ for $\eta$ an eigenvalue of $K$, so each $\eta\in2\pi i\mathbb{Z}$. The trace condition removes one of the four, so the fibre is a union of families, not a point.

**Proposition (the closed form of a root family).** Let $K=t\,(a\,A_{ij}+b\,B_{ij})$ with $t\ge0$ real and $a^2+b^2=1$, and let $\alpha=ia+b$, so that $\lvert\alpha\rvert=1$. Then

$$
e^{K}=\begin{pmatrix}\cos t & \alpha\sin t\\ -\bar\alpha\sin t & \cos t\end{pmatrix}\oplus I_2,
$$

the block on the coordinates $i,j$ and the identity on the other two coordinates. The eigenvalues on the block are $e^{\pm it}$, the determinant is $1$, and the angle of the block is $t$.

**Proof.** On the plane $\{i,j\}$ the generator is $K=t\begin{pmatrix}0&\alpha\\-\bar\alpha&0\end{pmatrix}$, because $A_{ij}$ and $B_{ij}$ have the entries $i$ in the upper corner and $i$ and $-1$ in the lower, and $ia+b=\alpha$. The square of that block is $-t^2I$ since $\lvert\alpha\rvert^2=1$, so the exponential is $\cos t\,I+\sin t\,K/t$, which is the display; the eigenvalues are $\pm it$ and the determinant is $\cos^2t+\lvert\alpha\rvert^2\sin^2t=1$. The two other coordinates are untouched because the generator vanishes there.

**Proposition (the bounded exponential of the traceless part of $SL_4$).** Every $A\in SL_4(\mathbb{C})$ has a unique factorisation $A=e^{K}e^{H}$ with $K\in\mathfrak{su}(4)$ and $H$ traceless Hermitian, so that $SU(4)$ is the maximal compact subgroup of $SL_4(\mathbb{C})$ and the exponential of the traceless anti-Hermitian part is exactly the compact factor of $SL_4$.

**Proof.** The polar decomposition writes $A=UP$ with $U$ unitary and $P$ positive definite Hermitian; $\det A=1$ forces $\det U\cdot\det P=1$, and both factors are positive reals in modulus on the left and phases on the right, so $\det U=1$ and $\det P=1$. Then $H=\log P$ is Hermitian with $\operatorname{tr}H=0$ and $U=e^{K}$ with $K$ traceless anti-Hermitian by the previous proposition. Uniqueness is that of the polar decomposition.

**The count of the compact half.** The subspace contributes the whole compactness of $SL_4$: the fifteen parameters of $SU(4)$ against the fifteen of the stretch half, and $30=15+15$.

## The Fifteen Generators: the Torus and the Twelve Roots

**The split $3+12$.** Three generators are the diagonal ones $H_k$; the other twelve come in six pairs, one pair per coordinate plane $\{i,j\}$ of $\mathbb{C}^4$. The three are the Cartan part and the twelve are the root part.

**Proposition (the root property).** For $\mu\in\mathbb{R}^4$ with $\sum_a\mu_a=0$, put $H=i\operatorname{diag}(\mu_1,\dots,\mu_4)$. Then

$$
[H,E_{ij}]=i(\mu_i-\mu_j)\,E_{ij},
$$

so the twelve off-diagonal matrix units are eigenvectors of the Cartan with the twelve roots $\mu_i-\mu_j$, $i\ne j$, and the six pairs correspond to the six pairs of opposite roots.

**Proof.** The commutator of two diagonal matrices is diagonal with entries $\mu_i-\mu_j$ on the entry $ij$; the factor $i$ comes from $H=i\operatorname{diag}\mu$, and the two elements $A_{ij},B_{ij}$ are the real and the imaginary parts of $iE_{ij}$ and $E_{ij}$.

**The torus.** The exponentials of the three $H_k$ are the diagonal matrices $\operatorname{diag}(e^{i\mu_1},\dots,e^{i\mu_4})$ with $\sum\mu_a=0$, which form a three-dimensional torus $T^3$; it is a maximal torus of $SU(4)$, and the Weyl group is the permutation group $S_4$ of the four coordinates.

**The six $\mathfrak{su}(2)$'s and the overcount.** Each pair $\{i,j\}$ together with its commutator spans an $\mathfrak{su}(2)$ acting on that plane and fixing the other two coordinates. Six copies of three generators make eighteen elements, but their real span has dimension $15$: the six copies overlap on the Cartan. The fifteen is the count of independent generators, not the count of planes.

| family | number | generators | support |
|---|---|---|---|
| Cartan | $3$ | $i(E_{kk}-E_{44})$ | all four coordinates |
| root family $\{i,j\}$ | $12$ | $i(E_{ij}+E_{ji})$, $E_{ij}-E_{ji}$ | the plane $\{i,j\}$ only |

## The Action on the Carrier $\mathbb{C}^4$

**The root family acts on one plane.** By the closed form, the exponential of a root family is the identity on the two complementary coordinates and a unitary block on the plane.

**Proposition (the block turn is isoclinic).** Read on the four real coordinates of the plane, the block $e^{K}$ of a root family is a rotation with two angles, and the two angles are equal to $t$.

**Proof.** The eigenvalues of the block are $e^{\pm it}$, so as a real four-dimensional rotation the block has the eigenvalue pairs $e^{\pm it}$ and $e^{\pm it}$, which is the definition of two equal angles. In the classification of *Simple and Non-Simple Rotations at $n=4$: the Two Angles and the Isoclinic Families* this is the isoclinic case, and the block is one of the two isoclinic families of that article.

**The Cartan part acts by phases.** The exponential of $i\operatorname{diag}(\mu)$ multiplies the coordinate $a$ by $e^{i\mu_a t}$, with the product of the four phases equal to $1$.

**Proposition (transitivity on the sphere).** $SU(4)$ acts transitively on the unit sphere $S^{7}\subset\mathbb{C}^4$, with stabiliser $SU(3)$, so that

$$
S^{7}=SU(4)/SU(3).
$$

**Proof.** Given a unit vector $v$, choose a unitary $V$ with $Vv=e_1$; if $\det V=e^{i\phi}$, replace $V$ by $\operatorname{diag}(e^{-i\phi},1,1,1)V$, which still sends $v$ to a unit vector and has determinant $1$, then correct by a diagonal element of $SU(4)$ sending that vector to $e_1$. The stabiliser of $e_1$ is the set of elements $U$ with $Ue_1=e_1$, which is $SU(3)$ in the last three coordinates.

**The spectrum of a general element.** Every $U\in SU(4)$ has the eigenvalues $e^{i\theta_1},\dots,e^{i\theta_4}$ with $\sum\theta_a\in2\pi\mathbb{Z}$; the conjugacy classes are the level sets of the four phases subject to that constraint, of dimension $3$, and the generic class has dimension $12$.

## The Action on the Bivector Space: $\mathfrak{su}(4)\cong\mathfrak{so}(6)$

**The second exterior power.** On the six-dimensional space $\Lambda^{2}\mathbb{C}^{4}$ with basis $e_i\wedge e_j$, $i<j$, a matrix $U$ acts by

$$
\Lambda^{2}U\,(e_i\wedge e_j)=\sum_{k<l}\det U\!\begin{pmatrix}i&j\\k&l\end{pmatrix}e_k\wedge e_l,
$$

the six by six matrix of the two by two minors, the Plücker matrix.

**Proposition (functoriality and the kernel).** $\Lambda^{2}(UV)=\Lambda^{2}U\,\Lambda^{2}V$ and $\Lambda^{2}(-U)=\Lambda^{2}U$, because the minors are quadratic in the entries. So $\Lambda^{2}$ is a homomorphism $SU(4)\to GL_6(\mathbb{C})$ whose kernel contains $\{\pm I\}$.

**Proposition (the algebra map is injective).** The derivative at the identity sends $K\in\mathfrak{su}(4)$ to the six by six matrix $(K\wedge)$ with the entries $\delta_{ik}K_{jl}-\delta_{il}K_{jk}-\delta_{jk}K_{il}+\delta_{jl}K_{ik}$, and this map is injective on $\mathfrak{su}(4)$.

**Proof.** The derivative of a determinant in the direction $K$ is the trace of $K$ on the two by two block, which is the displayed expression. If $K\wedge=0$ then for every pair $\{i,j\}$ the restriction of $K$ to that plane vanishes, so all the two by two principal minors of $K$ vanish; the off-diagonal entries vanish from the pairs and the diagonal differences vanish from the pairs, so $K$ is diagonal with all entries equal, and tracelessness makes it zero.

**Proposition (the image is $\mathfrak{so}(6)$).** Let $\langle\cdot,\cdot\rangle$ be the symmetric form of *The Antisymmetric Sector, the Pfaffian and the Klein Quadric of $M_4(\mathbb{C})$*, defined by $\omega\wedge\eta=\langle\omega,*\eta\rangle\,e_1\wedge e_2\wedge e_3\wedge e_4$. Then every image $K\wedge$ satisfies

$$
(K\wedge)^{\mathsf T}Q+Q\,(K\wedge)=0,\qquad (K\wedge)^*+(K\wedge)=0,
$$

with the matrix $Q$ of $\langle\cdot,\cdot\rangle$ and the standard Hermitian form of $\Lambda^2\mathbb{C}^4$. The space of six by six matrices satisfying both conditions has real dimension $15$, so the image is exactly that space, and

$$
\mathfrak{su}(4)\cong\mathfrak{so}(6,\mathbb{C}),\qquad \Lambda^{2}\mathfrak{su}(4)=\mathfrak{so}(6,\mathbb{C})\cap\mathfrak{u}(6)=\mathfrak{so}(6).
$$

**Proof.** The antisymmetry for $Q$ is the invariance of $\langle\cdot,\cdot\rangle$ under $\Lambda^{2}U$, differentiated at the identity; the anti-Hermitian condition is the unitarity of $\Lambda^{2}U$ differentiated at the identity, since $\Lambda^2$ of a unitary matrix is unitary for the induced Hermitian form. On the complexified side: $\Lambda^{2}$ is an injective homomorphism of Lie algebras from $\mathfrak{sl}_4$ onto a subspace of $\mathfrak{so}(6,\mathbb{C})$, both of complex dimension $15$, so the image is the whole of $\mathfrak{so}(6,\mathbb{C})$. The anti-Hermitian elements of $\mathfrak{so}(6,\mathbb{C})$ form a real form of real dimension $15$, and it is compact, the anti-Hermitian matrices being closed and bounded; the image of $\mathfrak{su}(4)$ lies in it by the second displayed condition and has real dimension $15$ by injectivity, so the two agree.

**Theorem (the group level).** $\Lambda^{2}$ induces an isomorphism

$$
SU(4)/\{\pm I\}\;\cong\;SO(6),
$$

so $SU(4)$ is a double cover of the rotation group of a six-dimensional real space, and its elements are the rotors of that space: two rotors to one rotation.

**Proof.** The image is connected, compact and of dimension $15$, and lies in $SO(6)$, which is connected of dimension $15$; so the image is all of $SO(6)$. For the kernel: if $\Lambda^{2}U=I$ then $Uu\wedge Uv=u\wedge v$ for all $u,v$, so $U$ carries every two-plane into itself. Taking the planes $\langle u,v\rangle$ and $\langle u,w\rangle$ with $u,v,w$ independent, the vector $Uu$ lies in both and is therefore a multiple of $u$; so $U$ is scalar, $U=\zeta I$. Then $\Lambda^{2}U=\zeta^{2}I$, so $\zeta^{2}=1$ and $U=\pm I$. The preimages of a rotation are exactly two.

**The six-space is Euclidean only with the Hermitian reading.** The bilinear form $\langle\cdot,\cdot\rangle$ is neutral on the real bivectors, of signature $(3,3)$, as the values $\langle e_1\wedge e_2,e_1\wedge e_2\rangle=0$ and $\langle e_1\wedge e_2,e_3\wedge e_4\rangle=1$ show. What makes the image a group of Euclidean rotations is the Hermitian form, which the image also preserves: the compact real form of $\mathfrak{so}(6,\mathbb{C})$ is the intersection with $\mathfrak{u}(6)$, and the Euclidean six-space is the real form of $\Lambda^{2}\mathbb{C}^{4}$ on which the Hermitian form is real and definite.

**What each family does to the bivectors.** The next three statements are the action of the fifteen, family by family.

**The root family $\{i,j\}$.** The bivector $e_i\wedge e_j$ is fixed, because the block acts on the plane by a determinant one matrix and its own top exterior power is trivial on the two-dimensional plane; the complementary bivector $e_k\wedge e_l$ is fixed because the block is the identity there. The other four bivectors, those with one index in the plane and one outside, are turned with the angle $t$. The spectrum on $\Lambda^{2}\mathbb{C}^{4}$ is therefore $1,1,e^{\pm it},e^{\pm it}$.

**The Cartan part.** The bivector $e_i\wedge e_j$ is multiplied by $e^{i(\mu_i+\mu_j)t}$, so the six angles of the six-space are the six sums $\mu_i+\mu_j$, in three opposite pairs, and the torus of the six-space is the image of the torus $T^3$ of the carrier.

**A general element.** The six angles of six-space are $\pm\theta_1,\pm\theta_2,\pm\theta_3$, three independent angles, and the fifteen parameters of $SU(4)$ distribute as $3+12$: three angles, and twelve parameters that choose the three planes the angles turn. The twelve form the flag manifold $SO(6)/T^3$, of dimension $15-3=12$.

| family | angles on $\mathbb{R}^{6}$ | fixed bivectors |
|---|---|---|
| root $\{i,j\}$ | $0,0,\pm t,\pm t$ | $e_i\wedge e_j$ and $e_k\wedge e_l$ |
| Cartan | $\mu_i+\mu_j$, six phases | none, generically |
| general | $\pm\theta_1,\pm\theta_2,\pm\theta_3$ | none, generically |

**Boundary.** *Rotors Acting on the Bivector Space: the Adjoint Action at $n=4$* treats the six-dimensional image of $SU(2)\times SU(2)$, which is $\mathfrak{so}(4)$ of dimension six, and the split of the bivector space into the self-dual and anti-self-dual three-spaces. Here the image is the fifteen-dimensional $\mathfrak{so}(6)$ and the bivectors are the vector space it acts on, not the space of its adjoint. The two articles are one level apart: that one turns the bivector space by rotations of the carrier, this one turns it by rotors of the six-space.

## The Action on the Symmetric Square

**The third module.** $\operatorname{Sym}^{2}\mathbb{C}^{4}$ has dimension ten, with basis $e_ie_j$, $i\le j$, and $U$ acts by $e_ie_j\mapsto(Ue_i)(Ue_j)$, symmetrised.

**Proposition (the ten angles).** The exponential of $i\operatorname{diag}(\mu)$ multiplies $e_ie_j$ by $e^{i(\mu_i+\mu_j)t}$, so the ten angles of the symmetric square are the ten sums $\mu_i+\mu_j$ with $i\le j$.

**Proof.** The product $(Ue_i)(Ue_j)$ is multiplied by the product of the two phases.

**Proposition (a root family on the ten).** For a root family on the plane $\{i,j\}$ the symmetric square splits as $\operatorname{Sym}^{2}(\text{plane})\oplus(\text{plane}\otimes\text{complement})\oplus\operatorname{Sym}^{2}(\text{complement})$ of dimensions $3+4+3$, and the angles are $0,0,0,0,\pm t,\pm t,\pm2t$.

**Proof.** On the three symmetric products of the plane the block acts as its symmetric square, of dimension three with weights $2t,0,-2t$; on the four products with one index in the plane and one outside it acts as the block itself on each of two copies, giving $\pm t$ twice; on the three products of the complementary coordinates it acts trivially.

**The count $6+10=16$.** The antisymmetric and the symmetric squares of the carrier have dimensions $6$ and $10$ and sum to $16$, the dimension of $\mathbb{C}^4\otimes\mathbb{C}^4$. The fifteen is neither: it is the space of traceless endomorphisms of the carrier, and the two squares are its two modules of smallest dimension.

## The Adjoint Action and the Orbits

**The conjugation.** $SU(4)$ acts on its algebra by $K\mapsto UKU^*$, and on the algebra $M_4(\mathbb{C})$ by the same formula.

**Proposition (the orbits are the isospectral sets).** Two traceless anti-Hermitian matrices are conjugate under $SU(4)$ exactly when they have the same spectrum. The orbit through $i\operatorname{diag}(\mu)$ is the set of traceless anti-Hermitian matrices with the spectrum $\{i\mu_1,\dots,i\mu_4\}$, of dimension $12$ when the $\mu_a$ are distinct.

**Proof.** Conjugation preserves the spectrum. Conversely, two anti-Hermitian matrices with the same spectrum are diagonalised by unitaries $V$, $W$ with the same diagonal form, so $WV^*$ conjugates one into the other; correcting the determinant by a diagonal phase leaves the diagonal form unchanged. The orbit is $SU(4)$ modulo the centraliser of the diagonal element, which for distinct $\mu_a$ is the torus $T^3$ of the diagonal matrices, of dimension $3$; so the orbit has dimension $15-3=12$.

**The same twelve.** The twelve of the orbit and the twelve of the flag manifold of the previous section are the same count, read at the two ends: the angles are the three invariants of a conjugacy class, and the twelve are the parameters that fix the planes.

## The Chiral Reading: the Seven and the Eight

**The split of the carrier.** With the chiral planes $\{1,2\}$ and $\{3,4\}$, the traceless anti-Hermitian part splits by support into the block-diagonal part and the off-block part.

**Proposition (the dimensions $7+8$).** The block-diagonal traceless anti-Hermitian matrices have real dimension $7$ and form $\mathfrak{s}(\mathfrak{u}(2)\oplus\mathfrak{u}(2))=\mathfrak{su}(2)\oplus\mathfrak{su}(2)\oplus\mathfrak{u}(1)$; the off-block ones have real dimension $8$. Their sum is $15$.

**Proof.** The block part is $\mathfrak{u}(2)\oplus\mathfrak{u}(2)$ of dimension $8$ subject to the vanishing of the total trace, one real condition. The off-block part is the eight real entries of the two off-diagonal two by two blocks, which are free.

**What each does.** The seven preserve the two chiral planes and act on each by a unitary of the corresponding block, so they rotate the two chiralities separately. The eight mix the planes and are the only part that moves a spinor's chirality; they are the mass block of *The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*, and the six chiral rotations of the block part are the chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*.

**The image on the bivectors.** The seven act on $\Lambda^{2}\mathbb{C}^{4}$ preserving the split into the two three-spaces, so their image is the $\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ of the self-dual and anti-self-dual halves; the eight map the two halves into each other. This is the $\mathfrak{so}(6)$ reading of the same seven and eight: the block-diagonal part is the $\mathfrak{so}(4)$ of six-space and the off-block part is the rest.

## What the Two Conditions Exclude

**No boost, and so no Lorentz rotor, is in the subspace.**

**Proposition (compactness passes to subalgebras).** Every subalgebra of $\mathfrak{su}(4)$ is compact, so $\mathfrak{so}(1,3)$ is not a subalgebra of $\mathfrak{su}(4)$.

**Proof.** A real subalgebra of a compact real form is a compact Lie algebra, because the positive definite form $\operatorname{tr}(K^*L)$ restricts to it; $\mathfrak{so}(1,3)$ is not compact, its Killing form being indefinite of signature $(6,4)$… the standard fact is that a compact Lie algebra has a negative semidefinite Killing form and $\mathfrak{so}(1,3)$ has not.

**Three separate obstructions, for the record.**
- **Dimension.** $\dim\mathfrak{su}(4)=15$ and $\dim\mathfrak{so}(1,3)=6$; a subalgebra of dimension six exists, but not this one.
- **Boundedness.** Every element of $SU(4)$ has singular values $1$; a boost has the singular values $e^{\pm t}$, unbounded in $t$.
- **Which half.** A boost is the exponential of a traceless Hermitian matrix, and the traceless Hermitian matrices are the other summand of the Cartan decomposition; the exponential of that summand is Hermitian and positive definite, never unitary. This is *The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$*.

**Where the Lorentz rotors are, at order four.** They are not in $SU(4)$. They are the left multiplications by the norm-one biquaternions, a six-dimensional non-compact subgroup of $SL_4(\mathbb{C})$, as the biquaternion corpus states in *Biquaternion Rotations and Lorentz Transformations*: the group $SL(2,\mathbb{C})\cong\mathrm{Spin}(1,3)$ acting on the four coefficients as the Dirac spinor. The fifteen of this article are the compact companion of that six, not its relative.

## The Biquaternion Case

**At order two the same construction gives the spatial rotors.** $M_2(\mathbb{C})$ with the Pauli display of the biquaternion algebra has the traceless anti-Hermitian part of real dimension three, and its exponential is $SU(2)$, the unit quaternions, the rotors of the vector part, with the angle doubled by the sandwich. *The Exponential of the Traceless Anti-Hermitian Part: Determinant One, Unitarity and the Rotation* proves that statement in full.

**The parallel, line by line.**

| | order two | order four |
|---|---|---|
| subspace | $\mathfrak{su}(2)$, dim $3$ | $\mathfrak{su}(4)$, dim $15$ |
| exponential | $SU(2)$, unit quaternions | $SU(4)$ |
| module acted on | the vector part, dim $3$ | $\Lambda^{2}\mathbb{C}^{4}$, dim $6$ |
| group acting on the module | $SO(3)$ | $SO(6)$ |
| kernel of the action | $\{\pm e_t\}$ | $\{\pm I\}$ |
| angles | one | three |

**The degeneracy of the split at order two.** At order two the traceless part is $\mathfrak{su}(2)\oplus i\mathfrak{su}(2)=\mathfrak{sl}_2(\mathbb{C})$, and that algebra *is* the Lorentz algebra $\mathfrak{so}(1,3)$; the anti-Hermitian half is its compact half, the three rotations, and the Hermitian half is the three boosts. The coincidence of the two dimensions, $3+3=6=\dim\mathfrak{so}(1,3)$, is what makes the biquaternion reading of the Lorentz group possible. At order four the same split is $15+15=30=\dim\mathfrak{sl}_4$, and the Lorentz algebra, of dimension six, is nowhere near the anti-Hermitian half: it sits inside the full traceless part, along the block $\mathfrak{sl}_2$ of a two-plane, and it is the biquaternion left multiplications that realise it.

## Summary

**The traceless anti-Hermitian part of $M_4(\mathbb{C})$ is $\mathfrak{su}(4)$, of real dimension $15$ and rank $3$, the compact real form of $\mathfrak{sl}_4$.** Traceless removes the scale and the phase, anti-Hermitian removes the stretch; the exponential of the intersection is $SU(4)$, a closed bounded group in which every element is unitary of determinant one.

**The exponential is onto and not injective.** The fibre over the identity is the set of traceless anti-Hermitian matrices with spectrum in $2\pi i\mathbb{Z}$. Every element of $SL_4$ is $e^{K}e^{H}$ with $K$ in the subspace and $H$ traceless Hermitian, so the subspace generates exactly the compact half of $SL_4$.

**The fifteen split as three Cartan generators and twelve root generators, six pairs, one pair per coordinate plane.** A root family turns its own plane by the closed form $\cos t\,I+\sin t\,K/t$ with the eigenvalues $e^{\pm it}$, fixes the two complementary coordinates exactly, and reads on the four real dimensions of the plane as an isoclinic rotation with two equal angles.

**The action on the bivector space is the rotor action of six-space.** $\Lambda^{2}$ maps $\mathfrak{su}(4)$ injectively onto $\mathfrak{so}(6,\mathbb{C})\cap\mathfrak{u}(6)=\mathfrak{so}(6)$, so $\mathfrak{su}(4)\cong\mathfrak{so}(6)$ and $SU(4)/\{\pm I\}\cong SO(6)$ with degree two. A root family fixes the bivector of its own plane and the complementary bivector and turns the other four with one angle; the Cartan part multiplies $e_i\wedge e_j$ by $e^{i(\mu_i+\mu_j)t}$; a general element has the six angles $\pm\theta_1,\pm\theta_2,\pm\theta_3$.

**The fifteen parameters are three angles and twelve planes.** The angles are the three invariants of a conjugacy class; the twelve are the flag manifold $SO(6)/T^3$, the choice of the three planes.

**The symmetric square carries ten angles, the sums $\mu_i+\mu_j$ with $i\le j$.** The chiral reading splits the fifteen as $7+8$: seven rotate the two chiral planes separately and act on the bivectors as $\mathfrak{so}(3)\oplus\mathfrak{so}(3)$, eight mix the planes and are the mass block.

**No Lorentz rotor is in the subspace.** The algebra is compact, every element is bounded, and a boost lies in the other summand of the Cartan decomposition. The Lorentz rotors at order four are the left multiplications by the norm-one biquaternions, of dimension six, non-compact, acting on the carrier as the Dirac spinor.

$$
\boxed{\ \exp:\mathfrak{su}(4)\to SU(4)\ \text{onto},\quad \det e^{K}=1,\quad \mathfrak{su}(4)\cong\mathfrak{so}(6),\quad SU(4)/\{\pm I\}\cong SO(6),\quad 15=3+12=7+8. }
$$

| module | dimension | angles of $e^{i\operatorname{diag}(\mu)}$ | angles of a root family |
|---|---|---|---|
| $\mathbb{C}^{4}$ | $4$ | $\mu_1,\mu_2,\mu_3,\mu_4$ | $\pm t$ on the plane, $0,0$ outside |
| $\Lambda^{2}\mathbb{C}^{4}$ | $6$ | $\mu_i+\mu_j$ | $0,0,\pm t,\pm t$ |
| $\operatorname{Sym}^{2}\mathbb{C}^{4}$ | $10$ | $\mu_i+\mu_j$, $i\le j$ | $0,0,0,0,\pm t,\pm t,\pm2t$ |
| $\mathfrak{su}(4)$ by conjugation | $15$ | roots $\mu_i-\mu_j$ | $\pm t,\pm t,0,0$ on the root plane |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{su}(4)$ | the traceless anti-Hermitian matrices, real dimension $15$ |
| $SU(4)$ | the special unitary group, $\exp\mathfrak{su}(4)$ |
| $K$ | a generator, an element of $\mathfrak{su}(4)$ |
| $H_k=i(E_{kk}-E_{44})$ | the three Cartan generators |
| $A_{ij}=i(E_{ij}+E_{ji})$, $B_{ij}=E_{ij}-E_{ji}$ | the twelve root generators |
| $E_{ij}$ | the matrix unit |
| $\mu$ | the real Cartan parameter, $\sum_a\mu_a=0$ |
| $\theta$ | an angle of the carrier or of six-space |
| $t$ | the modulus of a root-family parameter |
| $\alpha=ia+b$ | the unimodular phase of a root family, $a^2+b^2=1$ |
| $\Lambda^{2}\mathbb{C}^{4}$ | the bivector space, dimension $6$ |
| $\operatorname{Sym}^{2}\mathbb{C}^{4}$ | the symmetric square, dimension $10$ |
| $\langle\omega,\eta\rangle$ | the symmetric form of the bivector space, $\omega\wedge\eta=\langle\omega,*\eta\rangle\,\mathrm{vol}$ |
| $T^3$ | the maximal torus of $SU(4)$ |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the compact real forms, the Cartan decomposition and the covering $SU(4)\to SO(6)$.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the maximal compact subgroup of a semisimple group.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the polar decomposition and the minors of the second exterior power.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the subspace, its dimension and the compact real forms.
- [The Exponential and the Lie Group of $M_4(\mathbb{C})$](the-exponential-and-the-lie-group-of-m4c.html), for the exponential of the whole algebra and the table of the classical subgroups.
- [The Antisymmetric Sector, the Pfaffian and the Klein Quadric of $M_4(\mathbb{C})$](the-antisymmetric-sector-the-pfaffian-and-the-klein-quadric-of-m4c.html), for the Hodge star and the symmetric form on the bivector space.
- [Rotors Acting on the Bivector Space: the Adjoint Action at $n=4$](rotors-acting-on-the-bivector-space-at-n-4-the-adjoint-action.html), for the six-dimensional $\mathfrak{so}(4)$ image and the self-dual split.
- [Simple and Non-Simple Rotations at $n=4$: the Two Angles and the Isoclinic Families](simple-and-non-simple-rotations-at-n-4-two-angles-and-the-isoclinic-families.html), for the two angles of a rotation of four-space.
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the chiral block.
- [The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$](the-mass-block-and-the-chiral-polar-decomposition-of-m4c.html), for the eight that mix the planes.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$](the-exponential-of-sym-4-stretches-and-the-positive-cone.html), for the other summand of the Cartan decomposition.
- [The Exponential of the Traceless Anti-Hermitian Part: Determinant One, Unitarity and the Rotation](the-exponential-of-the-traceless-anti-hermitian-part-determinant-one-unitarity-and-the-rotation.html), for the order-two statement of the same theorem.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for where the Lorentz rotors are.
