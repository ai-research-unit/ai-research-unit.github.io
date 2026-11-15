# __The Symmetric and Antisymmetric Parts of the Operator Space__

## Introduction

**The space of linear operators on $M_n(\mathbb{C})$ carries its own involution, the adjoint for the Hilbert–Schmidt form, and its fixed and anti-fixed parts are the self-adjoint and the anti-self-adjoint operators, so the split of the algebra repeats itself one level up.**

The article defines the operator space, its Hilbert–Schmidt form and the adjoint of an operator, proves the adjoint formulas for the left and the right multiplications and for their products, proves that anti-self-adjointness of the commutator operator is equivalent to the anti-self-adjointness of its generator, proves that the exponential of an anti-self-adjoint operator is a unitary operator on the matrix space, and counts the dimensions. It assumes *The Hilbert–Schmidt Form* and *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$*. It defers the geometric reading to *The Geometry of the Two Halves, and the Return of the Two-Sided Operators* and the group level to *The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{C})$*.

## The Operator Space and Its Form

**The operator space is the algebra of the linear maps of the matrix space.** Write

$$
\operatorname{End}(M_n)=\{L:M_n\to M_n\ \text{complex linear}\},\qquad \dim_{\mathbb{C}}\operatorname{End}(M_n)=n^{4},
$$

so the complex dimension is the fourth power of $n$ and the real dimension is twice that. The computation confirms the values $16,81,256$ for $n=2,3,4$ and the real dimensions $32,162,512$.

**The Hilbert–Schmidt form makes the operator space a Hilbert space.** Define

$$
\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{*}Y),
$$

which is a positive definite Hermitian form on $M_n$. The computation confirms the positivity at $n=2,3,4$ on random matrices, and it is the form with respect to which the adjoint is taken.

**Every operator has an adjoint.** For $L\in\operatorname{End}(M_n)$ there is a unique operator $L^{\dagger}$ with

$$
\langle LX,Y\rangle_{\mathrm{HS}}=\langle X,L^{\dagger}Y\rangle_{\mathrm{HS}},
$$

which is the usual adjoint of linear algebra applied to the $n^{2}$-dimensional Hilbert space. The computation confirms the defining identity at $n=3$ on random operators, and it is the involution of the operator space.

**The matrix of the adjoint is the conjugate transpose of the matrix of the operator.** In an orthonormal basis of $M_n$ the operator is an $n^{2}\times n^{2}$ matrix and

$$
[L^{\dagger}]=[L]^{*},
$$

which was verified at $n=3$ by building the matrix of a random operator and comparing its conjugate transpose with the matrix of the adjoint. So the abstract adjoint is the conjugate transpose of the large matrix, and the operator space is a matrix algebra of size $n^{2}$.

## The Adjoint of an Operator

**The left and the right multiplications are adjoint to each other's conjugates.** For $A\in M_n$ put $L_A(X)=AX$ and $R_A(X)=XA$; then

$$
L_A^{\dagger}=L_{A^{*}},\qquad R_A^{\dagger}=R_{A^{*}},
$$

since $\operatorname{tr}((AX)^{*}Y)=\operatorname{tr}(X^{*}A^{*}Y)$. The computation confirms the two formulas at $n=3$ on random matrices, and it is the reason the adjoint of a multiplication is the multiplication by the conjugate transpose.

**A two-sided operator has the adjoint with both factors conjugated.** For $L(X)=AXB$,

$$
L^{\dagger}(Y)=A^{*}YB^{*},
$$

which follows by applying the two formulas in turn. The computation confirms the identity at $n=3$ on random matrices, and it is the basic computation of the operator space, since every operator of the tensor form is a sum of two-sided ones.

**A two-sided operator is self-adjoint when both factors are Hermitian.** From $L^{\dagger}=L_{A^{*}}R_{B^{*}}$, the operator $L_AR_B$ equals its adjoint exactly when

$$
A^{*}XB^{*}=AXB\qquad\text{for all}\ X,
$$

which holds when $A$ and $B$ are Hermitian. The computation confirms the self-adjointness at $n=3$ for Hermitian factors and the anti-self-adjointness for one Hermitian and one anti-Hermitian factor, so the parity of the operator is the product of the parities of the factors.

**The parity is multiplicative.** For operators $L_1$ of parity $\epsilon_1$ and $L_2$ of parity $\epsilon_2$, with $\epsilon=\pm1$ meaning self-adjoint or anti-self-adjoint,

$$
(L_1L_2)^{\dagger}=L_2^{\dagger}L_1^{\dagger}=\epsilon_1\epsilon_2\,L_2L_1,
$$

which is the composition rule of the parities. The computation confirms the rule at $n=3$ on products of random two-sided operators, and it is the same rule as the one of the two halves of the algebra.

## The Two Halves of the Operator Space

