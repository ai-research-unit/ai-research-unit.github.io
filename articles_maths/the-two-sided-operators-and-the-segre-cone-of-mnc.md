# __The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$__

## Introduction

**The question.** An operator of the form $X\mapsto AXB$ is the product of a left and a right multiplication. At $n=2$ the same object is the biquaternion two-sided operator, of which the corpus already has three accounts: the abstract family, the sixteen basis operators in the Peirce frame, and the coefficient matrix computed entry by entry. This article states the construction for $M_{n}(\mathbb{C})$, where the two parameters are $n\times n$ matrices, and computes the set they fill inside the $n^{4}$ dimensions of the endomorphism algebra.

**The result in one line.** The products fill a cone of complex dimension $2n^{2}-1$, closed under multiplication, with group of units $(\mathrm{GL}_{n}\times\mathrm{GL}_{n})/\mathbb{C}^{\times}$; the cone is the set of pure tensors of $M_{n}\otimes M_{\mathrm{opp},n}$ and its projectivisation is the Segre variety $\mathbb{P}^{n^{2}-1}\times\mathbb{P}^{n^{2}-1}$.

**The three numbers.** The parametrisation has $2n^{2}$ complex parameters, its generic fibre is a single scaling orbit of dimension one, and the image has dimension $2n^{2}-1$. At $n=2$ this is $8-1=7$, the dimension of the cone of the biquaternion algebra; at $n=3$ it is $17$; at $n=4$ it is $31$.

**Boundaries.** The one-sided families are *The One-Sided Operators of $M_n(\mathbb{C})$*; the general construction is *The Regular Representation in Dimension $n$*; the coefficient array and the length are *The Length and the Two Ranks on $M_n(\mathbb{C})$*; the sandwich, the adjoints and the difference family are *The Sandwich, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*. At $n=2$ the abstract family is *Operators Acting 2 Side*, the frame and the sixteen basis operators are *$M_4(\mathbb{C})$ Pauli Representation : Operators*, and the entry-by-entry array is *The Coefficient Matrix of a Two-Sided Operator: A Worked Computation*. The Hermitian sandwich is Part V.

**Conventions.** The algebra is $A=M_{n}(\mathbb{C})$ of complex dimension $N=n^{2}$; the operator space is $\operatorname{End}(A)$, of dimension $N^{2}=n^{4}$. The operator is $L_{A}R_{B}$, acting by $L_{A}R_{B}(X)=AXB$. In the column-stacking basis $L_{A}=\mathrm I_{n}\otimes A$, $R_{B}=B^{\mathsf T}\otimes\mathrm I_{n}$ and therefore
$$
[L_{A}R_{B}]=B^{\mathsf T}\otimes A .
$$
The identity operator is $\mathrm I_{N}=[L_{I}R_{I}]$. Rank is written of a matrix and of an operator; the length is written $\ell$.

## The Two-Sided Operator

### The Definition and the Matrix

**Definition.** The **two-sided operator** of the pair $(A,B)$ is
$$
L_{A}R_{B},\qquad L_{A}R_{B}(X)=AXB .
$$

**Proposition (the Kronecker form).** In the column-stacking basis,
$$
[L_{A}R_{B}]=B^{\mathsf T}\otimes A,
$$
an $N\times N$ matrix of $n^{2}$ blocks of size $n$, the block $(i,j)$ being $B_{ji}A$, because the $i$-th row of $B^{\mathsf T}$ is the $i$-th column of $B$ read across.

*Proof.* The product of the two matrices is $(B^{\mathsf T}\otimes\mathrm I_{n})(\mathrm I_{n}\otimes A)=B^{\mathsf T}\otimes A$, and the block form follows from the definition of the Kronecker product.

**The order of the two factors is not a choice.** The two multiplications commute, so $L_{A}R_{B}=R_{B}L_{A}$, and the operator is well defined by the unordered pair. What the display records is a different fact: in the tensor slot the left parameter occupies the second factor and the right parameter the first, because the transpose of the right parameter is what reaches the column-stacking matrix. **The letter names the action and the slot names the position, and the two do not coincide.**

