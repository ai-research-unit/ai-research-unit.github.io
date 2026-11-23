# __Coda: $M_4(\mathbb{C})$ and the Kronecker Reading__

## Introduction

**The category established one algebra, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$, one operator algebra $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}(\mathbb{B})$, and one matrix model $M_4(\mathbb{C})$, and the thread through every block is the Kronecker reading $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$; at $n=3$ that reading fails, the biquaternion model has no analogue, $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ has no counterpart, the trace form has inertia $(6,3)$, and the two angles exist for every $n\ge4$, so order four is the first order with two angles and not the only one.**

The article recalls what each block established, states the Kronecker reading and identifies its two factors with the two one-sided algebras, collects the thread, and then examines the passage to $M_3(\mathbb{C})$, where each of the special features of order four disappears except one: the number of rotation angles grows with the order and is two from order four onwards.

## What the Category Established

**The algebra.** The two base fields: $M_4(\mathbb{R})$ inside $M_4(\mathbb{C})$ as the fixed algebra of the conjugation, of real dimension $16$ inside $32$. The elementary symmetric functions: the four coefficients of $\det(\mathrm I+tA)$ and the strata they cut. The minimal polynomial and the Jordan form: the five partitions of four and the two regimes. The ideals: the centre $\mathbb{C}\mathrm I$ and the central simplicity of degree four.

**The involutions and the decompositions.** The involutions of first and second kind and their fixed algebras; the two halves $\operatorname{Sym}_4$ and $\operatorname{Skew}_4$ of dimensions $10$ and $6$; the orthogonality of the two halves; the fine decomposition against the diagonal with the count $4+6+6$; the triangular decomposition with the Borel of dimension $10$; $UT_4$ as another complement of the anti-Hermitian half; the symmetric and Cartan pairs with the reductivity criterion.

**The product on the halves.** The symmetric and antisymmetric parts of a product; the four multiplication tables and their ranks; the Jordan algebra $\operatorname{Sym}_4$ of degree four; the Lie algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$; the derivation $[A,X]$ and its two anti-self-adjointness statements; the radical of the Borel as its commutator; and $UT_4$ as a linear model of $\operatorname{Sym}_4$ with the wrong product.

**The forms.** The trace form with inertia $(10,6)$, the keystone of the category; the Killing form $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$ with radical $\mathbb{C}\mathrm I$; the Hilbert–Schmidt form with the two orthonormal bases; the four forms and their algebraic norms, with $P=Q_t^{2}-B^{2}$, $N=Q_t^{2}+B^{2}$ and $\det=\langle\tilde Q\rangle_\natural^{2}$.

**The idempotents and the spectrum.** The Peirce decompositions of the Jordan algebra and of the algebra, with the dimensions $k^{2}$, $(4-k)^{2}$ and $2k(4-k)$ and the corner recursion; the common spectral theorem for normal matrices; the Hermitian and the anti-Hermitian spectral theorems.

**The exponential and the rotor.** The rotor as a square root of a rotation with two signs and the double cover; the adjoint action on the six-dimensional bivector space; simple and non-simple rotations with two angles; where the rotor leaves the matrix algebra, in $Cl^{+}(4)\cong M_2\oplus M_2$; the exponential of the symmetric part stretching onto the cone.

**The operators.** $\operatorname{End}(M_4)$ of dimension $256$ and the regular representation; the one-sided operators and the stitch $R^{\mathrm{axf}}=D(L^{\mathrm{axf}})^{\mathsf T}D$; the two-sided operators and the Segre cone of dimension seven; the length and the two ranks; the two adjoints and the polar decomposition of an operator; the four eigenspaces of the two commuting involutions.

**Topology, analysis, geometry.** The contraction $\mathrm{GL}_4\simeq U(4)$ and the components of the halves; the idempotents as Grassmannians and the Klein quadric; the homotopy groups; the exponential and the Lie group structure; the positive cone and its boundary; the smooth structures; the geometry of the halves and the return of the operators; the symmetric space $\mathrm{GL}_4/O(4)$ and its complex twin; the semidefinite cone.

