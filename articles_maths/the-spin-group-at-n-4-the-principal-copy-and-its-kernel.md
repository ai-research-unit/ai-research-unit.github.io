# __The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$__

## Introduction

**The subject.** The matrix algebra of order four carries a copy of $SU(2)$, the **principal copy**, defined as the image of the third symmetric power of the defining two-dimensional representation. The module of the copy is $\mathbb{C}^4=\operatorname{Sym}^3\mathbb{C}^2=V_{3/2}$, the copy acts on the algebra by conjugation, and the kernel of that action is exactly the centre $\{\pm\mathrm I\}$.

**The order of the article.** The first section builds the copy and fixes the generators. The second proves that the conjugation action is unitary and by algebra automorphisms. The third computes the kernel, first on the module and then on the algebra. The fourth draws the consequence, that the algebra action is an action of $SO(3)$ and that its labels are therefore integers. The fifth compares the two kernels and states what the difference costs and what it buys.

**It assumes** *The Matrix Algebra $M_4(\mathbb{C})$* for the conventions, and *The Spin Content of $M_4(\mathbb{C})$* for the four carrier lists. The row at order two is *The Spin Group via $4\times4$ Real Matrices*; the rotor is *From the Spin Group to the Spin of a Single Rotor at $n=4$*.

**The result in one line.** The module is faithful and carries the half-integer label $\tfrac32$; the algebra action has kernel $\{\pm\mathrm I\}$ and carries the integer labels $0,1,2,3$; the difference between the two statements is one element, $-\mathrm I$.

**Boundaries.** Nothing here is about the real forms of the copy, which are the subject of *The Quaternionic Structure of the Module at $n=4$*. The decomposition of the algebra is quoted when needed and proved in *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$*; the computation of the weights is in *The Four Weights of the Module and the Half Angle at $n=4$*.

## The Principal Copy

**Definition.** Let $S=\mathbb{C}^2$ be the defining module of $SU(2)$. The **principal copy** is the image of the symmetric cube

$$
\operatorname{Sym}^3:SU(2)\longrightarrow GL(\operatorname{Sym}^3 S)=GL_4(\mathbb{C}),
$$

and the **module** of the copy is $V=\operatorname{Sym}^3 S$, of complex dimension four.

**Proposition.** With the orthonormal weight basis of $\operatorname{Sym}^3 S$, whose vectors are proportional to the monomials $u^3,u^2v,uv^2,v^3$, the derived representation of the Lie algebra sends the three generators to

$$
J_z=\operatorname{diag}\Bigl(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32\Bigr),\qquad
J_+=\sqrt3\,E_{01}+2E_{12}+\sqrt3\,E_{23},\qquad
J_-=J_+^{\dagger},
$$

and the brackets

$$
[J_z,J_+]=\phantom{-}J_+,\qquad [J_z,J_-]=-J_-,\qquad [J_+,J_-]=2J_z
$$

hold up to a residual of order $10^{-16}$, which is the rounding of the arithmetic and not a defect of the model.

*Proof.* The torus acts on $u$ and $v$ with opposite weights, so on the monomial $u^{3-k}v^{k}$ it acts with weight $\tfrac32-k$; that gives the diagonal matrix. The raising operator carries $u^{3-k}v^{k}$ to $u^{4-k}v^{k-1}$ with the coefficient $\sqrt{(3-k)(k+1)}$, which is $\sqrt3,2,\sqrt3$ for $k=0,1,2$; the lowering operator is the transpose conjugate. The three brackets are then checked entry by entry, and the numerical residuals are at the level of the machine epsilon.

**Corollary.** $J_z$ is Hermitian with the four distinct eigenvalues $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, and $J_+$ and $J_-$ are conjugate transposes of one another.

*Proof.* The diagonal entries are real, and the off-diagonal matrices displayed are transposes.

**Corollary.** The copy is a copy of $SU(2)$ and not of $SO(3)$: the module is a genuine spinorial module.

*Proof.* The kernel of the module representation is computed in the third section; it is $\{\pm\mathrm I\}$ and not larger, so the image is isomorphic to $SU(2)$.

## The Action on the Algebra

**Definition.** For $q\in SU(2)$ and $X\in M_4(\mathbb{C})$ let

