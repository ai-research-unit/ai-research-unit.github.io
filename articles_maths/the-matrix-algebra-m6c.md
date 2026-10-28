# __The Matrix Algebra $M_6(\mathbb{C})$__

## Introduction

$M_6(\mathbb{C})$ is the algebra of complex $6\times6$ matrices, of complex dimension $36$ and real dimension $72$. It has centre $\mathbb{C}I_6$, it is simple, its commutator subspace is the trace-zero hyperplane $\mathfrak{sl}_6$, and its unit group is $GL_6(\mathbb{C})$, of dimension $36$, with projective quotient $PGL_6(\mathbb{C})$, of dimension $35$.

This article fixes the ambient algebra: the matrix units, the trace and the determinant, the centre, the simplicity, the commutator subalgebra, the real structure of Hermitian and skew-Hermitian parts, and the two-sided module structure. It is the foundation on which the frame of *The Frame, the Simple Nilpotents and the Gauge of $M_6(\mathbb{C})$* and the coordinates of *The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$* are built.

No form and no topology are used here. The positive definite trace form is *The Involution and the Hermitian Structure of $M_6(\mathbb{C})$*; the exponential and the Lie group are *The Exponential and the Lie Group of $M_6(\mathbb{C})$*; the modules are *The Modules and the Minimal Left Ideals of $M_6(\mathbb{C})$*.

## The Algebra

### Definition

**Definition.** $M_6(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb{C}^6)$ is the algebra of complex-linear endomorphisms of $\mathbb{C}^6$, with the product of composition and the unit $I_6$. Its elements are the complex $6\times6$ matrices.

**Proposition.** $\dim_{\mathbb{C}}M_6(\mathbb{C})=36$ and $\dim_{\mathbb{R}}M_6(\mathbb{C})=72$.

**Proof.** A matrix has $36$ independent complex entries; a complex basis of $36$ elements is a real basis of $72$ elements when multiplied by $1$ and $\mathrm i$.

### The Matrix Units

Let $e_1,\dots,e_6$ be the standard basis of $\mathbb{C}^6$ and $e_j^{\vee}$ the dual basis. Put

$$
E_{ij}=e_ie_j^{\vee}.
$$

**Theorem (the matrix-unit rule).** The $E_{ij}$ are a basis of $M_6(\mathbb{C})$, and

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

**Proof.** The rule is $e_ie_j^{\vee}e_ke_l^{\vee}=e_i\delta_{jk}e_l^{\vee}$. The units are linearly independent: applying $\sum a_{ij}E_{ij}$ to $e_k$ gives the column $k$, so the sum is zero only if every $a_{ij}=0$. They span: for $A\in M_6(\mathbb{C})$, $A=\sum_{i,j}A_{ij}E_{ij}$, since both sides send $e_j$ to $\sum_iA_{ij}e_i$.

**Corollary.** The coordinates of $A$ are its entries, and the product is

$$
(AB)_{ij}=\sum_{k=1}^{6}A_{ik}B_{kj}.
$$

**Proof.** Multiply the two sums and apply the rule; the only surviving terms have matching inner indices.

### The Unit Group

**Definition.** $GL_6(\mathbb{C})=\{A\in M_6(\mathbb{C}):\det A\neq0\}$ is the unit group, and $PGL_6(\mathbb{C})=GL_6(\mathbb{C})/\mathbb{C}^\times I_6$ is the projective linear group.

**Proposition.** $GL_6(\mathbb{C})$ is a complex Lie group of dimension $36$, and $PGL_6(\mathbb{C})$ is a complex Lie group of dimension $35$.

**Proof.** $GL_6$ is the open set $\det\neq0$ in the affine space $M_6\cong\mathbb{C}^{36}$, so it has dimension $36$. The centre $\mathbb{C}^\times I_6$ is a closed subgroup of dimension one acting freely, so the quotient has dimension $35$.

**Proposition (the conjugation action).** $GL_6$ acts on $M_6$ by $A\mapsto gAg^{-1}$. The scalars act trivially, so the action factors through $PGL_6$, and the kernel of the action is exactly $\mathbb{C}^\times I_6$.

**Proof.** $(gh)A(gh)^{-1}=g(hAh^{-1})g^{-1}$. A scalar $tI$ gives $tAt^{-1}=A$. If $gAg^{-1}=A$ for all $A$, then $g$ commutes with every matrix, hence $g\in\mathbb{C}I_6$ by §*The Centre*.

