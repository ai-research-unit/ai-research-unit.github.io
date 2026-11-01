# __The Sandwich, the Difference Family and the Adjoints of $M_n(\mathbb{C})$__

## Introduction

**The three questions.** Three constructions sit beside the two-sided products and are read through them: the **adjoints**, which are the two-sided products taken with respect to a form; the **sandwich** $\Theta_{A}=T_{A,A^{*}}$, which is the member whose second parameter is the star of the first; and the **difference family** $L_{A}-R_{B}$, which is the operator $X\mapsto AX-XB$ and is the general Sylvester operator. This article computes the three and relates them to the cone of products.

**The result in one line.** The transpose, the plain adjoint and the Hilbert–Schmidt adjoint act on the parameters and never exchange the two slots; the sandwich is a positive operator of rank $(\operatorname{rank}A)^{2}$ and a monoid under composition; and the difference family is a subspace of dimension $2n^{2}-1$ whose members are the intertwiners of the pair.

**The contrast that matters.** For the quaternionic plain form at $n=2$ the plain adjoint **exchanges the two slots**, $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$, and the isometry group is the small $\{\pm\mathrm{Ad}_{\tilde Q}\}$ of complex dimension three. For the trace forms on $M_{n}(\mathbb{C})$ the adjoint **conjugates each slot separately** and the isometry group is the large $\mathrm{U}(n)\times\mathrm{U}(n)$ modulo the scalars. **The difference is the difference of the two bilinear forms, one indefinite of signature $(1,3)$ and one split or definite, and it is not a difference of dimension.**

**Boundaries.** The products and the cone are *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*; the one-sided families are *The One-Sided Operators of $M_n(\mathbb{C})$*; the length is *The Length and the Two Ranks on $M_n(\mathbb{C})$*. At $n=2$ the plain adjoint and the types are *$M_4(\mathbb{C})$ Standard Peirce Representation : Operators*, §*The Plain Adjoint and the Types*, and the Hermitian sandwich of the algebra is Part V. The Sylvester operator on $M_{4}(\mathbb{C})$ is *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$*.

**Conventions.** The algebra is $M_{n}(\mathbb{C})$ of complex dimension $N=n^{2}$; the operator is $T_{A,B}(X)=AXB$ with matrix $B^{\mathsf T}\otimes A$. The transpose of a matrix is ${}^{\mathsf T}$, the conjugate transpose ${}^{*}$, the Hilbert–Schmidt adjoint of an operator ${}^{\dagger}$, the adjoint for the trace bilinear form ${}^{\approx}$. The trace form is $\langle X,Y\rangle_{\mathrm{tr}}=\operatorname{tr}(X^{\mathsf T}Y)$ and the Hilbert–Schmidt form is $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{*}Y)$; they are two different forms and are never exchanged.

## The Transpose and the Trace Form

### The Transpose

**Proposition.** For every pair,
$$
\bigl(T_{A,B}\bigr)^{\mathsf T}=T_{A^{\mathsf T},B^{\mathsf T}}.
$$

*Proof.* The matrix of the operator is $B^{\mathsf T}\otimes A$, whose transpose is $B\otimes A^{\mathsf T}=(A^{\mathsf T})^{\mathsf T}\otimes A^{\mathsf T}$, the matrix of $T_{A^{\mathsf T},B^{\mathsf T}}$.

**The transpose conjugates the two parameters and exchanges nothing.** This is already a contrast with the quaternionic plain form, where the adjoint exchanges the slots; the reason is that the transpose acts on each tensor factor separately, while the quaternionic adjoint acts on the product of the two.

**The transpose of the two one-sided families.** The proposition specialises to $(L_{A})^{\mathsf T}=L_{A^{\mathsf T}}$ and $(R_{B})^{\mathsf T}=R_{B^{\mathsf T}}$, so each copy is carried to itself and not to the other copy. The exchange of the two copies is the flip of *The One-Sided Operators of $M_n(\mathbb{C})$*, a different involution.

### The Trace Bilinear Form

**Definition.** The **trace bilinear form** on $M_{n}(\mathbb{C})$ is
$$
\langle X,Y\rangle_{\mathrm{tr}}=\operatorname{tr}(X^{\mathsf T}Y)=\sum_{i,j}X_{ij}Y_{ij}.
$$
It is complex-bilinear, symmetric and non-degenerate, and it is not the Hilbert–Schmidt form: it has no complex conjugation.