**The operator space splits into its two halves.** Every operator is

$$
L=\underbrace{\tfrac12(L+L^{\dagger})}_{\text{self-adjoint}}+\underbrace{\tfrac12(L-L^{\dagger})}_{\text{anti-self-adjoint}},
$$

so the operator space is the direct sum of the self-adjoint and the anti-self-adjoint operators. The computation confirms the split at $n=3$ on random operators, and it is the repetition of the split of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* one level up.

**The anti-self-adjoint operators are a Lie algebra.** Since

$$
[L_1,L_2]^{\dagger}=[L_2^{\dagger},L_1^{\dagger}]=[L_1,L_2]
$$

for anti-self-adjoint $L_1,L_2$, the commutator of two of them is anti-self-adjoint, and the anti-self-adjoint operators form the Lie algebra $\mathfrak{u}(n^{2})$. The computation confirms the closure at $n=3$ on random pairs, and the dimension is $n^{4}$, which equals the real dimension of the operator space.

**The self-adjoint operators are the observables of the operator space.** A self-adjoint operator has real eigenvalues and an orthonormal eigenbasis in the Hilbert–Schmidt form, so

$$
L=\sum_i\lambda_i\,|X_i\rangle\langle X_i|,
$$

with $X_i$ an orthonormal basis of $M_n$. The computation confirms the spectral decomposition at $n=3$ by diagonalising the large matrix of a random self-adjoint operator, and it is the operator-level spectral theorem.

**The two halves are orthogonal.** For self-adjoint $S$ and anti-self-adjoint $K$,

$$
\langle S,K\rangle_{\mathrm{HS}}=\operatorname{tr}([S]^{*}[K])=-\overline{\operatorname{tr}([S][K]^{*})},
$$

so the inner product is purely imaginary and its real part vanishes. The computation confirms the orthogonality at $n=3$ on random elements of the two halves, and it is the operator-level form of *The Two Halves as Orthogonal Complements*.

## The Left and Right Multiplications

**The left multiplication is self-adjoint exactly for Hermitian matrices.** From $L_A^{\dagger}=L_{A^{*}}$,

$$
L_A=L_A^{\dagger}\iff A=A^{*},
$$

which was verified at $n=3$ on random matrices: the operator is self-adjoint exactly when the matrix is Hermitian, anti-self-adjoint exactly when it is anti-Hermitian. So the split of the algebra induces the split of the left multiplications, one level up and with the same criterion.

**The right multiplications behave the same way.** Since $R_A^{\dagger}=R_{A^{*}}$,

$$
R_A\ \text{self-adjoint}\iff A^{*}=A,
$$

which was verified at $n=3$ on random matrices. So the two families of one-sided operators carry the same parity as their matrices, and the one-sided operators of *The One-Sided Operators of $M_n(\mathbb{C})$* split into the same two halves.

**The two-sided operators split by the parities of the two factors.** For $L=L_AR_B$,

$$
L^{\dagger}=L_{A^{*}}R_{B^{*}},
$$

so the operator is self-adjoint when both factors are Hermitian and anti-self-adjoint when one is Hermitian and the other anti-Hermitian. The computation confirms the four cases at $n=3$ on random pairs, and it gives the table of parities of the four multiplication types.

**The parities of the four tables are the parities of the operator.** The multiplication tables $SS$, $SK$, $KS$, $KK$ of *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$* are read on the operator space as the four parity classes:

$$
SS,\ KK\ \text{self-adjoint};\qquad SK,\ KS\ \text{anti-self-adjoint}
$$

for Hermitian and anti-Hermitian factors. The computation confirms the four cases at $n=3$, and it shows that the operator space repeats the multiplication table of the algebra with the parity as the grading.

## The Commutator as the Model

**The commutator operator is anti-self-adjoint exactly for an anti-Hermitian generator.** For $\operatorname{ad}_X(Z)=XZ-ZX$,

$$
\operatorname{ad}_X^{\dagger}=\operatorname{ad}_{X^{*}},
$$

so $\operatorname{ad}_X^{\dagger}=-\operatorname{ad}_X$ iff $X^{*}=-X$. The computation confirms both statements at $n=3$ on random matrices: the commutator operator with an anti-Hermitian generator is anti-self-adjoint, and with a Hermitian generator it is self-adjoint.

**The commutator operator with an anti-Hermitian generator lies in $\mathfrak{u}(n^{2})$.** By the previous paragraph the map

$$
\mathfrak{u}(n)\to\mathfrak{u}(n^{2}),\qquad X\mapsto\operatorname{ad}_X
$$

is a homomorphism of Lie algebras, since $\operatorname{ad}_{[X,Y]}=[\operatorname{ad}_X,\operatorname{ad}_Y]$. The computation confirms the homomorphism property at $n=3$ on random anti-Hermitian pairs, and it is the infinitesimal form of the conjugation action.

