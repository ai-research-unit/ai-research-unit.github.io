# __Two-Sided Operators on the Biquaternion Algebra__

## Introduction: The Cone

**The subject.** A left multiplication and a right multiplication can be composed. For a pair of elements $\tilde Q,\tilde P\in\mathbb{B}$, the composite is the map

$$
T_{\tilde Q,\tilde P}:\mathbb{B}\longrightarrow\mathbb{B},\qquad T_{\tilde Q,\tilde P}(X)=\tilde Q\,X\,\tilde P ,
$$

the **two-sided operator** of the pair. The first subscript is the left multiplier, the second the right multiplier, and the argument is the third slot. The definition is the product of the two one-sided operators, $T_{\tilde Q,\tilde P}=L_{\tilde Q}R_{\tilde P}$, and it contains them at the two boundary cases $\tilde P=e_t$ and $\tilde Q=e_t$.

**The cone.** The assignment $(\tilde Q,\tilde P)\mapsto T_{\tilde Q,\tilde P}$ is bilinear, so the set of two-sided operators is closed under multiplication by complex scalars but not under addition. It is a **cone**, the image of the bilinear map, and its projective image is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$ of the decomposable tensors. The two parameters are eight complex numbers; the cone has complex dimension seven, because the scaling $(\tilde Q,\tilde P)\mapsto(\lambda\tilde Q,\lambda^{-1}\tilde P)$ leaves the operator unchanged.

**The basis operators.** The sixteen **basis operators** are

$$
e_\mu[\,]e_\nu:\mathbb{B}\longrightarrow\mathbb{B},\qquad e_\mu[\,]e_\nu(X)=e_\mu Xe_\nu,
$$

with $\mu,\nu\in\{t,x,y,z\}$. They are named here, at the start, because the generation theorem uses them: they are a basis of the ambient operator space $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and every two-sided operator is a linear combination of them. The bracket is the one of the elementary operators, and the two indices are the two slots.

**What the article proves.** The composition law $T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\tilde S\tilde P}$, with the second slot reversed. The two closures: the family is closed under composition and not under addition. The generation theorem: the sixteen basis operators are a basis of the ambient space, so the span of the family is the whole $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. The ladder $1,4,7,16$: the scalars, the one-sided families, the cone and the ambient space. The plain adjoint: $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$, the self-adjoint pairs and the empty skew sector. The isometries and the multiplicative members: the criteria $\tilde P\tilde Q=\pm e_t$ and $\tilde Q\tilde P=e_t$, the isometry group, and the absence of a pin group in the family.

**What the article does not do.** The matrix of $T_{\tilde Q,\tilde P}$ is *Two-Sided Operators on the Biquaternion Algebra*, where the sixteen matrices, the coefficient matrix and the length are computed. The Hermitian sandwich $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$ is Part V: this article states no sandwich theorem. The enveloping algebra and the bi-module structure are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; this article proves the generation statement on which that article's isomorphism rests. The association of the two one-sided families with the plain form is *The Four Adjoints of the Biquaternion Algebra in Examples*.

**The letters.** The parameters are $\tilde Q,\tilde P,\tilde R,\tilde S$, the argument is $X$, and the operator is $T_{\tilde Q,\tilde P}$. The letter $T$ names the two-sided family; the sandwich $\Theta$ is a different letter and a different object, and it is not used here. The conventions of the four letters, the slots and the set names are *Operator Family Conventions*.

**Boundaries.** The algebra is *The Biquaternion Algebra*; the ambient operator space is *The Endomorphisms of the Biquaternion Algebra*; the one-sided families are *The Left Regular Operators on the Biquaternion Algebra* and *The Right Regular Operators on the Biquaternion Algebra*; the commutant is *The Commutant of the Two Regular Families*; the matrix units are *Special Element and Peirce Conventions*; the form is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*.

## The Operator $T_{\tilde Q,\tilde P}$

### The Definition

**Definition.** For $\tilde Q,\tilde P\in\mathbb{B}$, the **two-sided operator of the pair** is

$$
T_{\tilde Q,\tilde P}:\mathbb{B}\longrightarrow\mathbb{B},\qquad T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P .
$$

**Proposition (bilinearity).** The assignment $(\tilde Q,\tilde P)\mapsto T_{\tilde Q,\tilde P}$ is complex-bilinear:

$$
T_{\lambda\tilde Q+\mu\tilde Q',\tilde P}=\lambda T_{\tilde Q,\tilde P}+\mu T_{\tilde Q',\tilde P},\qquad
T_{\tilde Q,\lambda\tilde P+\mu\tilde P'}=\lambda T_{\tilde Q,\tilde P}+\mu T_{\tilde Q,\tilde P'}.
$$

*Proof.* Both displays are the distributivity and the complex bilinearity of the algebra product.

**Proposition (the one-sided boundary).** With the unit in one slot,

$$
T_{\tilde Q,e_t}=L_{\tilde Q},\qquad T_{e_t,\tilde P}=R_{\tilde P}.
$$