$$
\Phi_q(X)=\rho(q)\,X\,\rho(q)^{-1},
$$

where $\rho(q)=\operatorname{Sym}^3 q$. This is the **conjugation action** of the principal copy on the algebra.

**Proposition.** $\rho(q)$ is unitary for every $q$, that is, $\rho(q)^{\dagger}=\rho(q)^{-1}$, and $\Phi_q$ is an algebra automorphism with $\Phi_q\circ\Phi_{q'}=\Phi_{qq'}$.

*Proof.* A symmetric power of a unitary matrix is unitary in the orthonormal weight basis, and the transpose conjugate of $\operatorname{Sym}^3 q$ is $\operatorname{Sym}^3(q^{\dagger})=\operatorname{Sym}^3(q^{-1})$. Conjugation by an invertible element is an automorphism, and the composition law is associativity of the product.

**Corollary.** $\Phi_q$ preserves the trace, the determinant, the rank and the spectrum of $X$.

*Proof.* All four are invariants of similarity.

**Corollary.** $\Phi_q$ is a unitary operator on the algebra for the Hilbert–Schmidt form, since $\operatorname{tr}\bigl(\Phi_q(X)^{\dagger}\Phi_q(Y)\bigr)=\operatorname{tr}(X^{\dagger}Y)$.

*Proof.* Insert $\rho(q)^{\dagger}=\rho(q)^{-1}$ and use the cyclicity of the trace.

**The two-sided form.** The action is written with one factor on each side, and neither the left multiplication alone nor the right multiplication alone is an algebra map. The left multiplication $X\mapsto\rho(q)X$ carries a product $XY$ to $\rho(q)XY$, while the product of the images is $\rho(q)X\rho(q)Y$; the two differ by the second factor. Conjugation is the smallest repair, and it is the reason the action on the algebra is two-sided while the action on the module is one-sided.

*Proof.* The two displays differ by $\rho(q)$ on the right, which is not the identity unless $q$ is central.

## The Kernel on the Module

**Proposition.** $\rho(-\mathrm I_2)=(-1)^{3}\mathrm I_4=-\mathrm I_4$, and the kernel of $\rho$ is exactly $\{\pm\mathrm I_2\}$.

*Proof.* On the monomial $u^{3-k}v^{k}$ the matrix $-\mathrm I_2$ acts by $(-1)^{3-k}(-1)^{k}=(-1)^{3}=-1$; hence $\rho(-\mathrm I_2)=-\mathrm I_4$. The kernel of an irreducible representation of $SU(2)$ is the centre when the representation is faithful; here $-\mathrm I_2$ acts as $-1$, which is not the identity, so the kernel is not all of the centre and contains no other element, since $SU(2)$ has centre $\{\pm\mathrm I_2\}$.

**Corollary.** The label of the module is $\tfrac32$, an odd half-integer, and the module is faithful.

*Proof.* The highest weight is $\tfrac32$, and faithful means injective, which is the proposition.

**The general rule.** For the symmetric power $\operatorname{Sym}^{m}S$ the element $-\mathrm I_2$ acts as $(-1)^{m}$, so the representation is faithful exactly when $m$ is odd, that is, exactly when the label $\tfrac m2$ is a half-integer in the strict sense. At $n=4$ one has $m=3$ and the module is faithful; at $n=3$ one has $m=2$ and the module is not faithful.

*Proof.* The same computation as in the proposition, with $m$ in place of three.

## The Kernel on the Algebra

**Proposition.** $\Phi_{-\mathrm I}(X)=(-\mathrm I_4)X(-\mathrm I_4)^{-1}=X$ for every $X$, so $-\mathrm I_2$ lies in the kernel of the algebra action.

*Proof.* The two signs cancel, $(-1)\cdot(-1)=+1$.

**Theorem.** The kernel of $q\mapsto\Phi_q$ is exactly $\{\pm\mathrm I_2\}$, and the image is isomorphic to $SU(2)/\{\pm\mathrm I_2\}\cong SO(3)$.

*Proof.* The proposition gives the inclusion of the centre in the kernel. For the converse, an element in the kernel acts trivially on the algebra, hence on the module, since the module is a quotient of the algebra as a module; by the previous section the kernel of the module action is the centre, so the kernel of the algebra action is contained in the centre. The quotient of $SU(2)$ by its centre is $SO(3)$, and the map to $GL(M_4)$ is injective on the quotient.