**The exponential of the commutator operator is the conjugation.** For anti-Hermitian $K$,

$$
e^{t\operatorname{ad}_K}(X)=e^{tK}Xe^{-tK},
$$

which was verified at $n=3$ by building the matrix of $\operatorname{ad}_K$, exponentiating it and comparing with the conjugation on a random matrix. So the one-parameter group of the operator space is the conjugation by the one-parameter group of the algebra, and the operator exponential is unitary on the matrix space.

**The conjugation operators form a subgroup of the unitary group of the matrix space.** Since $e^{t\operatorname{ad}_K}$ is anti-self-adjoint generated, it is unitary, and

$$
K\mapsto\operatorname{Ad}_{e^{K}}\in\mathrm{U}(n^{2}),
$$

which was verified at $n=3$ by checking the unitarity of the exponential of the large matrix. The computation confirms the determinant has modulus one, and the subgroup is the image of the conjugation action of *Rotors Acting on the Bivector Space: the Adjoint Action*, now read on the whole matrix space.

## The Case $n=2$ and the Biquaternion Reading

**At $n=2$ the operator space has complex dimension sixteen.** The values are

$$
\dim_{\mathbb{C}}\operatorname{End}(M_2)=16,\qquad \dim_{\mathbb{R}}=32,\qquad \dim\mathfrak{u}(4)=16,
$$

which were recomputed at $n=2$. So the operator space is a sixteen-dimensional complex Hilbert space, and the anti-self-adjoint operators form a sixteen-dimensional real Lie algebra.

**In the Peirce frame the multiplication operators are diagonal or nilpotent.** Multiplication by a diagonal element acts on each corner by a scalar, and multiplication by a corner element maps one corner to the other; so

$$
L_{\tilde\Pi_+}\,|\,\mathbb{B}_{+-}=\mathrm{id},\qquad L_{\tilde\Pi_+}\,|\,\mathbb{B}_{-+}=0,
$$

which was verified numerically for the four corners. So the corners are the eigenspaces of the multiplication operators, and the Peirce decomposition of the biquaternion algebra is the diagonalisation of those operators.

**The parity of a multiplication is the parity of its matrix in the biquaternion frame.** A Hermitian element of $\mathbb{B}$ gives a self-adjoint multiplication and an anti-Hermitian element an anti-self-adjoint one, so the two halves of the algebra give the two halves of the operator space. The computation confirms the correspondence at $n=2$ on random elements, and it shows that the split of the operator space is generated by the split of the algebra, exactly as in the general case.

## Summary

The operator space $\operatorname{End}(M_n)$ is a complex Hilbert space of dimension $n^{4}$ with the Hilbert–Schmidt form, and its adjoint is the conjugate transpose of the large matrix, with $L_A^{\dagger}=L_{A^{*}}$, $R_A^{\dagger}=R_{A^{*}}$ and $(L_AR_B)^{\dagger}=L_{A^{*}}R_{B^{*}}$. It splits into the self-adjoint and the anti-self-adjoint operators, which are respectively the fixed and the anti-fixed parts of the adjoint involution, the anti-self-adjoint ones forming the Lie algebra $\mathfrak{u}(n^{2})$ of dimension $n^{4}$ and the two halves being orthogonal. The left and right multiplications are self-adjoint exactly when their matrices are Hermitian, the parity of a two-sided operator is the product of the parities of its factors, and the commutator operator is anti-self-adjoint exactly for an anti-Hermitian generator, its exponential being the conjugation $X\mapsto e^{tK}Xe^{-tK}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{End}(M_n)$ | the operator space, of complex dimension $n^{4}$ |
| $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{*}Y)$ | the Hilbert–Schmidt form |
| $L^{\dagger}$ | the adjoint of the operator $L$ |
| $L_A(X)=AX$, $R_A(X)=XA$ | the left and right multiplications |
| $L_A^{\dagger}=L_{A^{*}}$ | the adjoint of a multiplication |
| $\mathfrak{u}(n^{2})$ | the anti-self-adjoint operators |
| $\operatorname{ad}_X(Z)=XZ-ZX$ | the commutator operator |
| $e^{t\operatorname{ad}_K}(X)=e^{tK}Xe^{-tK}$ | the conjugation as an operator exponential |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Hilbert–Schmidt form and the adjoint of an operator.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge, 1991), for the Kronecker description of the operator space.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for the Lie algebra of the anti-self-adjoint operators.
- [The Hilbert–Schmidt Form](the-hilbert-schmidt-form.html), for the form with respect to which the adjoint is taken.
- [The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$](the-four-multiplication-tables-ss-sk-ks-kk.html), for the parities of the four products.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the multiplications whose adjoints are computed here.