**The two one-sided members.** With the other parameter the identity,
$$
L_{A}R_{I}=L_{A},\qquad L_{I}R_{B}=R_{B},
$$
so both one-sided families lie in the product set. This is the first of the two boundary cases, and it shows that the product set is not a small perturbation of the two copies but contains them.

### The Scaling and the Fibre

**Bilinearity.** The map $(A,B)\mapsto L_{A}R_{B}$ is complex-bilinear:
$$
L_{\lambda A+\mu A'}R_{B}=\lambda L_{A}R_{B}+\mu L_{A'}R_{B},\qquad
L_{A}R_{\lambda B+\mu B'}=\lambda L_{A}R_{B}+\mu L_{A}R_{B'}.
$$
It is not complex-linear in the pair, and consequently its image is a cone and not a subspace.

**The scaling orbit.** For $\lambda\in\mathbb{C}^{\times}$,
$$
L_{\lambda A}R_{\lambda^{-1}B}=L_{A}R_{B},
$$
because the two scalars cancel in the product $(\lambda A)X(\lambda^{-1}B)$. The group $\mathbb{C}^{\times}$ acts on the parameter space $M_{n}\times M_{n}$ without fixed points away from the origin, and the factorisation map is constant on the orbits.

**Theorem (the fibre).** Let $A,B,C,D$ be nonzero. Then
$$
L_{A}R_{B}=L_{C}R_{D}\iff C=\lambda A,\ D=\lambda^{-1}B\ \text{for some }\lambda\in\mathbb{C}^{\times}.
$$

*Proof.* The implication from right to left is the scaling identity. For the other, $AXB=CXD$ for every $X$. Take $X=E_{ij}$: the entry $(k,l)$ of the identity reads $A_{ki}B_{jl}=C_{ki}D_{jl}$ for all $i,j,k,l$. Choose $(k_{0},i_{0})$ with $A_{k_{0}i_{0}}\ne0$ and $(j_{0},l_{0})$ with $B_{j_{0}l_{0}}\ne0$, and put $\lambda=C_{k_{0}i_{0}}/A_{k_{0}i_{0}}$. Fixing $k=k_{0}$ and $i=i_{0}$ gives $D_{jl}=\lambda^{-1}B_{jl}$ for all $j,l$, and fixing $j=j_{0}$ and $l=l_{0}$ gives $C_{ki}=\lambda A_{ki}$ for all $k,i$.

**The dimension.** The parameter space has complex dimension $2n^{2}$ and the generic fibre dimension one, so the image has complex dimension
$$
2n^{2}-1 .
$$
At $n=2$ this is $7$, at $n=3$ it is $17$, at $n=4$ it is $31$.

### The Zero Set and the Injectivity

**Proposition (the product vanishes exactly when a parameter does).**
$$
L_{A}R_{B}=0\iff A=0\ \text{or}\ B=0 .
$$

*Proof.* One direction is immediate. For the other, suppose $A$ and $B$ are both nonzero; choose $(a,b)$ with $A_{ab}\ne0$ and $(c,d)$ with $B_{cd}\ne0$, and evaluate on $E_{bc}$. The entry $(a,d)$ of $A E_{bc}B$ is $A_{ab}B_{cd}\ne0$, so the operator is nonzero.

**The vertex.** The zero operator is the image of every pair with a zero parameter, that is of the union of the two subspaces $A=0$ and $B=0$. It is the vertex of the cone, and it is the only point at which the fibre is not a scaling orbit: it is the whole union of the two $n^{2}$-dimensional subspaces.

**The injectivity in each slot.** With one parameter fixed at the identity the map is injective in the other, by the faithfulness of the one-sided representations. The same holds for every nonzero fixed parameter: if $L_{A}R_{B}=0$ with $B\ne0$, the zero-set proposition forces $A=0$, so the linear map $A\mapsto L_{A}R_{B}$ has trivial kernel and is injective for every $B\ne0$, and symmetrically for every $A\ne0$. **The only degenerate fixed parameter is the zero one, where the map is identically zero.**