**It is indefinite.** In the real reading the form is the sum of $n^{2}$ products $X_{ij}Y_{ij}$ of the same sign, hence a split form of signature $(n^{2},n^{2})$: the isotropic vectors are the matrices with $X^{\mathsf T}X=0$, and they form a cone and not the single point $0$. **The definite form of the algebra is the Hilbert–Schmidt form and not this one.**

### The Plain Adjoint

**Theorem.** The adjoint of a two-sided operator for the trace bilinear form is the transpose, and
$$
\bigl(T_{A,B}\bigr)^{\approx}=T_{A^{\mathsf T},B^{\mathsf T}}.
$$

*Proof.* By the cyclicity of the trace,
$$
\bigl\langle T_{A,B}X,Y\bigr\rangle_{\mathrm{tr}}
=\operatorname{tr}\bigl((AXB)^{\mathsf T}Y\bigr)
=\operatorname{tr}\bigl(X^{\mathsf T}A^{\mathsf T}YB^{\mathsf T}\bigr)
=\bigl\langle X,T_{A^{\mathsf T},B^{\mathsf T}}Y\bigr\rangle_{\mathrm{tr}} .
$$

**The self-adjoint products.** A nonzero product is self-adjoint for the trace form exactly when its two parameters are symmetric, up to the scaling class:
$$
\bigl(T_{A,B}\bigr)^{\approx}=T_{A,B}\iff A^{\mathsf T}=\lambda A,\quad B^{\mathsf T}=\lambda^{-1}B,\quad|\lambda|=1 .
$$
The clean representative is the pair of symmetric matrices, and every class contains one.

**The isometries.** The operator preserves the trace form exactly when both parameters are complex orthogonal:
$$
\langle T_{A,B}X,T_{A,B}Y\rangle_{\mathrm{tr}}=\langle X,Y\rangle_{\mathrm{tr}}\iff A^{\mathsf T}A=\mathrm I_{n},\quad BB^{\mathsf T}=\mathrm I_{n}.
$$

*Proof.* The left side is $\langle X,T_{A^{\mathsf T}A,\,BB^{\mathsf T}}Y\rangle_{\mathrm{tr}}$, which equals $\langle X,Y\rangle_{\mathrm{tr}}$ for all $X,Y$ exactly when the operator $T_{A^{\mathsf T}A,BB^{\mathsf T}}$ is the identity, that is exactly when $A^{\mathsf T}A=\mathrm I_{n}$ and $BB^{\mathsf T}=\mathrm I_{n}$.

**The count.** The complex orthogonal group $\mathrm{O}(n,\mathbb{C})$ has complex dimension $n(n-1)/2$, so the isometry group of the trace form inside the family is $\mathrm{O}(n,\mathbb{C})\times\mathrm{O}(n,\mathbb{C})$ modulo the scalars, of complex dimension $n^{2}-n$. **The trace form is the form whose isometries are the orthogonal pairs, and this is the exact analogue of the quaternionic case with the orthogonal group in place of the small group of inner automorphisms.**

## The Hilbert–Schmidt Adjoint

### The Dagger

**Theorem.** The adjoint of a two-sided operator for the Hilbert–Schmidt form is
$$
\bigl(T_{A,B}\bigr)^{\dagger}=T_{A^{*},B^{*}}.
$$

*Proof.* The form is $\operatorname{tr}(X^{*}Y)$, and
$$
\bigl\langle T_{A,B}X,Y\bigr\rangle_{\mathrm{HS}}
=\operatorname{tr}\bigl(B^{*}X^{*}A^{*}Y\bigr)
=\operatorname{tr}\bigl(X^{*}A^{*}YB^{*}\bigr)
=\bigl\langle X,T_{A^{*},B^{*}}Y\bigr\rangle_{\mathrm{HS}} .
$$

**The dagger conjugates each slot and exchanges neither.** The two parameters are conjugated separately and their order is kept, which is the operator form of the fact that the Hilbert–Schmidt form is the tensor product of the Hilbert–Schmidt forms of the two slots.

**The composition with the length.** The dagger preserves the cone and the length:
$$
\ell\bigl(M^{\dagger}\bigr)=\ell(M),
$$
because the array of $M^{\dagger}$ is obtained from the array of $M$ by conjugating the entries and permuting the two index sets, and a permutation of the rows and of the columns preserves the rank. **The length is a unitary invariant of the operator, and so are its strata $\mathcal{C}_{r}$.**