### Trace and Determinant

**Definition.** The **trace** is the linear functional

$$
\operatorname{tr}A=\sum_{i=1}^{6}A_{ii},
$$

and the **determinant** is the alternating multilinear function of the columns normalised by $\det I_6=1$.

**Theorem (the elementary properties).**

- $\operatorname{tr}(AB)=\operatorname{tr}(BA)$ for all $A,B$;
- $\operatorname{tr}([A,B])=0$;
- $\det(AB)=\det A\det B$;
- $\det A\neq0$ if and only if $A$ is invertible;
- $\det(tI_6-A)=t^6-\operatorname{tr}(A)t^5+\cdots+(-1)^6\det A$ is the characteristic polynomial.

**Proof.** The trace identity is $\sum_{i,j}A_{ij}B_{ji}=\sum_{i,j}B_{ji}A_{ij}$. The commutator statement follows. The determinant is multiplicative by the column expansion; it is nonzero exactly on a basis, that is on invertible matrices. The characteristic polynomial expands by the Leibniz formula, and the coefficients of $t^5$ and $t^0$ are the trace and the determinant.

**Corollary (Cayley–Hamilton).** $\chi_A(A)=0$.

**Proof.** This is the Cayley–Hamilton theorem for $6\times6$ matrices; it follows from the adjugate identity $(tI-A)\operatorname{adj}(tI-A)=\chi_A(t)I$ evaluated at $t=A$, or from the triangular form over $\mathbb{C}$.

**Corollary (the trace is the only invariant linear functional).** If $\varphi:M_6(\mathbb{C})\to\mathbb{C}$ is linear and $\varphi(AB)=\varphi(BA)$ for all $A,B$, then $\varphi=c\operatorname{tr}$ for some $c\in\mathbb{C}$.

**Proof.** The condition gives $\varphi([A,B])=0$, so $\varphi$ vanishes on $\mathfrak{sl}_6$. Since $M_6=\mathbb{C}I_6\oplus\mathfrak{sl}_6$ (§*The Commutator Subalgebra*), $\varphi$ is determined by its value on $I_6$, and $\operatorname{tr}$ is nonzero there.

## The Centre and the Simplicity

### The Centre

**Theorem.** The centre of $M_6(\mathbb{C})$ is $\mathbb{C}I_6$.

**Proof.** Let $A$ commute with every $E_{ij}$. From $AE_{ij}=E_{ij}A$, compare the $(k,j)$ entries: $A_{ki}=A_{jj}\delta_{ki}$. For fixed $i,j$ this says that the $i$-th column of $A$ vanishes off the diagonal and has diagonal entry $A_{jj}$. Hence $A$ is diagonal, and $A_{ii}=A_{jj}$ for all $i,j$. So $A=\lambda I_6$.

**Corollary.** $\dim_{\mathbb{C}}\mathbb{C}I_6=1$, and the quotient $M_6/\mathbb{C}I_6$ has dimension $35$.

### Simplicity

**Definition.** A **two-sided ideal** of $M_6(\mathbb{C})$ is a linear subspace $J$ with $M_6J\subseteq J$ and $JM_6\subseteq J$.

**Theorem.** $M_6(\mathbb{C})$ is simple: its only two-sided ideals are $0$ and $M_6(\mathbb{C})$.

**Proof.** Let $J\neq0$. Choose $0\neq A\in J$ with $A_{ij}\neq0$. For all $k,l$,

$$
E_{ki}AE_{jl}=A_{ij}E_{kl}\in J,
$$

because $J$ is a two-sided ideal. Since $A_{ij}\neq0$, every matrix unit $E_{kl}$ lies in $J$, and the units span $M_6$. So $J=M_6$.

**Corollary (the left ideals).** The six spaces

$$
L_j=M_6E_{jj}=\left\{\sum_i a_{ij}E_{ij}:a_{ij}\in\mathbb{C}\right\}
$$

are minimal left ideals, each of dimension six, and

$$
M_6(\mathbb{C})=L_1\oplus\cdots\oplus L_6
$$

as left modules. Every simple left $M_6$-module is isomorphic to $L_j\cong\mathbb{C}^6$.