*Proof.* $Xe_t=X$ and $e_tX=X$.

**Proposition (injectivity in each slot).** For a fixed unit $\tilde P$, the map $\tilde Q\mapsto T_{\tilde Q,\tilde P}$ is injective; for a fixed unit $\tilde Q$, the map $\tilde P\mapsto T_{\tilde Q,\tilde P}$ is injective.

*Proof.* $T_{\tilde Q,\tilde P}(e_t)=\tilde Q\tilde P$, and $\tilde P$ is a unit, so $\tilde Q$ is recovered. The second statement is $T_{\tilde Q,\tilde P}(e_t)=\tilde Q\tilde P$ with $\tilde Q$ a unit.

**The zero operator.** $T_{\tilde Q,\tilde P}=0$ exactly when $\tilde Q=0$ or $\tilde P=0$. If one parameter is zero the operator is zero. Conversely, if both are nonzero, choose entries $Q_{ab}\neq0$ and $P_{cd}\neq0$ in the $2\times2$ model and put $X=E_{bc}$; then $(QXP)_{ad}=Q_{ab}P_{cd}\neq0$.

### The Scaling Orbit

**Proposition (the scaling).** For every $\lambda\in\mathbb{C}^{\times}$,

$$
T_{\lambda\tilde Q,\lambda^{-1}\tilde P}=T_{\tilde Q,\tilde P}.
$$

*Proof.* $(\lambda\tilde Q)X(\lambda^{-1}\tilde P)=\tilde QX\tilde P$.

**The orbit.** The group $\mathbb{C}^{\times}$ acts on the parameter space by $(\tilde Q,\tilde P)\mapsto(\lambda\tilde Q,\lambda^{-1}\tilde P)$, and the operator is constant on each orbit. For a pair with both parameters nonzero, the orbit is a complex line, and it is the whole set of pairs giving the same operator: if $T_{\tilde Q,\tilde P}=T_{\tilde R,\tilde S}$ with nonzero pairs, then $\tilde R=\lambda\tilde Q$ and $\tilde S=\lambda^{-1}\tilde P$. The proof is the injectivity of the tensor map, proved in §*The Sixteen Products as a Basis*.

**The dimension.** The parameter space has complex dimension eight. The generic orbit has dimension one, so the cone has complex dimension seven. The zero operator is the image of every pair with a zero parameter, and it is the vertex of the cone.

**The normalisation.** A pair with $\tilde Q$ a unit can be put in the normal form $(\tilde Q,e_t)$ by the scaling $\lambda=\tilde Q^{-1}$, which gives the left multiplication; a pair with $\tilde P$ a unit can be put in the form $(e_t,\tilde P)$, which gives the right multiplication. The scaling is therefore the reason the cone has a complex seven-dimensional body and a complex four-dimensional boundary on each side.

### $L_{\tilde Q}$ and $R_{\tilde Q}$ as Boundary Cases

**The two slices.** The boundary cases are the two slices $\tilde P=e_t$ and $\tilde Q=e_t$. The first is the left family, of complex dimension four; the second is the right family, also of complex dimension four. Both are contained in the cone.

**The intersection of the slices.** The two slices meet in the scalars: $L_{\tilde Q}=R_{\tilde P}$ exactly when $\tilde Q=\tilde P$ is central, by *The Commutant of the Two Regular Families*, §*The Proof*. The intersection is the line $\mathbb{C}\cdot\mathrm I_4$, of complex dimension one.

**The boundary is not the whole cone.** A generic pair has neither parameter equal to the unit, and its operator is neither a left nor a right multiplication. The cone is complex seven-dimensional, the two boundary slices are complex four-dimensional each, and the difference is the two-parameter body.

## Composition and the Two Closures

### $T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\tilde S\tilde P}$

**Theorem (composition).** For all $\tilde Q,\tilde P,\tilde R,\tilde S\in\mathbb{B}$,

$$
T_{\tilde Q,\tilde P}\,T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\ \tilde S\tilde P}.
$$

*Proof.* For every $X$, $T_{\tilde Q,\tilde P}(T_{\tilde R,\tilde S}(X))=\tilde Q(\tilde RX\tilde S)\tilde P=(\tilde Q\tilde R)X(\tilde S\tilde P)$ by associativity.

**The reversal.** The first slot composes in the order of the composition, $\tilde Q\tilde R$; the second slot composes in the reverse order, $\tilde S\tilde P$. The reversal is the anti-representation of the right family, and it is the only place where the order of the two parameters is not the reading order.

**The powers.** By induction, $(T_{\tilde Q,\tilde P})^n=T_{\tilde Q^n,\tilde P^n}$ for every $n\geq1$.

**The inverses.** $T_{\tilde Q,\tilde P}$ is invertible exactly when both parameters are units, and then

$$
(T_{\tilde Q,\tilde P})^{-1}=T_{\tilde Q^{-1},\tilde P^{-1}}.
$$