## The Cone

### The Image Is a Cone

**Proposition.** The product set
$$
\mathcal{C}=\{L_{A}R_{B}:A,B\in M_{n}(\mathbb{C})\}
$$
is a closed algebraic cone, stable under multiplication, and not a subspace.

*Proof.* The cone property is the bilinearity. The closedness and the algebraic character are the rank condition of the companion article: $\mathcal{C}=\{M:\operatorname{rank}c(M)\le1\}$, cut out by the $2\times2$ minors of the coefficient array, which are polynomial. It is not a subspace because it is not closed under addition: for $n\ge2$ the sum $L_{I}R_{I}+L_{E_{11}}R_{E_{11}}$ of two products is not one, its coefficient array being the sum of two independent rank-one arrays.

**The cone is a set of pure tensors.** Under the isomorphism $M_{n}\otimes M_{\mathrm{opp},n}\to\operatorname{End}(M_{n})$ the product $L_{A}R_{B}$ is the image of the elementary tensor $A\otimes B_{\mathrm{opp}}$. Hence
$$
\mathcal{C}=\{A\otimes B_{\mathrm{opp}}\}=\text{the decomposable tensors of }M_{n}\otimes M_{\mathrm{opp},n} .
$$
**This is the abstract reason for all the properties of the set**: the pure tensors of a tensor square form a cone, their projectivisation is a Segre variety, and their dimension is $2N-1$ and not $N^{2}$.

### The Segre Variety

**The projective image.** The cone is stable under scaling, so it has a projectivisation inside $\mathbb{P}^{N^{2}-1}$, the ambient projective space of complex dimension $N^{2}-1=n^{4}-1$. The projectivisation of the pure tensors is
$$
\mathbb{P}^{N-1}\times\mathbb{P}^{N-1}=\mathbb{P}^{n^{2}-1}\times\mathbb{P}^{n^{2}-1},
$$
of complex dimension $2(N-1)=2n^{2}-2$, one less than the cone it closes.

**The count.** The Segre variety has dimension $2n^{2}-2$ and the cone over it has dimension $2n^{2}-1$; the ambient projective space has dimension $n^{4}-1$ and the ambient affine space $n^{4}$. At $n=2$ the Segre variety is $\mathbb{P}^{3}\times\mathbb{P}^{3}$ of dimension six inside $\mathbb{P}^{15}$, which is the count of the Pauli Representation article.

**The two rulings.** The two families of linear spaces of the Segre variety are the two one-sided families: fixing $B=I$ gives the copy $\mathbb{P}(M_{n})$ of the left multiplications, and fixing $A=I$ gives the copy of the right multiplications. The two copies meet in the single point of the scalars. **The copies are linear spaces inside the cone and not generators of it**: their linear span is the subspace of dimension $2n^{2}-1$ of the companion article, the sums of a left and a right multiplication, and a generic product is not in that span.

### The Dimension of the Strata

**The rank stratification of the cone.** The cone is stratified by the rank of the parameters. Write $r=\operatorname{rank}A$ and $s=\operatorname{rank}B$; the stratum of pairs of ranks $(r,s)$ has dimension
$$
r(2n-r)+s(2n-s)-1
$$
when both parameters are nonzero, the subtraction of one being the scaling. At $n=2$ the strata are $(1,1)$, $(1,2)$, $(2,1)$ and $(2,2)$, of complex dimensions $5,6,6,7$. **The stratum $(2,2)$ is open and dense, so the cone is the closure of the products of two units**; the smaller strata are the degenerations on which one parameter loses rank.