**Proof.** $L_j$ is the $j$-th column. It is a left ideal because $M_6L_j\subseteq L_j$; it is minimal because a nonzero element of $L_j$ has a nonzero entry in row $i$, and then $E_{ij}$ times it is $E_{ij}$, so the ideal generated is all of $L_j$. The sum is direct because the columns are independent. A simple module is a quotient of the regular module $M_6$, and the regular module is the direct sum of the six copies $L_j$; so the simple quotient is one of them.

**Corollary (isotypic of length one).** As a left module, $M_6(\mathbb{C})\cong(\mathbb{C}^6)^{\oplus6}$; as a right module, $M_6(\mathbb{C})\cong((\mathbb{C}^6)^*)^{\oplus6}$; the algebra is isotypic of length one, and all its simple modules have dimension six.

**Proof.** The left statement is the column decomposition. The right statement is the row decomposition, the rows being the dual spaces. The algebra has one isomorphism class of simple modules, so it is isotypic of length one (the length is the number of distinct simple summands, which is one).

**Corollary (the bimodule).** As an $M_6$-bimodule,

$$
M_6(\mathbb{C})\cong\mathbb{C}^6\otimes(\mathbb{C}^6)^*,
\qquad
E_{ij}\leftrightarrow e_i\otimes e_j^{\vee}.
$$

**Proof.** The map $e_i\otimes e_j^{\vee}\mapsto E_{ij}$ is a bimodule isomorphism: $A(e_i\otimes e_j^{\vee})B=AE_{ij}B$.

### The Commutator Subalgebra

**Theorem.** $[M_6(\mathbb{C}),M_6(\mathbb{C})]=\mathfrak{sl}_6(\mathbb{C})=\{A:\operatorname{tr}A=0\}$, and

$$
M_6(\mathbb{C})=\mathbb{C}I_6\oplus\mathfrak{sl}_6(\mathbb{C}),
\qquad
36=1+35 .
$$

**Proof.** Every commutator has trace zero, so $[M_6,M_6]\subseteq\mathfrak{sl}_6$. Conversely, for $i\neq j$,

$$
E_{ij}=[E_{ii},E_{ij}],
\qquad
E_{ii}-E_{jj}=[E_{ij},E_{ji}].
$$

The units $E_{ij}$ with $i\neq j$ and the differences $E_{ii}-E_{jj}$ (for $j=2,\dots,6$) are a basis of the trace-zero hyperplane, of dimension $35$. So the commutator subspace is $\mathfrak{sl}_6$. The decomposition is the decomposition of a matrix into its scalar part $\tfrac16(\operatorname{tr}A)I_6$ and its traceless part.

**Corollary (perfectness).** $\mathfrak{sl}_6(\mathbb{C})=[\mathfrak{sl}_6(\mathbb{C}),\mathfrak{sl}_6(\mathbb{C})]$.

**Proof.** The displayed identities express every basis element of $\mathfrak{sl}_6$ as a commutator of two traceless matrices: $E_{ij}=[E_{ii}-\tfrac16I_6,E_{ij}]$ and $E_{ii}-E_{jj}=[E_{ij},E_{ji}]$, and both arguments are traceless.

**Remark (single commutators).** Every traceless matrix is not only a sum of commutators but a single commutator: for $n\ge2$ and every $A$ with $\operatorname{tr}A=0$ there are $B,C$ with $A=[B,C]$. This is Shoda's theorem over an algebraically closed field of characteristic zero; it is stronger than perfectness and is not needed below. **The identity is not a commutator**, because its trace is $6\neq0$.

## The Real Structure

### Complex and Real Dimensions

**Proposition.** $M_6(\mathbb{C})$ has complex dimension $36$ and real dimension $72$. The real basis is $E_{ij}$ and $\mathrm iE_{ij}$, $1\le i,j\le6$.

**Proof.** The $36$ complex units are a complex basis; multiplying by $1$ and $\mathrm i$ gives $72$ real basis vectors.

### Hermitian and Skew-Hermitian Parts

**Definition.** The **conjugate transpose** of $A$ is $A^*=\bar A^{\mathsf T}$, with entries $(A^*)_{ij}=\overline{A_{ji}}$. An element is **Hermitian** if $A^*=A$, **skew-Hermitian** if $A^*=-A$, and **$*$-unitary** if $A^*A=I_6$.

**Proposition.** Every $A\in M_6(\mathbb{C})$ splits uniquely as

$$
A=\frac{A+A^*}{2}+\frac{A-A^*}{2},
$$