### The Self-Adjoint and the Skew-Adjoint

**Theorem (the types).** Let $T=T_{A,B}$ be nonzero and put $\lambda$ the scalar of its class, $|\lambda|=1$.

- $T$ is self-adjoint exactly when its class contains a pair of Hermitian matrices.
- $T$ is skew-adjoint exactly when its class contains a pair with $A$ skew-Hermitian and $B$ Hermitian.

*Proof.* The equation $T^{\dagger}=T$ reads $T_{A^{*},B^{*}}=T_{A,B}$, which by the fibre theorem is $A^{*}=\lambda A$, $B^{*}=\lambda^{-1}B$; taking adjoints again gives $|\lambda|=1$, and rescaling the pair by $\mu$ with $\mu/\bar\mu=\lambda$ brings both parameters to the Hermitian case. The skew case reads $T_{A^{*},B^{*}}=T_{-A,B}$, that is $A^{*}=-\lambda A$ and $B^{*}=\lambda^{-1}B$, and the same rescaling brings the pair to the skew-Hermitian and Hermitian case.

**The sign is carried by the first slot and not by the two.** The asymmetry is not a convention: the two slots enter the product in opposite orders, so the sign of the adjoint equation reaches them with opposite signs, and only the first slot can carry the minus. **At $n=2$ the quaternionic plain form has no skew sector at all among the nonzero products; the Hilbert–Schmidt form has a large one, of real dimension $2n^{2}-1$ in the cone.**

**The count of the skew sector.** The pairs $(A,B)$ with $A$ skew-Hermitian and $B$ Hermitian form a real space of dimension $n^{2}+n^{2}=2n^{2}$, and the scaling by the unit circle is one real parameter, so the skew-adjoint products form a real cone of dimension $2n^{2}-1$: the same count as the whole cone over the reals, because the condition is real-linear.

### The Isometries

**Theorem.** The operator $T_{A,B}$ preserves the Hilbert–Schmidt form exactly when both parameters are unitary:
$$
T_{A,B}^{\dagger}T_{A,B}=\mathrm I_{N}\iff A^{*}A=\mathrm I_{n},\quad BB^{*}=\mathrm I_{n}.
$$

*Proof.* By the composition law, $T_{A^{*},B^{*}}T_{A,B}=T_{A^{*}A,\,BB^{*}}$, which is the identity exactly for a unitary pair.

**The group.** The isometries of the family form the group
$$
\{T_{A,B}:A,B\in\mathrm{U}(n)\}\cong\frac{\mathrm{U}(n)\times\mathrm{U}(n)}{\mathrm{U}(1)},
$$
of real dimension $2n^{2}-1$. At $n=2$ the dimension is $7$, the dimension of the cone.

**The unitary group of the algebra is smaller than the isometry group of one operator.** The group $\mathrm{PU}(n)$ acts on the algebra by conjugation, $X\mapsto UXU^{*}$, and this is the subfamily $T_{U,U^{*}}$ with $B=A^{*}$: the sandwich of a unitary element. **Every isometry of the family is a pair of unitaries acting on the two sides; only the diagonal of that group, the pairs $(U,U^{*})$, acts by automorphisms of the algebra.**

### The Contrast with the Biquaternion Form

**The three forms.** At $n=2$ the algebra carries three forms that are easily confused: the quaternionic scalar-part form $\mathrm{Sc}(XY)$, of signature $(1,3)$; the trace bilinear form $\operatorname{tr}(X^{\mathsf T}Y)$; and the Hilbert–Schmidt form $\operatorname{tr}(X^{*}Y)$, definite. The operator articles of the biquaternion category use the first.

**The three adjoints.** The first gives the slot exchange $(T_{\tilde Q,\tilde P})^{\approx}=T_{\tilde P,\tilde Q}$; the second gives the double conjugation of the transpose $T_{A^{\mathsf T},B^{\mathsf T}}$; the third gives $T_{A^{*},B^{*}}$. **The three formulas are three readings of the same cyclicity of the trace, applied to three different pairings, and none of them is the transpose of another.**