**The singular locus is the vertex alone.** The Segre variety is smooth, so the cone over it is smooth away from the origin: at every point of the cone other than $0$ the derivative of the parametrisation $(A,B)\mapsto L_{A}R_{B}$ has rank $2n^{2}-1$, the dimension of the cone. The two rulings are smooth subvarieties of a smooth open part, and the only singular point is the zero operator.

## The Invariants

### The Three Formulas

**Theorem.** For every pair,
$$
\operatorname{rank}L_{A}R_{B}=\operatorname{rank}A\cdot\operatorname{rank}B,\qquad
\operatorname{tr}L_{A}R_{B}=\operatorname{tr}A\cdot\operatorname{tr}B,\qquad
\det L_{A}R_{B}=(\det A\cdot\det B)^{n}.
$$

*Proof.* The matrix is the Kronecker product $B^{\mathsf T}\otimes A$. The rank of a Kronecker product is the product of the ranks; the trace is the product of the traces; and for two matrices of size $n$ the determinant of the Kronecker product is $(\det B^{\mathsf T})^{n}(\det A)^{n}$.

**The determinant is not a norm.** At $n=2$ the formula reads $\det T=(\det A\det B)^{2}$, which is the square of the product of the two norms. The fourth power of a complex number is not the biquaternion norm of anything, and this is why the article on the trace and the determinant of the biquaternion representation keeps the two notions apart. **The determinant of the operator is a multiplicative character of the pair and carries no positivity.**

**The trace is the pairing of the two parameters.** The formula $\operatorname{tr}L_{A}R_{B}=\operatorname{tr}A\operatorname{tr}B$ says that the trace of the two-sided operator is the product of the two scalar parts, and therefore that the trace sees only the scalar parts. The traceless parts of the two parameters are invisible to the trace and visible to the determinant and the rank.

### The Attained Ranks

**Theorem.** The rank of a product takes exactly the values
$$
\operatorname{rank}L_{A}R_{B}=rs,\qquad 0\le r,s\le n .
$$

*Proof.* The rank of $A$ and the rank of $B$ each take every value from $0$ to $n$, independently, and the rank of the product is their product.

**The consequence.** The set of attained ranks is the multiplication table of $\{0,1,\dots,n\}$ against itself. At $n=2$ it is $\{0,1,2,4\}$ and the value $3$ is missing; at $n=3$ it is $\{0,1,2,3,4,6,9\}$ and the values $5,7,8$ are missing; at $n=4$ it is $\{0,1,2,3,4,6,8,9,12,16\}$ and the values $5,7,10,11,13,14,15$ are missing. **No product has rank strictly between $n$ and $n^{2}$ unless that number factors through $n$, and in particular no product has a prime rank above $n$.**

**The two ends.** The rank $n^{2}$ is attained exactly by the pairs of units: the product is invertible exactly when both parameters are. The rank one is attained by every pair of rank-one parameters, and more generally by every pair whose ranks multiply to one. The rank zero is the vertex.

**The comparison with the biquaternion case.** At $n=2$ the four values $0,1,2,4$ are the values of the biquaternion article, and the missing value $3$ is the reason the product set is not a union of determinantal strata of every rank. **The gap at $3$ is the first trace of the general arithmetic of $n$, and it is visible already at the smallest case.**

## The Monoid

### The Composition

**Theorem (the composition law).** For all four parameters,
$$
L_{A}R_{B}\,L_{C}R_{D}=L_{AC}R_{DB}.
$$

*Proof.* Apply the left side to $X$: $A(CXD)B=(AC)X(DB)$.

**The order of the second slot is reversed.** The pair composes as $(A,B)(C,D)=(AC,DB)$, so the second slot multiplies in the reverse order. This is the semigroup of the biquaternion article, and it is the product in the tensor algebra $M_{n}\otimes M_{\mathrm{opp},n}$ read on its two slots: the first factor multiplies on the left and the second on the right, and a right action composes in reverse.