a Hermitian part plus a skew-Hermitian part. The real vector spaces

$$
\mathfrak{u}(6)=\{A:A^*=-A\},\qquad
\mathfrak{su}(6)=\{A\in\mathfrak{u}(6):\operatorname{tr}A=0\}
$$

have real dimensions $36$ and $35$.

**Proof.** The two parts are Hermitian and skew-Hermitian, and the sum is $A$; uniqueness follows by applying the conjugate transpose. A skew-Hermitian matrix has purely imaginary diagonal entries ($6$ real parameters) and arbitrary complex entries above the diagonal ($15$ complex $=30$ real parameters), so $\dim_{\mathbb{R}}\mathfrak{u}(6)=36$. The trace is a nonzero real-linear functional on $\mathfrak{u}(6)$ (with values in $\mathrm i\mathbb{R}$), so its kernel has real dimension $35$.

**Theorem (the complexification).** As real vector spaces,

$$
M_6(\mathbb{C})=\mathfrak{u}(6)\oplus\mathrm i\,\mathfrak{u}(6)
\cong\mathfrak{u}(6)\otimes_{\mathbb{R}}\mathbb{C}.
$$

**Proof.** If $A\in\mathfrak{u}(6)\cap\mathrm i\mathfrak{u}(6)$, then $A^*=-A$ and $A=\mathrm iB$ with $B^*=-B$, so $A^*=(\mathrm iB)^*=-\mathrm iB^*=\mathrm iB=A$, hence $A=0$. The dimensions add: $36+36=72$. The complex scalar multiplication on the right is the complexification.

**Corollary (the $*$-unitary group).** $U(6)=\{A:A^*A=I_6\}$ is a compact real Lie group of dimension $36$, and $PU(6)=U(6)/U(1)$ has dimension $35$.

**Proof.** $U(6)$ is closed and bounded in $M_6(\mathbb{C})\cong\mathbb{R}^{72}$, hence compact; its Lie algebra is $\mathfrak{u}(6)$, of dimension $36$. The centre $U(1)$ acts freely, so the quotient has dimension $35$.

**Remark (the two real forms).** $GL_6(\mathbb{C})$ has complex dimension $36$; its compact real form $U(6)$ has real dimension $36$; $PGL_6(\mathbb{C})$ and $PU(6)$ both have dimension $35$. The equality of the two $35$'s is the equality of the complex and compact real dimensions of the same projective group.

## The Algebra as an Algebra of Operators

### The Left and Right Representations

**Definition.** For $A\in M_6(\mathbb{C})$ let

$$
L_A(B)=AB,\qquad R_A(B)=BA
$$

be the left and right multiplications on $M_6$.

**Proposition.** $L$ and $R$ are faithful algebra homomorphisms, $L_A R_B=R_B L_A$ for all $A,B$, and the map

$$
M_6\otimes M_6^{\mathrm{op}}\longrightarrow\operatorname{End}(M_6),
\qquad
A\otimes B\longmapsto L_A R_B
$$

is an isomorphism of algebras.

**Proof.** $L_{AB}=L_AL_B$ and $R_{AB}=R_BR_A$ (the order reverses for the right representation, which is the opposite algebra). Faithfulness: $L_A=0$ implies $A=L_A(I)=0$. The commutation is associativity. The map is injective because $L_A R_B(I)=AB$, and both sides have dimension $36\cdot36=1296$.

### Derivations and Automorphisms

**Definition.** A **derivation** of $M_6$ is a linear map $D$ with $D(AB)=D(A)B+AD(B)$. An **inner derivation** is $\operatorname{ad}_A(B)=[A,B]$.

**Theorem.** Every derivation of $M_6(\mathbb{C})$ is inner, and

$$
\operatorname{Der}(M_6)\cong\mathfrak{sl}_6(\mathbb{C}),
\qquad
\dim\operatorname{Der}(M_6)=35 .
$$

**Proof.** The algebra $M_6$ is central simple (§*The Centre* and §*Simplicity*), so the Skolem–Noether theorem applies: every derivation is inner. The map $A\mapsto\operatorname{ad}_A$ has kernel the centre $\mathbb{C}I_6$ and image the inner derivations, so the derivations are $\mathfrak{sl}_6$; the dimension is $36-1=35$.

**Theorem (the automorphisms).** Every automorphism of $M_6(\mathbb{C})$ is inner, and