*Proof.* The inverse is verified by the composition law. Conversely, if the operator is invertible it is injective; a nonzero kernel of $\tilde Q$ or of $\tilde P$ would give a nonzero kernel of the operator, so both are units.

**The identity.** $T_{\tilde Q,\tilde P}=\mathrm{id}$ exactly when $\tilde Q\tilde P=e_t$ and $\tilde Q$ is central. The proof is the evaluation at $e_t$ and then the commutation with every $X$; the central solutions are $\tilde Q=\lambda e_t$, $\tilde P=\lambda^{-1}e_t$.

### Closed Under Multiplication, Not Under Addition

**Proposition (closure under composition).** The set $\operatorname{End}_{LR}(\mathbb{B})=\{T_{\tilde Q,\tilde P}\}$ is closed under composition, by the composition law. It contains the identity $T_{e_t,e_t}$ and is closed under inversion on the units.

**Proposition (not closed under addition).** The sum of two two-sided operators need not be a two-sided operator. The simplest example is

$$
\mathrm{id}+T_{\vec e_x,\vec e_x},
$$

which is not of the form $T_{\tilde Q,\tilde P}$.

*Proof.* Suppose $\mathrm{id}+T_{\vec e_x,\vec e_x}=T_{\tilde Q,\tilde P}$. At $X=e_t$ the left side is $e_t+\vec e_x e_t\vec e_x=e_t-e_t=0$, so $\tilde Q\tilde P=0$. If $\tilde Q=0$ or $\tilde P=0$, the right side is zero, but the left side at $X=\vec e_y$ is $\vec e_y+\vec e_x\vec e_y\vec e_x=2\vec e_y\neq0$; so both parameters are nonzero. In the $2\times2$ model, $\tilde Q\tilde P=0$ with both factors nonzero forces both to have rank one. At $X=\vec e_y$ the left side is $2\vec e_y$, of rank two, while $\tilde Q\vec e_y\tilde P$ has rank at most one. Contradiction.

**The two closures.** The family is a multiplicative monoid and not an additive one. Its linear span is a subspace, and the span is the subject of §*The Generation Theorem*; the family itself is the cone inside that span, not the whole span.

**The sum of two products.** A sum $T_{\tilde Q,\tilde P}+T_{\tilde R,\tilde S}$ is a two-sided operator in special cases, for instance when the two pairs are proportional, but not in general. The criterion for a sum of two products to be one product is the rank condition of *Two-Sided Operators on the Biquaternion Algebra*, §*The Criterion for a Single Product*.

## The Generation Theorem

### The Statement

**Theorem (the generation).** The sixteen basis operators $e_\mu[\,]e_\nu$, $\mu,\nu\in\{t,x,y,z\}$, are linearly independent and span the ambient space:

$$
\operatorname{Span}_{\mathbb{C}}\{T_{\tilde Q,\tilde P}:\tilde Q,\tilde P\in\mathbb{B}\}=\operatorname{End}_{\mathbb{C}}(\mathbb{B}),\qquad
\dim_{\mathbb{C}}\operatorname{End}_{\mathbb{C}}(\mathbb{B})=16 .
$$

In particular every complex-linear operator of $\mathbb{B}$ is a finite sum of two-sided operators, and the sum needs at most sixteen terms.

**The statement beside the proof.** The independence and the spanning are proved together in the next two subsections: the matrix-unit computation exhibits sixteen independent operators, and the change of basis shows that the coefficient products are the same sixteen operators in another basis. The generation statement is not used before it is proved.

### The Matrix-Unit Computation

**The algebra's matrix units.** In the Peirce frame, write

$$
U_{11}=\tilde\Pi_+,\qquad U_{12}=\vec\Upsilon_-,\qquad U_{21}=\vec\Upsilon_+,\qquad U_{22}=\tilde\Pi_- .
$$

The four elements satisfy

$$
U_{ij}U_{kl}=\delta_{jk}U_{il},
$$

the multiplication table of the matrix units of $M_2(\mathbb{C})$, by *Spinors as Peirce Coordinates in the Biquaternion Algebra*, §*Systems of Matrix Units*. The order of the indices is the matrix order: the first index is the row, the second the column, and $U_{12}=\vec\Upsilon_-$ and $U_{21}=\vec\Upsilon_+$ are the two mixed units in that order.

**The elementary operators.** For fixed $i,j,k,l$, the operator $U_{ij}[\,]U_{kl}$ acts on the basis element $U_{mn}$ by

$$
U_{ij}[\,]U_{kl}(U_{mn})=U_{ij}U_{mn}U_{kl}=\delta_{jm}\delta_{nk}U_{il}.
$$

In the basis $\{U_{mn}\}$ of the carrier, ordered by the pair $(m,n)$, this operator has a single nonzero entry, equal to $1$, in the row $(i,l)$ and the column $(j,k)$. It is therefore the matrix unit

$$
E_{(i,l),(j,k)}
$$