**Corollary.** The kernel is not larger than $\{\pm\mathrm I_2\}$: no element of $SU(2)$ outside the centre acts trivially on $M_4(\mathbb{C})$.

*Proof.* The theorem.

**The dimension check.** Both groups have dimension three, $\dim SU(2)=3$ and $\dim SO(3)=3$, and the covering is two-to-one. The module has dimension four and the algebra sixteen, and neither dimension enters the count of the kernel.

*Proof.* The real dimensions of the two groups, and the dimension count for the two spaces.

## Faithfulness and Factorisation

**Proposition.** The module representation is faithful and the algebra representation factors through the centre; the two statements are compatible because the algebra contains the module in a way that is not stable under the copy.

*Proof.* The module is $\operatorname{Sym}^3 S$, on which $-\mathrm I$ acts as $-1$; the algebra is $\operatorname{End}(V)$, on which $-\mathrm I$ acts as the conjugation by $-1$, which is the identity. The containment of the module in the algebra is not equivariant: the module appears inside the algebra only as a left ideal, and left multiplication is one-sided.

**Corollary (the origin of the integers).** Every label of a summand of the algebra is an integer, since the acting group is $SO(3)$ and the irreducible representations of $SO(3)$ are the integer spins.

*Proof.* The decomposition of the algebra into summands is a decomposition into irreducible representations of the image group, which is $SO(3)$; the irreducible representations of $SO(3)$ are $V_k$ with $k$ a non-negative integer.

**Corollary (the exception).** The half-integer $\tfrac32$ nevertheless occurs inside the algebra, as the label of a minimal left ideal, and not as the label of a summand.

*Proof.* A rank-one idempotent $P$ gives a four-dimensional left ideal $M_4P$ on which left multiplication by $J_z$ has the eigenvalues $\pm\tfrac32,\pm\tfrac12$; a summand of the conjugation decomposition would need these weights in the multiset $0^{4},\pm1^{3},\pm2^{2},\pm3$, which does not contain them.

## Summary

The principal copy is the image of $\operatorname{Sym}^3$ in $GL_4(\mathbb{C})$, its module is $\mathbb{C}^4=V_{3/2}$ with the four weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, and the three generators satisfy the $\mathfrak{su}_2$ brackets to machine precision. The copy acts on the algebra by conjugation, which is unitary for the Hilbert–Schmidt form and preserves trace, determinant and spectrum.

The element $-\mathrm I$ acts as $-1$ on the module, because $2j=3$ is odd, and as $+1$ on the algebra, because the two signs cancel. The kernel of the module representation is $\{\pm\mathrm I\}$ and the kernel of the algebra representation is also $\{\pm\mathrm I\}$; the first makes the module faithful, the second makes the algebra action an action of $SO(3)$.

The factorisation through $SO(3)$ is the reason every label of a summand is an integer. The half-integer $\tfrac32$ is present inside the algebra only as the label of a minimal left ideal, where the acting group is read through a one-sided multiplication and the kernel no longer acts trivially.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S=\mathbb{C}^2$ | the defining module of $SU(2)$ |
| $\rho(q)=\operatorname{Sym}^3 q$ | the module representation |
| $V=\operatorname{Sym}^3 S=V_{3/2}$ | the module of the copy |
| $J_z,J_+,J_-$ | the three generators in the weight basis |
| $\Phi_q(X)=\rho(q)X\rho(q)^{-1}$ | the conjugation action |
| $V_k$ | the carrier of spin $k$, of dimension $2k+1$ |
| $M_4P$ | a minimal left ideal |

## Further Reading

- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the four carrier lists and the corrected proposition on spin $\tfrac32$.
- [From the Spin Group to the Spin of a Single Rotor at $n=4$](from-the-spin-group-to-the-spin-of-a-single-rotor-at-n-4.html), for the sign after $2\pi$.
- [The Four Weights of the Module and the Half Angle at $n=4$](the-four-weights-of-the-module-and-the-half-angle-at-n-4.html), for the weight basis and the lowering operator.
- [The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$](the-clebsch-gordan-decomposition-of-m4c.html), for the decomposition used in the section on faithfulness.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices.html), for the row at order two.