**Powers.** The composition gives
$$
(L_{A}R_{B})^{k}=L_{A^{k}}R_{B^{k}},
$$
for $k\ge1$, and the identity operator is $L_{I}R_{I}$. In particular the powers of a two-sided operator are two-sided, and the one-parameter family $\{L_{e^{tX}}R_{e^{tY}}\}$ is a one-parameter subgroup of the group of units.

### The Group of Units

**Theorem.** The set of invertible products is
$$
\{L_{A}R_{B}:A,B\in\mathrm{GL}_{n}(\mathbb{C})\},
$$
and it is the image of $\mathrm{GL}_{n}(\mathbb{C})\times\mathrm{GL}_{n}(\mathbb{C})$; since the fibre of the parametrisation is the line of scalings it is isomorphic to the quotient $(\mathrm{GL}_{n}\times\mathrm{GL}_{n})/\mathbb{C}^{\times}$, of complex dimension $2n^{2}-1$.

*Proof.* The inverse of $L_{A}R_{B}$ is $L_{A^{-1}}R_{B^{-1}}$, by the composition law, so the products of units are invertible and form a group. The pair $(A,B)$ is recovered from the operator by the fibre theorem up to scaling; the map $(A,B)\mapsto L_{A}R_{B}$ restricted to units has kernel $\{(\lambda I,\lambda^{-1}I)\}$ of dimension one, so the group is the quotient $(\mathrm{GL}_{n}\times\mathrm{GL}_{n})/\mathbb{C}^{\times}$, of complex dimension $2n^{2}-1$, the same count as the cone.

**The two counts are the same number and different objects.** The cone has dimension $2n^{2}-1$ and contains non-invertible members; the group of units has dimension $2n^{2}-1$ and is open inside the cone. **The cone is the closure of the group of units, and the smaller strata are the degenerations in which one parameter loses rank; this is the precise sense in which the two-sided family is a group that has been allowed to degenerate.**

**The monoid is not a group and the failure is the zero.** The product set contains the zero operator, which has no inverse, so the family is a monoid with zero. It is regular in the semigroup sense: every member has a generalised inverse, because $L_{A}R_{B}L_{A^{-}}R_{B^{-}}L_{A}R_{B}$ for a reflexive generalised inverse $A^{-}$ of $A$ and $B^{-}$ of $B$.

## The Two Boundaries and the Sandwich

**The left and right boundaries.** The two copies are the boundary cases of the cone:
$$
L_{A}R_{I}=L_{A},\qquad L_{I}R_{B}=R_{B},
$$
of dimension $n^{2}$ each inside the cone of dimension $2n^{2}-1$. Their intersection is the scalars. A generic product lies in neither copy, and the generic product is not a one-sided operator.

**The sandwich.** The **sandwich** is the member with the second parameter the conjugate transpose of the first,
$$
\mathrm{Sd}_{A}=L_{A}R_{A^{*}},\qquad \mathrm{Sd}_{A}(X)=AXA^{*}.
$$
It is a real subcone of the complex cone, of real dimension $2n^{2}-1$, and it is the subject of *The Sandwich, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*. The word *Hermitian* in the biquaternion articles refers to the same choice of the second slot, and the subcone is real and not complex because the star is antilinear.

**The diagonal of the pair space.** The products with $A=B$ form the **diagonal subcone** $\{L_{A}R_{A}\}$ of complex dimension $n^{2}$, on which the scaling acts by $\lambda^{2}$ and not by $\lambda$. The diagonal is not the sandwich: it is complex, of dimension $n^{2}$, and it is not the set of self-adjoint products either, since the dagger of $L_{A}R_{A}$ is $L_{A^{*}}R_{A^{*}}$, again diagonal, and it equals $L_{A}R_{A}$ only when $A$ is a scalar multiple of a normal matrix.

## The Case $n=2$