of the complex sixteen-dimensional operator space, in the sense of *Matrix Representations Conventions*, §*The Unit Table*. As $(i,l)$ and $(j,k)$ run over the four pairs, the sixteen operators $U_{ij}[\,]U_{kl}$ run over the sixteen matrix units of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$. They are linearly independent and they span.

**The count.** There are $2\times2\times2\times2=16$ choices of $(i,j,k,l)$, and they give the $4\times4=16$ matrix units. The two counts agree, and the agreement is the computation.

### The Sixteen Products as a Basis

**The change of basis.** The coefficient units $e_\mu$ are linear combinations of the matrix units $U_{ij}$:

$$
e_\mu=\sum_{i,j=1}^{2}c_{\mu,ij}U_{ij},\qquad
U_{ij}=\sum_{\mu}d_{\mu,ij}e_\mu,
$$

with the element label written first and the matrix pair second, and the two $4\times4$ matrices $c$ and $d$ inverse to one another; the change is the Peirce change $C_{\Pi}$ of *Matrix Representations Conventions*, §*The Change $C_{\Pi}$*, read on the algebra rather than on the operator space.

**Theorem (the basis).** The sixteen products $e_\mu[\,]e_\nu$ are a basis of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

*Proof.* Expand each coefficient unit in the matrix units:

$$
e_\mu[\,]e_\nu=\sum_{i,j,k,l}c_{\mu,ij}c_{\nu,kl}\,U_{ij}[\,]U_{kl}.
$$

The sixteen operators $U_{ij}[\,]U_{kl}$ are a basis, by §*The Matrix-Unit Computation*. The coefficient matrix of the display is the tensor product $c\otimes c$, and $c$ is invertible; hence $c\otimes c$ is invertible, and the sixteen products are a basis.

**The span.** Every two-sided operator is a linear combination of the sixteen products, and every operator of the ambient space is a linear combination of the sixteen products; the span is the whole space, of complex dimension sixteen. The bilinear map $(\tilde Q,\tilde P)\mapsto T_{\tilde Q,\tilde P}$ is therefore surjective onto $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and its image is the cone of the decomposable elements inside the complex sixteen-dimensional space.

**The parameters and the operators.** The parameters are eight complex numbers, the operators they generate by linear combination are complex sixteen-dimensional, and the map is bilinear rather than linear. The count is not a contradiction: the eight parameters describe one decomposable tensor, and the sixteen complex dimensions are the span of all of them.

## The Ladder $1,4,7,16$

### The Chain

**The chain of sets.** The scalars, the one-sided families, the cone and the ambient space form the chain

$$
\mathbb{C}\cdot\mathrm I_4\ \subset\ \operatorname{End}_L(\mathbb{B})\ \subset\ \operatorname{End}_{LR}(\mathbb{B})\ \subset\ \operatorname{End}_{\mathbb{C}}(\mathbb{B}),
$$

with complex dimensions

$$
1\ <\ 4\ <\ 7\ <\ 16 .
$$

The first inclusion is $L_{\lambda e_t}=\lambda\mathrm I_4$; the second is $T_{\tilde Q,e_t}=L_{\tilde Q}$; the third is the definition of the two-sided operator as a product. Each inclusion is proper, because the complex dimensions are strictly increasing. The right family is a second copy of complex dimension four, incomparable with the left one, and the two meet in the scalars by *The Commutant of the Two Regular Families*.

**The middle dimension.** The complex dimension seven is the complex dimension of the cone: eight complex parameters minus the one-dimensional complex scaling orbit. The chain is a chain of sets, not of subspaces. The cone is not a subspace, and its linear span is the whole complex sixteen-dimensional space by §*The Generation Theorem*. The complex dimension seven is the dimension of the cone as an algebraic variety, not the dimension of a subspace containing it.

**The two sevens.** A second complex seven-dimensional object sits beside the cone: the linear sum $\operatorname{End}_L(\mathbb{B})+\operatorname{End}_R(\mathbb{B})$, of complex dimension $4+4-1=7$. The sum is a subspace and is not the cone; the cone is a monoid and is not a subspace. The two sevens are different objects with the same complex dimension, and they must not be identified.

### The Sum Is Not a Subalgebra

**Theorem (the sum).** The subspace $\operatorname{End}_L(\mathbb{B})+\operatorname{End}_R(\mathbb{B})$ has complex dimension seven and is not a subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$.

*Proof.* The complex dimension is $4+4-1=7$ by the intersection theorem of *The Commutant of the Two Regular Families*. For the failure of closure, take $L_{\vec e_x}$ and $R_{\vec e_x}$, both in the sum. Their product is $T_{\vec e_x,\vec e_x}$. If the sum were a subalgebra, this product would be $L_{\tilde A}+R_{\tilde B}$ for some $\tilde A,\tilde B$; the next paragraph shows that it is not.

Suppose $\vec e_xX\vec e_x=\tilde AX+X\tilde B$ for all $X$. At $X=e_t$, $-\!e_t=\tilde A+\tilde B$. At $X=\vec e_x$,