$$
\operatorname{Aut}(M_6)\cong PGL_6(\mathbb{C}),
\qquad
\dim\operatorname{Aut}(M_6)=35 .
$$

**Proof.** Skolem–Noether: every automorphism is $A\mapsto gAg^{-1}$ for some $g\in GL_6$, and $g$ is unique up to a scalar. The inner automorphism group is $GL_6/\mathbb{C}^\times I_6=PGL_6$, of dimension $35$.

### The Trace Pairing

**Definition.** The **trace pairing** is

$$
\langle A,B\rangle=\operatorname{tr}(AB).
$$

**Theorem.** The trace pairing is a nondegenerate symmetric bilinear form on $M_6(\mathbb{C})$, invariant under the left and right multiplications:

$$
\langle AB,C\rangle=\langle A,BC\rangle .
$$

**Proof.** Bilinearity and symmetry are immediate from the trace. Nondegeneracy: if $\langle A,B\rangle=0$ for all $B$, take $B=E_{ij}$; then $\operatorname{tr}(AE_{ij})=A_{ji}=0$ for all $i,j$, so $A=0$. Invariance: $\operatorname{tr}(ABC)=\operatorname{tr}(A\,BC)$ by associativity.

**Corollary (the Killing form).** On $\mathfrak{sl}_6(\mathbb{C})$ the Killing form is $12\operatorname{tr}(AB)$; on $M_6(\mathbb{C})$ it is $12\operatorname{tr}(AB)-2\operatorname{tr}(A)\operatorname{tr}(B)$.

**Proof.** For $\mathfrak{gl}_n$ the Killing form is $2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$; at $n=6$ this is $12\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$. On the traceless part the second term vanishes.

**Remark.** The trace pairing is not the Hermitian form of *The Involution and the Hermitian Structure of $M_6(\mathbb{C})$*: it is complex bilinear, not conjugate-linear, and it is indefinite as a real bilinear form. The positive definite form is $\operatorname{tr}(A^*B)$, which uses the involution. On Hermitian matrices the two pairings agree and are real.

## Worked Examples

### The Nilpotent Jordan Block

**Example.** Let

$$
N=\sum_{i=1}^{5}E_{i,i+1}=
\begin{pmatrix}
0&1&0&0&0&0\\
0&0&1&0&0&0\\
0&0&0&1&0&0\\
0&0&0&0&1&0\\
0&0&0&0&0&1\\
0&0&0&0&0&0
\end{pmatrix}.
$$

Then

$$
N^r=\sum_{i=1}^{6-r}E_{i,i+r}\quad(1\le r\le5),
\qquad
N^6=0,
$$

$\operatorname{rank}N=5$, $\operatorname{tr}N=0$, $\det N=0$, and the characteristic polynomial is $t^6$.

**Proof.** The product rule telescopes: $E_{i,i+1}E_{i+1,i+2}=E_{i,i+2}$, and so on. The $r$-th power has ones on the $r$-th superdiagonal. The rank is five because the image is spanned by $e_1,\dots,e_5$ and the kernel is $\mathbb{C}e_6$. The trace is the sum of the diagonal entries, all zero; the determinant is zero because $N$ is not invertible; the characteristic polynomial is $t^6$ because $N$ is nilpotent of index six.

### The Cyclic Shift

**Example.** Let $\rho$ be the permutation matrix of the cycle $1\mapsto2\mapsto\cdots\mapsto6\mapsto1$. Then $\rho^6=I_6$, $\operatorname{tr}\rho=0$, $\det\rho=-1$, and

$$
\chi_\rho(t)=t^6-1 .
$$

**Proof.** $\rho$ is a permutation matrix with no fixed point, so its trace is zero and its determinant is the sign of the $6$-cycle, which is $(-1)^5=-1$. Its eigenvalues are the six sixth roots of unity, each once, so the characteristic polynomial is $\prod_k(t-\zeta_k)=t^6-1$.

**Remark.** The cyclic shift is a root in the sense of *Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$*: $\rho^6=I_6$ with simple spectrum. The nilpotent $N$ is the other extreme: $N^6=0$ with a single eigenvalue. The two examples are the two ends of the Jordan classification, and both have trace zero.

### A Projector

**Example.** $P=E_{11}$ satisfies $P^2=P$, $\operatorname{rank}P=1$, $\operatorname{tr}P=1$, $\det P=0$, and $\chi_P(t)=t^5(t-1)$.