**The three isometry groups.** They are $\{\pm\mathrm{Ad}_{\tilde Q}\}$ of complex dimension three, $\mathrm{O}(2,\mathbb{C})\times\mathrm{O}(2,\mathbb{C})$ modulo the scalars of complex dimension two, and $\mathrm{U}(2)\times\mathrm{U}(2)$ modulo the scalars of real dimension seven. **The indefinite form has the smallest isometry group and the definite form the largest, and the count is a property of the form and not of the operator family.**

## The Sandwich

### The Definition and the Monoid

**Definition.** The **sandwich** by $A$ is
$$
\Theta_{A}=T_{A,A^{*}},\qquad \Theta_{A}(X)=AXA^{*}.
$$

**Theorem (the sandwich family is a monoid).** For all $A$ and $B$,
$$
\Theta_{A}\Theta_{B}=\Theta_{AB},\qquad \Theta_{\mathrm I_{n}}=\mathrm I_{N}.
$$

*Proof.* By the composition law, $T_{A,A^{*}}T_{B,B^{*}}=T_{AB,\,B^{*}A^{*}}=T_{AB,(AB)^{*}}$. The identity is the sandwich of the identity.

**The composition is not reversed.** The sandwich is the subfamily on which the two slots are tied by the star, and the reversal of the second slot is exactly undone by the star: $(AB)^{*}=B^{*}A^{*}$. **The sandwich family is a monoid isomorphic to the multiplicative monoid of the algebra, inside the monoid of all products.**

**The two-sided nature of the tie.** The map $A\mapsto\Theta_{A}$ is not injective: $\Theta_{A}=\Theta_{B}$ for nonzero $A,B$ exactly when $B=\lambda A$ with $|\lambda|=1$, by the fibre theorem and the reality of the star. The image is therefore a real cone of real dimension $2n^{2}-1$, and it is the **Hermitian subcone** of the complex cone.

### The Invariants

**Theorem.** Let $r=\operatorname{rank}A$. Then
$$
\operatorname{rank}\Theta_{A}=r^{2},\qquad
\operatorname{tr}\Theta_{A}=|\operatorname{tr}A|^{2},\qquad
\det\Theta_{A}=|\det A|^{2n}.
$$

*Proof.* The matrix is $A^{*\mathsf T}\otimes A=\bar A\otimes A$, whose rank is $r^{2}$, whose trace is $\operatorname{tr}\bar A\operatorname{tr}A$ and whose determinant is $(\det\bar A\det A)^{n}$.

**The rank is a square.** The sandwich of a rank-one element has rank one, the sandwich of a singular element is singular, and the sandwich of an invertible element has full rank. **The values of the rank of a sandwich are the squares $0,1,4,9,\dots,n^{2}$ and no others**, a proper subset of the products $rs$ of the general cone.

**The determinant is a modulus raised to the power $2n$, hence real and non-negative.** The sandwich is the member of the cone on which the determinant of the operator is real; the general product has an arbitrary complex determinant and the sandwich has a non-negative one.

### The Kernel and the Positivity

**Theorem.** The sandwich is a positive semidefinite operator for the Hilbert–Schmidt form, and its kernel has dimension $n^{2}-r^{2}$:
$$
\langle \Theta_{A}X,X\rangle_{\mathrm{HS}}=\|AX\|_{\mathrm{F}}^{2}\ge0,\qquad
\ker\Theta_{A}=\{X:AXA^{*}=0\}.
$$

*Proof.* The form is $\operatorname{tr}((AXA^{*})^{*}X)=\operatorname{tr}(AX^{*}A^{*}X)=\operatorname{tr}((AX)^{*}(AX))=\|AX\|_{\mathrm F}^{2}$, which is a sum of squares. The kernel is the set on which this norm vanishes, and its dimension is $n^{2}-r^{2}$ by the rank formula above.

**The positivity is the reason the sandwich is the object of the polar decomposition and of the states.** For $A$ Hermitian, $\langle\Theta_{A}X,X\rangle_{\mathrm{HS}}=\operatorname{tr}(A^{2}X^{*}X)$, so the sandwich of a positive element is the operator of a positive quadratic form, and the map $A\mapsto\Theta_{A}$ carries the cone of positive elements into the cone of positive operators. **The complex cone of products has no positivity; the sandwich subcone has it, and the two carry the same real dimension by accident of the counting.**