## The Kronecker Reading

**Theorem.** $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes_{\mathbb{C}}M_2(\mathbb{C})$ as algebras, by the Kronecker product $A\otimes B\mapsto$ the block matrix with blocks $a_{ij}B$.

**Proof.** The Kronecker product of matrix units satisfies $(E_{ij}\otimes E_{kl})(E_{i'j'}\otimes E_{k'l'})=\delta_{ji'}\delta_{lk'}E_{ij'}\otimes E_{kl'}$, which is the multiplication rule of matrix units; the sixteen products are therefore the matrix units of the algebra of order four, the map is an injective algebra homomorphism, and both sides have dimension sixteen.

**Corollary.** The two factors are subalgebras and not ideals: $M_2\otimes\mathrm I$ and $\mathrm I\otimes M_2$ are each isomorphic to $M_2(\mathbb{C})$ and neither is a two-sided ideal of the product.

**Proof.** An ideal of a product of simple algebras would contain a factor; the two subalgebras commute with each other and their product generates everything.

**Corollary.** The Kronecker reading is the statement $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}(\mathbb{B})$ once the factors are named: the first factor is the left multiplications, the second the right multiplications.

**Proof.** $L_aR_b=L_a\otimes R_b^{\mathrm{opp}}$, and the sixteen products are independent.

**Corollary.** The sixteen two-sided products are the matrix units of the reading, and the trace pairing on them is the permutation form, which shows no inertia in that basis.

**Proof.** The trace of a product of two matrix units is a Kronecker delta.

## The Thread

**Proposition.** Every special feature of order four is a feature of the factorisation $4=2\cdot2$: the trace-form inertia $(10,6)$, the split $\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, the two angles of a rotation, the two orthogonal complex structures, the even Clifford algebra $M_2\oplus M_2$, and the Segre cone $\mathbb{P}^{3}\times\mathbb{P}^{3}$.

**Proof.** Each object is built from the pair of factors $M_2$ and $M_2$: the ten and the six are the symmetric and antisymmetric parts of the tensor product, the two $\mathfrak{sl}_2$ are the two factors of the antisymmetric part, and the two angles are the two parameters of the two factors.

**Corollary.** The two-sided operators are the place where the factorisation is visible as operators: the basis $T_{\mu\nu}=L_{e_\mu}R_{e_\nu}$ is the tensor product of the two four-dimensional one-sided bases.

**Proof.** The product formula and the independence of the sixteen elements.

**Corollary.** The group of order $32$ generated by the signed basis elements is the finite skeleton of the factorisation: it is the central product of two copies of the quaternion group, one from each factor.

**Proof.** Each factor $M_2$ contains a copy of $Q_8$ among its signed permutation units, and the sixteen products generate the central product.

## The Passage to $n=3$

**Proposition.** $M_3(\mathbb{C})$ is not a nontrivial tensor product of matrix algebras, since $3$ is prime and the only factorisation is $1\cdot3$.

**Proof.** The dimension of a tensor product is the product of the dimensions, and the only factorisations of nine into two squares greater than one would need $3=ab$ with $a,b>1$.

**Corollary.** The Kronecker reading fails at order three, and with it the two-sided operator description of the algebra as a tensor square.

**Proof.** The previous proposition.

**Corollary.** The biquaternion model has no analogue at order three: a three-dimensional algebra whose tensor square is $M_3(\mathbb{C})$ would have to be simple, and a simple algebra over $\mathbb{C}$ of dimension three would be $M_k(\mathbb{C})$ with $k^{2}=3$, which is impossible.

**Proof.** The tensor square of a three-dimensional algebra has dimension nine, and the simple algebras over $\mathbb{C}$ have square dimensions.

**Corollary.** $\mathfrak{so}(3)$ is simple of dimension three, equal to $\mathfrak{sl}_2$, and there is no decomposition into two ideals as at order four.

**Proof.** $\mathfrak{so}(3)\cong\mathfrak{su}(2)$ is simple.