**Proof.** $E_{11}^2=E_{11}$; the image is $\mathbb{C}e_1$ and the kernel is spanned by $e_2,\dots,e_6$. The trace is the single nonzero diagonal entry, and the determinant is zero because the rank is one. The characteristic polynomial has the eigenvalue $1$ once and $0$ five times.

## Summary

$M_6(\mathbb{C})$ is the algebra of complex $6\times6$ matrices, of complex dimension $36$ and real dimension $72$, with basis $E_{ij}$ and product $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

Its centre is $\mathbb{C}I_6$, it is simple, and it is isotypic of length one: as a left module it is six copies of $\mathbb{C}^6$, and every simple module is $\mathbb{C}^6$. Its commutator subspace is the trace-zero hyperplane,

$$
[M_6,M_6]=\mathfrak{sl}_6(\mathbb{C}),
\qquad
M_6=\mathbb{C}I_6\oplus\mathfrak{sl}_6,
\qquad
36=1+35 .
$$

$$
\boxed{\ M_6(\mathbb{C})\text{ is central simple, } \operatorname{Der}(M_6)\cong\mathfrak{sl}_6,\ \operatorname{Aut}(M_6)\cong PGL_6,\ \dim=35 .\ }
$$

The real structure is $M_6=\mathfrak{u}(6)\oplus\mathrm i\mathfrak{u}(6)$, with $\dim_{\mathbb{R}}\mathfrak{u}(6)=36$ and $\dim_{\mathbb{R}}\mathfrak{su}(6)=35$. The trace pairing $\langle A,B\rangle=\operatorname{tr}(AB)$ is nondegenerate, symmetric and invariant; the Killing form on $\mathfrak{sl}_6$ is $12\operatorname{tr}(AB)$.

| Object | Dimension | Data |
|---|---|---|
| $M_6(\mathbb{C})$ | $36$ complex, $72$ real | $E_{ij}$, product rule |
| Centre | $1$ | $\mathbb{C}I_6$ |
| $\mathfrak{sl}_6(\mathbb{C})$ | $35$ | trace-zero matrices |
| $GL_6(\mathbb{C})$ | $36$ | invertible matrices |
| $PGL_6(\mathbb{C})$ | $35$ | $GL_6/\mathbb{C}^\times$ |
| $U(6)$ | $36$ real | $A^*A=I_6$ |
| $PU(6)$ | $35$ real | $U(6)/U(1)$ |
| $\operatorname{Der}(M_6)$ | $35$ | inner derivations |
| $\operatorname{Aut}(M_6)$ | $35$ | $PGL_6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E_{ij}$ | the matrix unit $e_ie_j^{\vee}$, with $E_{ij}E_{kl}=\delta_{jk}E_{il}$ |
| $\operatorname{tr}$ | the trace, $\sum_iA_{ii}$ |
| $\det$ | the determinant |
| $\chi_A(t)$ | the characteristic polynomial $\det(tI_6-A)$ |
| $\mathfrak{sl}_6$ | the trace-zero matrices, $[M_6,M_6]$ |
| $A^*$ | the conjugate transpose |
| $\mathfrak{u}(6),\mathfrak{su}(6)$ | skew-Hermitian and trace-zero skew-Hermitian matrices |
| $\langle A,B\rangle=\operatorname{tr}(AB)$ | the trace pairing |
| $\operatorname{ad}_A(B)=[A,B]$ | the inner derivation |

## Further Reading

- [The Frame, the Simple Nilpotents and the Gauge of $M_6(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-m6c.html), for the frame, the matrix units and the gauge.
- [The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m6c.html), for the coordinates and the scalar-traceless split.
- [The Involution and the Hermitian Structure of $M_6(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m6c.html), for the positive definite trace form and the real forms.
- [The Modules and the Minimal Left Ideals of $M_6(\mathbb{C})$](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the column ideals and the simple modules.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_6(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m6c.html), for $PGL_6$ and its action.
- [Central Simple Algebras and the Brauer Group](central-simple-algebras-and-the-brauer-group.html), for the simplicity, Skolem–Noether and the inner derivations.
- Israel Nathan Herstein, *Noncommutative Rings* (Carus Mathematical Monographs, 1968), for the centre, the ideals and the matrix units.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the trace, the derivations and the automorphisms.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for $\mathfrak{sl}_6$ and the Killing form.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the general algebra at order $n$.