**The eigenstructure.** Let $A$ be diagonalisable with eigenbasis $u_{1},\dots,u_{n}$ and eigenvalues $\lambda_{1},\dots,\lambda_{n}$. The $n^{2}$ rank-one matrices $u_{i}u_{j}^{*}$ are a basis of the algebra and satisfy
$$
\Theta_{A}\bigl(u_{i}u_{j}^{*}\bigr)=\lambda_{i}\bar\lambda_{j}\,u_{i}u_{j}^{*},
$$
so the spectrum of the sandwich is the $n^{2}$ numbers $\lambda_{i}\bar\lambda_{j}$ and the sandwich is diagonal in that basis. The spectral projector of $\Theta_{A}$ at the value $\lambda_{i}\bar\lambda_{j}$ is the two-sided operator $T_{P_{i},P_{j}}$ of the two spectral projectors of $A$; **the sandwich carries the spectral data of the element into the two-sided operators, with one index on each side.**

## The Difference Family

### The Sylvester Operator

**Definition.** The **difference operator** of the pair is
$$
L_{A}-R_{B}:X\longmapsto AX-XB,
$$
the general **Sylvester operator** of the pair.

**The matrix.** In the column-stacking basis,
$$
[L_{A}-R_{B}]=\mathrm I_{n}\otimes A-B^{\mathsf T}\otimes\mathrm I_{n},
$$
the Kronecker difference, of trace $n(\operatorname{tr}A-\operatorname{tr}B)$.

**The kernel.** The kernel is the space of intertwiners:
$$
\ker(L_{A}-R_{B})=\{X:AX=XB\},
$$
which for $A=B$ is the centraliser of $A$, of dimension at least $n$, and for a pair with disjoint spectra is zero.

**The invertibility criterion.** The operator is invertible exactly when the spectra are disjoint, $\operatorname{spec}A\cap\operatorname{spec}B=\varnothing$, because the eigenvalues of the difference are the differences $\lambda_{i}(A)-\lambda_{j}(B)$. This is the criterion of *The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$*, and it holds at every $n$ with the same proof: the matrix $\mathrm I\otimes A-B^{\mathsf T}\otimes\mathrm I$ is triangularised by the triangular forms of $A$ and $B$.

### The Span

**Theorem.** The difference family spans a subspace of complex dimension $2n^{2}-1$:
$$
\dim\operatorname{span}\{L_{A}-R_{B}:A,B\in M_{n}(\mathbb{C})\}=2n^{2}-1 .
$$

*Proof.* The map $(A,B)\mapsto L_{A}-R_{B}$ is linear from $2n^{2}$ dimensions, and its kernel is the set of pairs with $L_{A}=R_{B}$. Such a pair satisfies $AX=XB$ for all $X$; with $X=I$ this gives $A=B$, and then $A$ is scalar, so the kernel is the line $\{(\lambda\mathrm I_{n},\lambda\mathrm I_{n})\}$. The image has dimension $2n^{2}-1$.

**The same number as the cone, and a different object.** The cone of products has dimension $2n^{2}-1$ and is not a subspace; the span of the differences has dimension $2n^{2}-1$ and is a subspace. The two meet in the scalars, and neither contains the other. **At $n=4$ the number is $31$, which is the count of the Sylvester article for the algebra $M_{4}(\mathbb{C})$ read as an algebra of dimension sixteen.**

**The sum family is a subspace and not a subalgebra.** The family $\{L_{A}+R_{B}\}$ is the same subspace, since $L_{A}+R_{B}=L_{A}-R_{-B}$. It is not closed under composition: $(L_{A}+R_{B})(L_{C}+R_{D})=L_{AC}+R_{DB}+T_{A,D}+T_{C,B}$, which contains two product terms and is not a difference in general. **The product family is closed under multiplication and is not a subspace; the difference family is a subspace and is not closed under multiplication, and the two facts are the two halves of the same asymmetry.**

### The Polarisation

**Theorem.** For all $A$ and $B$,
$$
2T_{A,B}=\bigl(L_{A}+R_{B}\bigr)^{2}-L_{A^{2}}-R_{B^{2}}.
$$

*Proof.* The two one-sided operators commute, so the square of the sum is $L_{A^{2}}+2L_{A}R_{B}+R_{B^{2}}$.