$$
-\vec e_x=\tilde A\vec e_x+\vec e_x\tilde B
=\tilde A\vec e_x-\vec e_x-\vec e_x\tilde A,
$$

so $\tilde A$ commutes with $\vec e_x$; then $\tilde B=-\!e_t-\tilde A$ commutes with $\vec e_x$ as well. Write $\tilde A=a e_t+b\vec e_x$ and $\tilde B=(-1-a)e_t-b\vec e_x$. At $X=\vec e_y$,

$$
\vec e_x\vec e_y\vec e_x=\vec e_y,\qquad
\tilde A\vec e_y+\vec e_y\tilde B
=(a-1-a)\vec e_y+(b+b)\vec e_z=-\vec e_y+2b\vec e_z,
$$

which cannot equal $\vec e_y$. Contradiction.

**The reading.** The two one-sided families generate, under addition, a complex seven-dimensional subspace, and under composition they generate the whole complex sixteen-dimensional algebra. The sum is the additive closure and is not a subalgebra; the cone is the multiplicative closure and is not a subspace. The generation theorem is the statement that the multiplicative closure, taken with linear combinations, reaches the whole ambient space.

## The Plain Adjoint

### $T_{\tilde Q,\tilde P}^{\approx}=T_{\tilde P,\tilde Q}$

**Theorem (the adjoint).** For the general plain bilinear form $\langle X,Y\rangle=\mathrm{Sc}(XY)$,

$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=T_{\tilde P,\tilde Q}.
$$

*Proof.* For all $X,Y$,

$$
\bigl\langle T_{\tilde Q,\tilde P}X,Y\bigr\rangle
=\mathrm{Sc}\bigl(\tilde QX\tilde PY\bigr)
=\mathrm{Sc}\bigl(X\tilde PY\tilde Q\bigr)
=\bigl\langle X,T_{\tilde P,\tilde Q}Y\bigr\rangle,
$$

by the cyclicity of the scalar part. The adjoint is unique by the non-degeneracy of the form.

**The swap.** The adjoint exchanges the two parameters. It does not conjugate either of them, and it does not keep the side: the left multiplier of the adjoint is the right multiplier of the operator. The swap is the two-sided form of the one-sided identities $(L_{\tilde Q})^{\approx}=R_{\tilde Q}$ and $(R_{\tilde P})^{\approx}=L_{\tilde P}$ of *The Four Adjoints of the Biquaternion Algebra in Examples*, §*Association as a Transpose*.

**The involution.** $(T_{\tilde Q,\tilde P})^{\approx\approx}=T_{\tilde Q,\tilde P}$, and $(T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S})^{\approx}=T_{\tilde S,\tilde R}T_{\tilde P,\tilde Q}$, the reversal of the composition.

### The Self-Adjoint Pairs

**Theorem (the self-adjoint criterion).** For $\tilde Q\neq0$, the operator $T_{\tilde Q,\tilde P}$ is self-adjoint exactly when the two parameters are proportional:

$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=T_{\tilde Q,\tilde P}
\iff \tilde P=\lambda\tilde Q\quad\text{for some }\lambda\in\mathbb{C}.
$$

The self-adjoint two-sided operators are therefore the scalar multiples of the diagonal operators $T_{\tilde Q,\tilde Q}$, together with the zero operator.

*Proof.* Write $A=\mathsf M_2(\tilde Q)\neq0$ and $B=\mathsf M_2(\tilde P)$. Self-adjointness is $AXB=BXA$ for every $X\in M_2(\mathbb{C})$. On the matrix units $X=E_{ij}$ this reads $A_{ik}B_{lj}=B_{ik}A_{lj}$ for all $i,j,k,l$. Choose $(k_0,i_0)$ with $A_{k_0i_0}\neq0$ and put $\lambda=B_{k_0i_0}/A_{k_0i_0}$; taking $i=k_0$, $k=i_0$ gives $B_{lj}=\lambda A_{lj}$ for all $l,j$, so $B=\lambda A$ and $\tilde P=\lambda\tilde Q$. Conversely, $\tilde P=\lambda\tilde Q$ makes the two sides equal. The argument uses no inverse, so it covers the zero divisors.

**The diagonal.** The operator $T_{\tilde Q,\tilde Q}$ is self-adjoint for every $\tilde Q$, including the zero divisors; it is the operator $X\mapsto\tilde QX\tilde Q$, and it is not an inner automorphism unless $\tilde Q$ is a unit.

### The Skew Pairs

**Theorem (the skew sector is trivial).** No nonzero two-sided operator is skew-adjoint:

$$
\bigl(T_{\tilde Q,\tilde P}\bigr)^{\approx}=-T_{\tilde Q,\tilde P}
\iff T_{\tilde Q,\tilde P}=0.
$$

*Proof.* Skew-adjointness is $BXA=-AXB$ for all $X$. On the matrix units, $B_{ik}A_{lj}=-A_{ik}B_{lj}$. If $A=0$ the operator is zero. Otherwise choose $(k_0,i_0)$ with $A_{k_0i_0}\neq0$ and put $\mu=-B_{k_0i_0}/A_{k_0i_0}$; then $B=\mu A$. Substituting back gives $2\mu AXA=0$ for all $X$, and $AXA$ is not identically zero for $A\neq0$, so $\mu=0$ and $B=0$. The zero operator is skew-adjoint.