**Corollary.** The trace form on $M_3(\mathbb{C})$ has inertia $(6,3)$, since $\dim\operatorname{Sym}_3=6$ and $\dim\operatorname{Skew}_3=3$, and the fine count is $3+3+3=9$.

**Proof.** $\operatorname{tr}(S^{2})>0$ on real symmetric matrices of order three and $\operatorname{tr}(K^{2})<0$ on real antisymmetric matrices, with the same dimension count as at order four.

**Corollary.** The inertia is the pair of triangular numbers $\tfrac{3\cdot4}{2}=6$ and $\tfrac{3\cdot2}{2}=3$, the same pattern as the ten and the six at order four, so the pattern survives the loss of the factorisation.

**Proof.** The two counts.

## The Two Angles beyond $n=4$

**Proposition.** A rotation of $\mathbb{R}^{n}$ has $\lfloor n/2\rfloor$ angles in its normal form, so there are two angles from order four onwards and not only at order four.

**Proof.** The real normal form of an orthogonal matrix is a block diagonal of rotations by single angles plus a possible $\pm1$ in odd order.

**Corollary.** Order four is the first order at which two angles appear, and it is not the only one; the special features of order four are the factorisation $4=2\cdot2$, not the number of angles.

**Proof.** $\lfloor3/2\rfloor=1$ and $\lfloor4/2\rfloor=2$, and the count grows with the order.

**Corollary.** The two angles at order four are the two parameters of the two $\mathfrak{sl}_2$ summands; at order five there are two angles and no such splitting, so the two angles and the split are independent phenomena.

**Proof.** The dimension of the maximal torus of $\mathfrak{so}(n)$ is $\lfloor n/2\rfloor$, while the split into two ideals happens only at order four.

**The isoclinic case.** The isoclinic rotations, with the two angles equal in modulus, exist for every even order; at order four they form the two families $\theta_1=\pm\theta_2$.

**Proof.** The isoclinic condition is the proportionality of the two angles, available for every even order.

**Corollary.** Nothing in the two-angle story is special to order four except the exact coincidence with the two $\mathfrak{sl}_2$ factors.

**Proof.** The two statements above.

## Summary

The category established one algebra of dimension four, one operator algebra of dimension sixteen and one matrix model of dimension sixteen, and kept them apart throughout. The trace form on the model has inertia $(10,6)$, the two halves are its positive and negative eigenspaces, and the symmetric decomposition and the form are one split read twice.

The thread is the Kronecker reading $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$, which is $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}(\mathbb{B})$ once the two factors are named as the left and the right multiplications. Every special feature of order four comes from the factorisation $4=2\cdot2$.

At order three the reading fails, the biquaternion model disappears, $\mathfrak{so}(3)$ is simple, and the trace form has inertia $(6,3)$. The two angles of a rotation exist for every order at least four, so order four is the first with two angles but not the only one; what is unique to order four is the coincidence of the two angles with the two simple ideals.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_4\cong M_2\otimes M_2$ | the Kronecker reading |
| $M_2\otimes\mathrm I$, $\mathrm I\otimes M_2$ | the two factors, subalgebras not ideals |
| $(10,6)$ | the inertia at order four |
| $(6,3)$ | the inertia at order three |
| $\lfloor n/2\rfloor$ | the number of angles |
| central product $Q_8\circ Q_8$ | the finite skeleton, order $32$ |

## Further Reading

- [The Trace Form and Its Inertia on the Two Halves of $M_4(\mathbb{C})$](the-trace-form-and-its-inertia-on-the-two-halves-of-m4c.html), for the keystone of the category.
- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the operator face of the factorisation.
- [The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$](the-lie-algebra-skew-4-and-so-4.html), for the split into two simple ideals.
- [Simple and Non-Simple Rotations: One Angle at $n\le3$, Two Angles at $n\ge4$](simple-and-non-simple-rotations-one-angle-at-n-le-3-two-angles-at-n-ge-4.html), for the count of angles.
- [The Ideals, the Centre and the Simplicity of $M_4(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-m4c.html), for the simplicity that makes the factors subalgebras.