**The cone is the quadratic image of the subspace.** The polarisation writes every product as a quadratic expression in the difference family, and with it every operator of length $r$ as a quadratic expression in $2r$ one-sided operators. **The two-sided products are not a linear object at all: they are the polarisation of the sum family, and this is the reason the cone is a cone and not a subspace.**

**The trace of the polarisation.** The trace of the square of the sum is not the square of the sum of the traces, because the cross term is the trace of a product and not a product of traces:
$$
\operatorname{tr}(L_{A}+R_{B})^{2}=n\operatorname{tr}A^{2}+2\operatorname{tr}A\operatorname{tr}B+n\operatorname{tr}B^{2}.
$$
With $\operatorname{tr}L_{A^{2}}=n\operatorname{tr}A^{2}$ and $\operatorname{tr}R_{B^{2}}=n\operatorname{tr}B^{2}$ the polarisation gives $2\operatorname{tr}T_{A,B}=2\operatorname{tr}A\operatorname{tr}B$, which is the trace formula of the products recovered from the one-sided data.

## Summary

The transpose of a two-sided operator is $T_{A^{\mathsf T},B^{\mathsf T}}$ and is also its adjoint for the trace bilinear form; the Hilbert–Schmidt adjoint is $T_{A^{*},B^{*}}$. Both conjugate the two parameters and neither exchanges the slots, and this is the contrast with the quaternionic plain form, whose adjoint is the slot exchange. The isometry groups are $\mathrm{O}(n,\mathbb{C})\times\mathrm{O}(n,\mathbb{C})$ modulo the scalars for the trace form and $\mathrm{U}(n)\times\mathrm{U}(n)$ modulo the scalars for the Hilbert–Schmidt form, of complex dimension $n^{2}-n$ and real dimension $2n^{2}-1$.

The sandwich $\Theta_{A}=T_{A,A^{*}}$ is a monoid under composition, $\Theta_{A}\Theta_{B}=\Theta_{AB}$, positive semidefinite for the Hilbert–Schmidt form, of rank $r^{2}$, of trace $|\operatorname{tr}A|^{2}$, of determinant $|\det A|^{2n}$, and of kernel dimension $n^{2}-r^{2}$. Its image is the real cone of real dimension $2n^{2}-1$.

The difference family $L_{A}-R_{B}$ is the general Sylvester operator, with kernel the intertwiners, invertible exactly for disjoint spectra, and spanning a subspace of dimension $2n^{2}-1$. The polarisation $2T_{A,B}=(L_{A}+R_{B})^{2}-L_{A^{2}}-R_{B^{2}}$ writes every product as a quadratic expression in the difference family. **The products are a cone, the differences a subspace, the sandwiches a positive monoid; the three objects carry the same dimension count and three different structures.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(T_{A,B})^{\mathsf T}=T_{A^{\mathsf T},B^{\mathsf T}}$ | the transpose |
| $\langle X,Y\rangle_{\mathrm{tr}}=\operatorname{tr}(X^{\mathsf T}Y)$ | the trace bilinear form, split of signature $(n^{2},n^{2})$ |
| ${}^{\approx}$ | the adjoint for the trace form, equal to the transpose |
| $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{*}Y)$ | the Hilbert–Schmidt form, definite |
| ${}^{\dagger}$ | the Hilbert–Schmidt adjoint, $T_{A^{*},B^{*}}$ |
| $\Theta_{A}=T_{A,A^{*}}$ | the sandwich, $X\mapsto AXA^{*}$ |
| $r$ | the rank of $A$, giving $\operatorname{rank}\Theta_{A}=r^{2}$ |
| $L_{A}-R_{B}$ | the Sylvester operator $X\mapsto AX-XB$ |
| $2n^{2}-1$ | the dimension of the cone, of the skew sector and of the difference span |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the Sylvester equation, the Kronecker sum and the criterion of the disjoint spectra.
- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the sandwich $A\mapsto AXA^{*}$ and the positivity of the Hilbert–Schmidt form.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the cone and its two boundaries.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the two copies and the flip.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the invariance of the length under the dagger.
- [$M_4(\mathbb{C})$ Standard Peirce Representation : Operators](m4c-standard-peirce-representation-operators.html), for the plain adjoint and the three types at $n=2$.
- [The Sylvester Operator and the Kronecker Sum of $M_4(\mathbb{C})$](the-sylvester-operator-and-the-kronecker-sum-of-m4c.html), for the difference operator at $n=4$.