**The reading.** The plain form has a self-adjoint sector and no skew sector among the nonzero two-sided operators. The asymmetry is the asymmetry of the swap: a self-adjoint pair is a pair of proportional parameters, and the proportionality is symmetric; a skew pair would need an antisymmetric proportionality, and the only antisymmetric scalar is zero.

## Isometries and Multiplicative Members

### The Isometries of the Plain Form

**Theorem (the isometries).** The operator $T_{\tilde Q,\tilde P}$ preserves the plain form,

$$
\bigl\langle T_{\tilde Q,\tilde P}X,T_{\tilde Q,\tilde P}Y\bigr\rangle=\langle X,Y\rangle\qquad\text{for all }X,Y,
$$

exactly when

$$
\tilde P\tilde Q=\pm e_t .
$$

Equivalently, $\tilde Q$ is a unit and $\tilde P=\pm\tilde Q^{-1}$, and the operator is $\pm\mathrm{Ad}_{\tilde Q}$.

*Proof.* If $T_{\tilde Q,\tilde P}$ preserves the form it is injective, because the form is non-degenerate, so both parameters are units. An invertible isometry has inverse its adjoint, so $T_{\tilde Q,\tilde P}T_{\tilde P,\tilde Q}=\mathrm{id}$. By the composition law the composite is $T_{\tilde Q\tilde P,\tilde Q\tilde P}$, and $T_{\tilde A,\tilde A}=\mathrm{id}$ exactly when $\tilde A$ is central with $\tilde A^2=e_t$, that is $\tilde A=\pm e_t$. Hence $\tilde Q\tilde P=\pm e_t$, and for units this is $\tilde P\tilde Q=\pm e_t$ and $\tilde P=\pm\tilde Q^{-1}$. Conversely, $\tilde P=\pm\tilde Q^{-1}$ makes $T_{\tilde Q,\tilde P}=\pm\mathrm{Ad}_{\tilde Q}$, and the inner automorphism and its negative preserve the form.

**The group.** The isometries of the family are the two cosets

$$
T_{\tilde Q,\tilde Q^{-1}}=\mathrm{Ad}_{\tilde Q},\qquad
T_{\tilde Q,-\tilde Q^{-1}}=-\mathrm{Ad}_{\tilde Q},
$$

with $\tilde Q$ a unit. The inner automorphism depends on $\tilde Q$ only through its class in $\mathbb{B}^{\times}/\mathbb{C}^{\times}$, so the group is

$$
\{\pm\mathrm{Ad}_{\tilde Q}\}\cong(\mathbb{B}^{\times}/\mathbb{C}^{\times})\times\{\pm1\},
$$

of complex dimension three. It is not all of $O_4(\mathbb{C})$, which has dimension six. The kernel of the parametrisation is $\{(\lambda e_t,\lambda^{-1}e_t)\}\cong\mathbb{C}^{\times}$, and the two cosets are the two components of the group.

### The Criterion $\tilde Q\tilde P=e_t$

**Theorem (the multiplicative members).** A nonzero operator $T_{\tilde Q,\tilde P}$ is multiplicative,

$$
T_{\tilde Q,\tilde P}(XY)=T_{\tilde Q,\tilde P}(X)\,T_{\tilde Q,\tilde P}(Y)\qquad\text{for all }X,Y,
$$

exactly when

$$
\tilde Q\tilde P=e_t .
$$

Then $\tilde P=\tilde Q^{-1}$ and $T_{\tilde Q,\tilde P}=\mathrm{Ad}_{\tilde Q}$, an automorphism of the algebra for every unit $\tilde Q$.

*Proof.* Multiplicativity reads

$$
\tilde QX\tilde P\,\tilde QY\tilde P=\tilde QXY\tilde P
\quad\text{for all }X,Y,
$$

that is $\tilde QX(\tilde P\tilde Q-e_t)Y\tilde P=0$ for all $X,Y$. Since $\tilde Q$ and $\tilde P$ are nonzero, the matrix model gives $\tilde P\tilde Q=e_t$: if $\tilde QX(\tilde P\tilde Q-e_t)\neq0$ for some $X$, then $BX\tilde P=0$ for all $X$ with $B\neq0$, which forces $B=0$ by testing on the matrix units and using $\tilde P\neq0$. Hence $\tilde P\tilde Q=e_t$, and then $\tilde P=\tilde Q^{-1}$ and $\tilde Q\tilde P=e_t$. The converse is immediate.

**The zero exception.** The zero operator is multiplicative, and its product of parameters is $0$, not $e_t$. The criterion is read on the nonzero operators.

**The partial law.** If the product $\tilde P\tilde Q$ is central, $\tilde P\tilde Q=\mu e_t$ with $\mu\in\mathbb{C}$, then