**The identification.** At $n=2$ the algebra is the biquaternion algebra $\mathbb{B}$, the operator space is $M_{4}(\mathbb{C})$, the parameters are two biquaternions, and the formulas read
$$
\operatorname{rank}T=rs\in\{0,1,2,4\},\qquad \operatorname{tr}T=4Q_{t}P_{t},\qquad \det T=\langle\tilde Q\rangle_{\natural}^{2}\langle\tilde Q_2\rangle_{\natural}^{2},
$$
the last by $\det\mathsf M_{2}(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ and the general formula $\det T=(\det A\det B)^{2}$. The dimension of the cone is $7$, its projectivisation is $\mathbb{P}^{3}\times\mathbb{P}^{3}$ of dimension six, and the group of units is $(\mathrm{GL}_{2}\times\mathrm{GL}_{2})/\mathbb{C}^{\times}$, of complex dimension $7$.

**What is the same and what is not.** The cone, the fibre, the composition law, the rank formula, the trace formula and the determinant formula are the same statements at every $n$. The biquaternion articles add three things that the general case does not see: the Clifford frame and the sixteen basis operators, the gauge of the Peirce frame, and the two conjugate-linear involutions of the algebra. **The general article owns the counts; the biquaternion article owns the frame.**

## Summary

The two-sided operator $L_{A}R_{B}(X)=AXB$ has the matrix $B^{\mathsf T}\otimes A$, is bilinear in the pair, and is constant on the scaling orbits $(\lambda A,\lambda^{-1}B)$. The products fill a closed algebraic cone of complex dimension $2n^{2}-1$ inside the $n^{4}$ dimensions of the endomorphism algebra; the cone is the set of pure tensors of $M_{n}\otimes M_{\mathrm{opp},n}$, and its projectivisation is the Segre variety $\mathbb{P}^{n^{2}-1}\times\mathbb{P}^{n^{2}-1}$.

The rank of a product is the product of the ranks, so the attained ranks are the products $rs$ with $0\le r,s\le n$; the trace is the product of the traces and the determinant is the $n$-th power of the product of the determinants. The products compose by $L_{A}R_{B}L_{C}R_{D}=L_{AC}R_{DB}$, so the family is a monoid with zero whose group of units is $(\mathrm{GL}_{n}\times\mathrm{GL}_{n})/\mathbb{C}^{\times}$, of complex dimension $2n^{2}-1$.

The two one-sided copies are the two rulings of the cone and meet in the scalars; the sandwich $\mathrm{Sd}_{A}=L_{A}R_{A^{*}}$ is a real subcone of real dimension $2n^{2}-1$; the diagonal $\{L_{A}R_{A}\}$ is a complex subcone of complex dimension $n^{2}$. **The cone is not a subspace and not a group, and every property of the two-sided operators follows from the one fact that its members are the pure tensors of a tensor square.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{A}R_{B}$ | the two-sided operator $X\mapsto AXB$ |
| $[L_{A}R_{B}]=B^{\mathsf T}\otimes A$ | its matrix in the column-stacking basis |
| $\mathcal{C}$ | the cone of products |
| $N=n^{2}$ | the dimension of the algebra |
| $2n^{2}-1$ | the complex dimension of the cone |
| $\mathbb{P}^{n^{2}-1}\times\mathbb{P}^{n^{2}-1}$ | the Segre variety of the projectivised cone |
| $\mathrm{Sd}_{A}=L_{A}R_{A^{*}}$ | the sandwich |
| $(\mathrm{GL}_{n}\times\mathrm{GL}_{n})/\mathbb{C}^{\times}$ | the group of units of the monoid |
| $\ell$ | the length, treated in the companion article |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the Kronecker product, its rank and its determinant.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for the Segre varieties and the cones over them.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the two rulings of the cone.
- [The Regular Representation in Dimension $n$](the-regular-representation-in-dimension-n.html), for the tensor form and the ladder.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the coefficient array which cuts the cone out by minors.
- [Operators Acting 2 Side](operators-acting-2-side.html), for the abstract family at $n=2$.
- [$M_4(\mathbb{C})$ Pauli Representation : Operators](m4c-pauli-representation-operators.html), for the sixteen basis operators and the Peirce gauge.