$$
T_{\tilde Q,\tilde P}(X)\,T_{\tilde Q,\tilde P}(Y)=\mu\,T_{\tilde Q,\tilde P}(XY)
$$

for all $X,Y$. The scalar is the central product of the parameters, not a norm. The genuine multiplicative case is $\mu=1$.

**Multiplicative and isometric.** A nonzero operator that is both multiplicative and an isometry is an inner automorphism $\mathrm{Ad}_{\tilde Q}$ with $\tilde Q$ a unit, without the minus: the isometry criterion allows $\tilde P\tilde Q=-e_t$, and the multiplicative criterion excludes it.

### The Absence of a Pin Group

**The quadratic form is not multiplicative.** Put $\mathfrak{Q}(\tilde Q)=\mathrm{Sc}(\tilde Q^2)$, the quadratic form polarised to the plain form. It is not multiplicative:

$$
\mathfrak{Q}\!\left(\frac{5e_t+4\vec e_x}{3}\right)=\mathfrak{Q}\!\left(\frac{5e_t+4\vec e_y}{3}\right)=1,
\qquad
\mathfrak{Q}\!\left(\frac{(5e_t+4\vec e_x)(5e_t+4\vec e_y)}{9}\right)=-\frac{431}{81}.
$$

The level set $\{\mathfrak{Q}=\pm1\}$ is therefore not closed under multiplication, and no scalar condition on one parameter cuts a subgroup out of the family.

**No pin group.** A pin group needs a multiplicative form whose level set is a subgroup. The isometry group of the family is only $\{\pm\mathrm{Ad}_{\tilde Q}\}$, of complex dimension three, and it is not a pin group. The pin group of the quadratic space is the one built in the Clifford algebra, of complex dimension six, and it is not contained in the family. The isometry condition is a condition on the pair, $\tilde P\tilde Q=\pm e_t$, not on either parameter alone.

**The reflections.** A reflection of the plain form in a direction of the vector subspace acts on that subspace with determinant $-1$, whereas $\mathrm{Ad}_{\tilde Q}$ acts there with determinant $+1$; $-\mathrm{Ad}_{\tilde Q}$ acts there with determinant $-1$, but it negates the centre, while the reflection fixes the centre. A reflection in a central direction negates the centre and is not $\pm\mathrm{Ad}_{\tilde Q}$; a reflection in a mixed direction moves the centre line, which $\pm\mathrm{Ad}_{\tilde Q}$ preserves. In every case the reflection is outside the family. The improper isometries live in the Clifford algebra, where the reflection in a non-isotropic vector $u$ is $\rho_u(v)=-uvu^{-1}$.

**The contrast.** The quaternionic twin of the corpus has a multiplicative norm, so its sandwich is an isometry exactly on the level set of the norm, and that level set is a group. Here the form carries no norm, nothing is selected, and the level set is not a group. The difference has one source: the plain form is the scalar part of the algebra's own product, and the product does not preserve its own scalar part.

## Worked Examples

**The identity and its multiples.** $T_{e_t,e_t}=\mathrm{id}$ is self-adjoint, form preserving and multiplicative. The central multiples $\lambda\,\mathrm{id}=T_{\lambda e_t,e_t}$ are self-adjoint for every $\lambda$, preserve the form only for $\lambda=\pm1$, and are multiplicative only for $\lambda=1$. The three criteria are genuinely different, and the example separates them.

**A mixed operator.** The operator $T_{\vec e_x,\vec e_y}$ has $\tilde P\tilde Q=\vec e_y\vec e_x=-\vec e_z$, so it is neither self-adjoint (the parameters are not proportional), nor form preserving ($-\vec e_z\neq\pm e_t$), nor multiplicative. Its adjoint is $T_{\vec e_y,\vec e_x}$, the pair exchanged, and the two operators differ.

**An inner automorphism.** For the pure unit $\vec e_x$, one has $\vec e_x^{-1}=-\vec e_x$, so

$$
\mathrm{Ad}_{\vec e_x}=T_{\vec e_x,\vec e_x^{-1}}=T_{\vec e_x,-\vec e_x}.
$$

The three criteria hold at once: the parameters are proportional with $\lambda=-1$, so the operator is self-adjoint; $\tilde P\tilde Q=(-\vec e_x)\vec e_x=e_t$, so it preserves the form; and $\tilde P=\tilde Q^{-1}$, so it is multiplicative. It is the least degenerate two-sided operator after the identity.

**A self-adjoint operator with a null parameter.** For $\tilde Q=e_t+i\vec e_z$, a zero divisor with $\tilde Q^2=2\tilde Q$, the diagonal operator $T_{\tilde Q,\tilde Q}$ is self-adjoint by the criterion with $\lambda=1$, although the parameter is not a unit. Self-adjointness is a condition on the pair, not on invertibility; the form-preserving criterion, by contrast, forces both parameters to be units.

**A diagonal operator multiplicative up to sign.** For the pure unit $\vec e_x$, the product of the parameters is $\vec e_x^2=-e_t$, central, so the partial law applies with the scalar $-1$:

$$
T_{\vec e_x,\vec e_x}(X)\,T_{\vec e_x,\vec e_x}(Y)=-T_{\vec e_x,\vec e_x}(XY).
$$

The operator $X\mapsto\vec e_xX\vec e_x$ is anti-multiplicative, and it is the negative of the inner automorphism $\mathrm{Ad}_{\vec e_x}$. The example separates the central-product family from the genuinely multiplicative operators.

## Summary

The two-sided operators are the products $T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P$ of a left and a right multiplication with independent parameters. They contain the one-sided operators at the boundary cases $\tilde P=e_t$ and $\tilde Q=e_t$, and they form a cone of complex dimension seven: eight parameters modulo the scaling $(\lambda\tilde Q,\lambda^{-1}\tilde P)$. The composition law is $T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\tilde S\tilde P}$, with the second slot reversed. The family is closed under composition and not under addition; the sum $\mathrm{id}+T_{\vec e_x,\vec e_x}$ is not a product.

The sixteen basis operators $e_\mu[\,]e_\nu$ are a basis of the ambient space, so the span of the family is the whole $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, of complex dimension sixteen. The ladder is $1,4,7,16$: the scalars, the one-sided families, the cone, the ambient space. The chain is a chain of sets, not of subspaces; the cone is not a subspace, and its span is the whole space. The linear sum of the two one-sided families is a complex seven-dimensional subspace and is not a subalgebra.

The plain adjoint exchanges the parameters, $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$. The self-adjoint operators are the scalar multiples of the diagonal operators, $\tilde P=\lambda\tilde Q$; no nonzero operator is skew-adjoint. The isometries are the two cosets $\pm\mathrm{Ad}_{\tilde Q}$, with $\tilde P\tilde Q=\pm e_t$, of complex dimension three; the multiplicative members are the inner automorphisms $\mathrm{Ad}_{\tilde Q}$, with $\tilde Q\tilde P=e_t$. The quadratic form is not multiplicative, so the family contains no pin group, and the reflections lie outside it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{\tilde Q,\tilde P}(X)=\tilde QX\tilde P$ | The two-sided operator of the pair; first subscript left, second right, argument third |
| $e_\mu[\,]e_\nu(X)=e_\mu Xe_\nu$ | The sixteen basis operators |
| $T_{\tilde Q,e_t}=L_{\tilde Q}$, $T_{e_t,\tilde P}=R_{\tilde P}$ | The one-sided boundary cases |
| $\operatorname{End}_{LR}(\mathbb{B})$ | The cone of the two-sided operators |
| $T_{\tilde Q,\tilde P}T_{\tilde R,\tilde S}=T_{\tilde Q\tilde R,\tilde S\tilde P}$ | The composition law; the second slot reverses |
| $(T_{\tilde Q,\tilde P})^n=T_{\tilde Q^n,\tilde P^n}$ | The powers |
| $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$ | The plain adjoint swaps the parameters |
| Self-adjoint $\iff\tilde P=\lambda\tilde Q$ | For $\tilde Q\neq0$; the diagonal operators and their multiples |
| Skew-adjoint $\iff T_{\tilde Q,\tilde P}=0$ | The skew sector is trivial |
| Isometry $\iff\tilde P\tilde Q=\pm e_t$ | The group $\{\pm\mathrm{Ad}_{\tilde Q}\}$ |
| Multiplicative, nonzero $\iff\tilde Q\tilde P=e_t$ | Then $T_{\tilde Q,\tilde P}=\mathrm{Ad}_{\tilde Q}$ |
| $\tilde P\tilde Q$ central $\implies$ multiplicative up to $\tilde P\tilde Q$ | The partial law |
| $1,4,7,16$ | Scalars, one-sided, cone, ambient |
| $\mathfrak{Q}(\tilde Q)=\mathrm{Sc}(\tilde Q^2)$ | The quadratic form of the plain form; not multiplicative |

## Further Reading

- [Two-Sided Operators on the Biquaternion Algebra](two-sided-operators-on-the-biquaternion-algebra.html), for the sixteen matrices, the coefficient matrix and the length.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the isomorphism that the generation theorem supports.
- [The Left Regular Operators on the Biquaternion Algebra](the-left-regular-operators-on-the-biquaternion-algebra.html) and [The Right Regular Operators on the Biquaternion Algebra](the-right-regular-operators-on-the-biquaternion-algebra.html), for the two boundary families.
- [The Commutant of the Two Regular Families](the-commutant-of-the-two-regular-families.html), for the intersection used in the ladder.
- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the association of the one-sided families and the four adjoints.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the plain form and its quadratic form.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the algebra's matrix units used in the generation theorem.
- [Matrix Representations Conventions](conventions-of-the-matrix-models.html), for the operator-space matrix units and the Peirce change.
- [Operator Family Conventions](conventions-of-the-operator-families.html), for the letters, the slots and the set names.
