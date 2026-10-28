# __The Sextic and the Spectral Strata of $M_6(\mathbb{C})$__

## Introduction

Every $A\in M_6(\mathbb{C})$ has a characteristic polynomial of degree six,

$$
\chi_A(t)=\det(tI_6-A)=t^6-s_1t^5+s_2t^4-s_3t^3+s_4t^2-s_5t+s_6 .
$$

The six roots, counted with multiplicity, are the eigenvalues. Their multiplicity pattern is a partition of $6$, and the partitions stratify the algebra. The stratum of simple spectrum is open and dense, of dimension $36$; the discriminant is the codimension-one stratum of a repeated root; the smallest stratum is the single-eigenvalue locus, of dimension $31$.

On the simple stratum the six spectral projectors are the Lagrange projectors of the sextic. They are polynomials in $A$, idempotent, of rank one, and they sum to the identity. At a repeated root they degenerate: the individual projectors have poles along the discriminant, the cluster projector onto a generalized eigenspace extends, and the nilpotent part is the residue.

The article assumes the root and its Lagrange projectors of *Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$* and the algebra of *The Matrix Algebra $M_6(\mathbb{C})$*. It uses no form and no topology. The spectral theorem for the Hermitian case is *Spectral Theory and the Spectral Projectors of $M_6(\mathbb{C})$*; the exponential is *The Exponential and the Lie Group of $M_6(\mathbb{C})$*.

## The Characteristic Sextic

### The Polynomial

**Definition.** The **characteristic polynomial** of $A$ is

$$
\chi_A(t)=\det(tI_6-A).
$$

**Proposition.** $\chi_A$ is monic of degree six, and

$$
\chi_A(t)=t^6-\operatorname{tr}(A)t^5+\cdots+(-1)^6\det A .
$$

**Proof.** The determinant is multilinear in the six columns of $tI_6-A$; the term of degree six is $t^6$, the term of degree five is $-t^5\operatorname{tr}A$ (one diagonal entry $-A_{ii}$ and five factors $t$), and the constant term is $\det(-A)=(-1)^6\det A$.

### The Coefficients

**Definition.** The **elementary symmetric functions** of $A$ are the coefficients

$$
\chi_A(t)=t^6-s_1t^5+s_2t^4-s_3t^3+s_4t^2-s_5t+s_6 .
$$

**Theorem (Newton's identities).** Let $p_k=\operatorname{tr}(A^k)$. Then

$$
s_1=p_1,\qquad
s_2=\frac{p_1^2-p_2}{2},\qquad
s_3=\frac{p_1^3-3p_1p_2+2p_3}{6},
$$

and in general $ks_k=\sum_{i=1}^{k}(-1)^{i-1}s_{k-i}p_i$, with $s_0=1$.

**Proof.** The eigenvalues $\lambda_1,\dots,\lambda_6$ satisfy $p_k=\sum_i\lambda_i^k$, and the elementary symmetric functions $s_k$ of the eigenvalues are the coefficients of $\prod_i(t-\lambda_i)$. Newton's identities are the standard relations between the power sums and the elementary symmetric functions; they follow by differentiating $\log\prod_i(1-\lambda_it)$.

**Corollary.** $s_6=\det A$, and $s_5=\operatorname{tr}(\operatorname{adj}A)$, the sum of the six principal $5\times5$ minors.

**Proof.** The constant term is $\prod_i\lambda_i=\det A$. The coefficient of $t$ is $(-1)^5$ times the sum of the principal $5\times5$ minors, which is $\operatorname{tr}(\operatorname{adj}A)$.

**Theorem (Cayley–Hamilton).** $\chi_A(A)=0$.

**Proof.** The adjugate identity $(tI-A)\operatorname{adj}(tI-A)=\chi_A(t)I$ is an identity of polynomials with matrix coefficients; evaluating at $t=A$ gives $0=\chi_A(A)$.

### The Spectrum

**Theorem.** Over $\mathbb{C}$,

$$
\chi_A(t)=\prod_{i=1}^{6}(t-\lambda_i),
$$

where $\lambda_1,\dots,\lambda_6$ are the eigenvalues counted with algebraic multiplicity. Moreover

$$
\operatorname{tr}A=\sum_i\lambda_i,\qquad
\det A=\prod_i\lambda_i .
$$

**Proof.** The fundamental theorem of algebra splits the sextic; the trace and determinant are the coefficients $s_1$ and $s_6$.

**Definition.** The **spectrum** of $A$ is the multiset $\{\lambda_1,\dots,\lambda_6\}$. Its **multiplicity pattern** is the partition $\lambda$ of $6$ whose parts are the multiplicities of the distinct eigenvalues, written in decreasing order.

### The Discriminant

**Definition.** The **discriminant** of $A$ is

$$
\Delta(A)=\prod_{1\le i<j\le6}(\lambda_i-\lambda_j)^2 .
$$

**Theorem.** $\Delta$ is a polynomial in the entries of $A$ (equivalently, in the coefficients $s_1,\dots,s_6$), and

$$
\Delta(A)=0
\quad\Longleftrightarrow\quad
\chi_A\text{ has a repeated root}.
$$

**Proof.** The discriminant of a monic polynomial is a polynomial in its coefficients; expressing the coefficients as functions of the entries gives a polynomial in the entries. It vanishes exactly when two roots coincide.

**Corollary (the simple stratum).** The set

$$
U=\{\Delta(A)\neq0\}
$$

is open and dense in $M_6(\mathbb{C})$, of dimension $36$.

**Proof.** $\Delta$ is not identically zero: the diagonal matrix $\operatorname{diag}(1,2,3,4,5,6)$ has $\Delta=\prod_{i<j}(i-j)^2\neq0$. The complement of a nonzero polynomial is open and dense, and a nonempty open subset of $\mathbb{C}^{36}$ has dimension $36$.

**Remark.** The root set of *Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$* is not $U$: it is the subset of $U$ on which the spectrum is exactly the six sixth roots. It has dimension $30$, not $36$; the difference of six is the freedom of the six eigenvalues, which the root fixes.

## The Strata

### The Partitions of Six

The multiplicity patterns are the eleven partitions of $6$:

$$
\begin{array}{llll}
(1,1,1,1,1,1), & (2,1,1,1,1), & (2,2,1,1), & (2,2,2),\\
(3,1,1,1), & (3,2,1), & (3,3), & (4,1,1),\\
(4,2), & (5,1), & (6). &
\end{array}
$$

**Definition.** For a partition $\lambda=(m_1,\dots,m_r)$ of $6$ with $m_1\ge\cdots\ge m_r\ge1$, the **stratum** $S_\lambda$ is the set of matrices whose distinct eigenvalues have multiplicities $m_1,\dots,m_r$.

**Example.** $S_{(1,1,1,1,1,1)}=U$ is the simple stratum. $S_{(2,1,1,1,1)}$ is the discriminant locus minus the strata with a higher multiplicity. $S_{(6)}$ is the set of matrices with a single eigenvalue.

### The Dimension of a Stratum

**Theorem.** For a partition $\lambda$ of $6$ with $r$ parts,

$$
\dim S_\lambda=30+r=36-(6-r).
$$

**Proof.** The characteristic map $\chi:M_6\to\mathbb{C}^6$, $A\mapsto(s_1,\dots,s_6)$, has image of dimension $r$ on $S_\lambda$: the coefficients are the elementary symmetric functions of the $r$ distinct eigenvalues, which are $r$ free parameters. The fibre over a fixed polynomial with the root multiplicities $\lambda$ is the set of matrices with that characteristic polynomial. The fibre contains the conjugacy class of a matrix with one Jordan block for each distinct eigenvalue (the regular element); that orbit has dimension $36-6=30$, because the centralizer of a cyclic element is the six-dimensional algebra of polynomials in the element. The regular orbit is open in the fibre, so the fibre has dimension $30$, and the family of fibres is locally trivial over the space of polynomials with the fixed multiplicity pattern. The total dimension is $30+r$.

**Corollary (the table).**

| Partition | $r$ | $\dim S_\lambda$ | Codimension | Representative |
|---|---|---|---|---|
| $(1,1,1,1,1,1)$ | $6$ | $36$ | $0$ | $\operatorname{diag}(1,2,3,4,5,6)$ |
| $(2,1,1,1,1)$ | $5$ | $35$ | $1$ | $\operatorname{diag}(1,1,2,3,4,5)$ |
| $(2,2,1,1)$ | $4$ | $34$ | $2$ | $\operatorname{diag}(1,1,2,2,3,4)$ |
| $(2,2,2)$ | $3$ | $33$ | $3$ | $\operatorname{diag}(1,1,2,2,3,3)$ |
| $(3,1,1,1)$ | $4$ | $34$ | $2$ | $\operatorname{diag}(1,1,1,2,3,4)$ |
| $(3,2,1)$ | $3$ | $33$ | $3$ | $\operatorname{diag}(1,1,1,2,2,3)$ |
| $(3,3)$ | $2$ | $32$ | $4$ | $\operatorname{diag}(1,1,1,2,2,2)$ |
| $(4,1,1)$ | $3$ | $33$ | $3$ | $\operatorname{diag}(1,1,1,1,2,3)$ |
| $(4,2)$ | $2$ | $32$ | $4$ | $\operatorname{diag}(1,1,1,1,2,2)$ |
| $(5,1)$ | $2$ | $32$ | $4$ | $\operatorname{diag}(1,1,1,1,1,2)$ |
| $(6)$ | $1$ | $31$ | $5$ | $\operatorname{diag}(1,1,1,1,1,1)$ |

**Proof.** Substitute $r$ in $30+r$; the codimension is $36-(30+r)=6-r$. The representatives have the required eigenvalue multiplicities.

### The Closure Order

**Theorem.** $S_\mu$ meets the closure of $S_\lambda$ if and only if $\mu$ is coarser than $\lambda$, that is, if and only if $\lambda$ refines $\mu$. In particular the simple stratum is open and dense, and the closure of the discriminant is the union of all strata with a repeated eigenvalue.

**Proof.** Coalescing eigenvalues is a specialization: a matrix in $S_\lambda$ can be deformed to a matrix in $S_\mu$ exactly when each part of $\mu$ is a sum of parts of $\lambda$. The closure is the union of the strata obtained by such coalescences. The simple partition refines every partition, so its closure is the whole algebra.

**Corollary (the discriminant).** The discriminant is the closure of the stratum $S_{(2,1,1,1,1)}$, and that stratum is its open dense part, of dimension $35$.

**Proof.** A repeated root means some multiplicity is at least two; the generic repeated-root matrix has exactly one double root and four simple roots, which is the partition $(2,1,1,1,1)$.

### The Root Set Inside the Strata

**Proposition.** The root set is the fibre of the characteristic map over the polynomial $t^6-1$:

$$
\{H:H^6=I_6,\ \text{six distinct eigenvalues}\}
=\chi^{-1}(t^6-1)\cap U .
$$

It has dimension $30$, and it lies in the simple stratum.

**Proof.** $H^6=I$ with simple spectrum means the eigenvalues are the six distinct sixth roots, so $\chi_H=t^6-1$. Conversely, a matrix with characteristic polynomial $t^6-1$ and simple spectrum has eigenvalues the six sixth roots, hence satisfies $H^6=I$ (it is diagonalizable with those eigenvalues). The fibre over $t^6-1$ is the conjugacy class of $\operatorname{diag}(\zeta_1,\dots,\zeta_6)$, of dimension $30$.

**Remark (the six parameters).** The simple stratum has dimension $36$; the root set has dimension $30$. The difference is the six eigenvalues: on $U$ the characteristic map is a submersion onto the six-dimensional space of monic sextics with simple roots, and the root set is the fibre over one point. **The root fixes the spectrum; the stratum forgets it.**

## The Cyclic Element and the Torus

### Cyclic Elements

**Definition.** An element $A\in M_6(\mathbb{C})$ is **cyclic** if there is a vector $v\in\mathbb{C}^6$ such that

$$
v,\ Av,\ A^2v,\ \dots,\ A^5v
$$

is a basis of $\mathbb{C}^6$. Equivalently, the minimal polynomial of $A$ has degree six.

**Proposition.** $A$ is cyclic if and only if the centralizer of $A$ in $M_6$ is the algebra $\mathbb{C}[A]$ of polynomials in $A$, of dimension six:

$$
Z(A)=\{B:AB=BA\}=\mathbb{C}[A]\cong\mathbb{C}[t]/(m_A(t)).
$$

**Proof.** If $A$ is cyclic, the basis $v,Av,\dots,A^5v$ identifies $\mathbb{C}^6$ with $\mathbb{C}[t]/(m_A)$ as a module over $\mathbb{C}[t]$, and the commuting endomorphisms are the multiplications by polynomials, that is $\mathbb{C}[A]$. Conversely, if the centralizer is six-dimensional, the double centralizer theorem gives that $\mathbb{C}[A]$ is its own centralizer, which forces the minimal polynomial to have degree six.

**Corollary (the cyclic centralizer).** For a cyclic element with simple spectrum,

$$
Z(A)\cong\mathbb{C}^6,
\qquad
Z(A)\cap GL_6\cong(\mathbb{C}^\times)^6,
\qquad
\text{image of }Z(A)\cap GL_6\text{ in }PGL_6\cong(\mathbb{C}^\times)^5 .
$$

The first is the algebra $\mathbb{C}^6$; the second is its unit group, the torus of dimension six; the third is the gauge torus of dimension five.

**Proof.** If the spectrum is simple, $A$ is diagonalizable and $\mathbb{C}[A]$ is the algebra of diagonal matrices in the eigenbasis, isomorphic to $\mathbb{C}^6$. Its units are the diagonal matrices with nonzero entries, $(\mathbb{C}^\times)^6$. The projective quotient removes the overall scalar, leaving $(\mathbb{C}^\times)^5$.

**Corollary (the root).** For the root $H$ of *Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$*, the centralizer in $GL_6$ is the maximal torus $(\mathbb{C}^\times)^6$, of dimension six, and the gauge is its projective quotient, of dimension five.

**Proof.** $H$ has simple spectrum and $\chi_H=t^6-1$, so it is cyclic. Its centralizer is the diagonal torus in the eigenbasis.

### The Orbit

**Theorem.** The conjugacy class of a cyclic element has dimension $30$:

$$
\dim(GL_6\cdot A)=36-6=30 .
$$

**Proof.** The orbit–stabilizer theorem: the stabilizer is the centralizer, of dimension six.

**Corollary.** The simple stratum is the union of the orbits of the cyclic elements, each of dimension $30$; the eigenvalues are the six parameters transverse to the orbit.

**Proof.** A matrix with simple spectrum is cyclic, and its orbit is the set of matrices with the same spectrum, of dimension $30$. The simple stratum is the union over the six-dimensional space of spectra.

**Remark (the non-cyclic centralizer).** A non-cyclic element has a centralizer of dimension greater than six. The extreme case is the scalar matrix $\lambda I_6$, whose centralizer is all of $M_6$, of dimension $36$. The dimension of the centralizer measures the degeneracy of the spectrum: it is six exactly on the cyclic elements, and it grows as the Jordan structure coarsens.

## The Spectral Projectors

### The Lagrange Formula

**Theorem.** Let $A$ have simple spectrum $\lambda_1,\dots,\lambda_6$. Then the six matrices

$$
P_i=\prod_{j\neq i}\frac{A-\lambda_jI_6}{\lambda_i-\lambda_j},
\qquad i=1,\dots,6,
$$

satisfy

$$
P_i^2=P_i,\qquad
P_iP_j=\delta_{ij}P_i,\qquad
\sum_{i=1}^{6}P_i=I_6,\qquad
A=\sum_{i=1}^{6}\lambda_iP_i,
$$

and $\operatorname{rank}P_i=1$, $\operatorname{tr}P_i=1$.

**Proof.** The polynomial $L_i(t)=\prod_{j\neq i}(t-\lambda_j)/(\lambda_i-\lambda_j)$ is the Lagrange interpolation polynomial with $L_i(\lambda_j)=\delta_{ij}$. On the eigenline of $\lambda_j$, $L_i(A)$ acts by $L_i(\lambda_j)=\delta_{ij}$; so $P_i$ is the projection onto the $i$-th eigenline along the sum of the others. The spectral identity $A=\sum_i\lambda_iP_i$ holds on each eigenvector.

**Corollary (the projectors are polynomials).** The $P_i$ are polynomials in $A$ of degree at most five, with coefficients that are symmetric functions of the eigenvalues.

**Proof.** The Lagrange polynomial has degree five in $t$; substituting $A$ gives a polynomial in $A$ of degree at most five.

### The Residue Formula

**Theorem.** Let $\gamma_i$ be a small positively oriented circle around $\lambda_i$, separating it from the other eigenvalues. Then

$$
P_i=\frac{1}{2\pi\mathrm i}\oint_{\gamma_i}(zI_6-A)^{-1}\,dz .
$$

**Proof.** In the eigenbasis, the resolvent is $\operatorname{diag}(1/(z-\lambda_1),\dots,1/(z-\lambda_6))$; the residue at $z=\lambda_i$ is the coordinate projector $P_i$. The contour integral picks the residue.

**Corollary (the cluster projector).** For any $A$, not necessarily with simple spectrum, and for a contour $\gamma$ enclosing a cluster of eigenvalues and no others,

$$
\Pi_\gamma=\frac{1}{2\pi\mathrm i}\oint_\gamma(zI_6-A)^{-1}\,dz
$$

is an idempotent, the spectral projector onto the generalized eigenspace of the cluster. For a simple spectrum and a contour around one eigenvalue, $\Pi_\gamma=P_i$.

**Proof.** The resolvent is holomorphic off the spectrum; the contour integral of a resolvent is idempotent (the residue calculus gives $\Pi_\gamma^2=\Pi_\gamma$), it commutes with $A$, and its image is the sum of the generalized eigenspaces of the eigenvalues inside $\gamma$.

**Corollary (the sum of the projectors).** If $\gamma$ encloses all six eigenvalues, $\Pi_\gamma=I_6$.

**Proof.** The resolvent at infinity is $z^{-1}I+O(z^{-2})$, so the residue at infinity is $I$; the sum of all residues is zero, hence the integral over a large circle is $I$.

### The Limits at a Repeated Root

**Theorem (the degeneration).** Let $A(\varepsilon)$ be a holomorphic family of matrices, and suppose that at $\varepsilon=0$ two eigenvalues coalesce. Then:

- the individual Lagrange projectors $P_i(\varepsilon)$ may have poles of order one at $\varepsilon=0$;
- the sum of the projectors over the coalescing cluster has a holomorphic limit, the spectral projector onto the generalized eigenspace;
- the weighted sum $\sum_i\lambda_i(\varepsilon)P_i(\varepsilon)=A(\varepsilon)$ has the limit $A(0)$, and the nilpotent part of $A(0)$ is the limit of the weighted differences.

**Proof.** The projectors are rational functions of $A$ with denominators $\lambda_i-\lambda_j$; when two eigenvalues coalesce, the denominators vanish. The cluster sum is the contour integral around the cluster, which is holomorphic as long as the cluster stays separated from the other eigenvalues. The spectral identity is an identity for every $\varepsilon$, so its limit is $A(0)$.

**Example (the Jordan block).** Consider the $2\times2$ family

$$
A(\varepsilon)=\begin{pmatrix}\lambda+\varepsilon&1\\0&\lambda\end{pmatrix},
\qquad
\chi_{A(\varepsilon)}(t)=(t-\lambda-\varepsilon)(t-\lambda).
$$

The eigenvalues are $\lambda+\varepsilon$ and $\lambda$; the eigenvectors are $e_1$ and $(1,-\varepsilon)$. The Lagrange projectors are

$$
P_+(\varepsilon)=\begin{pmatrix}1&1/\varepsilon\\0&0\end{pmatrix},
\qquad
P_-(\varepsilon)=\begin{pmatrix}0&-1/\varepsilon\\0&1\end{pmatrix}.
$$

Both have a pole at $\varepsilon=0$; their sum is $I_2$ for every $\varepsilon$, and the weighted sum is

$$
(\lambda+\varepsilon)P_+(\varepsilon)+\lambda P_-(\varepsilon)
=\begin{pmatrix}\lambda+\varepsilon&1\\0&\lambda\end{pmatrix}=A(\varepsilon),
$$

which tends to $A(0)=\lambda I_2+E_{12}$. The cluster projector $P_++P_-=I_2$ is the spectral projector of $A(0)$ onto its generalized eigenspace, which is the whole space. The nilpotent part $E_{12}$ is the limit of $\varepsilon P_+(\varepsilon)$.

**Corollary (no continuous eigenbasis).** In the example, the eigenvectors $e_1$ and $(1,-\varepsilon)$ can be chosen continuously, but they become linearly dependent at $\varepsilon=0$; the normalized eigenvectors both tend to $e_1$. There is no continuous basis of eigenvectors through the repeated root.

**Remark (the monodromy).** The eigenvalues are algebraic functions of $A$, not rational; a loop around the discriminant permutes them. The unordered set of spectral projectors is single-valued, while a projector labeled by "the eigenvalue that started at $\lambda_i$" is not. On the simple stratum each $P_i$ is a polynomial in $A$ once the eigenvalue $\lambda_i$ is named; the monodromy acts on the naming, not on the unordered set of projectors.

## The Degeneration of the Root

**Proposition.** The root set is the simple-spectrum part of the hypersurface $H^6=I_6$. At a matrix with a repeated sixth root, the Lagrange projectors are not defined; the spectral projectors of the distinct eigenvalues are the cluster projectors, and the rank-one projectors of the repeated eigenvalue do not exist.

**Proof.** The Lagrange formula requires the six eigenvalues to be distinct. If two are equal, the denominators vanish. The contour integral around the repeated eigenvalue gives the projector onto its generalized eigenspace, of rank equal to the multiplicity; the individual rank-one projectors would require a splitting of that eigenspace, which is not canonical.

**Corollary (the centralizer grows).** At a repeated root, the centralizer of $H$ in $GL_6$ is strictly larger than the maximal torus, and the orbit of $H$ has dimension strictly less than $30$.

**Proof.** A repeated eigenvalue gives a nontrivial generalized eigenspace, and there are additional commuting endomorphisms mixing the repeated eigenlines; the centralizer contains the torus and more. The orbit dimension is $36$ minus the centralizer dimension.

**Example.** $H=\operatorname{diag}(1,1,\zeta,\zeta^2,\zeta^3,\zeta^4)$ satisfies $H^6=I_6$ but has a repeated eigenvalue $1$. Its centralizer contains $GL_2$ on the first two coordinates, of dimension four, in addition to the torus on the other four; the orbit is smaller than $30$. The two Lagrange projectors of the eigenvalue $1$ do not exist; the spectral projector onto the $1$-eigenspace is the rank-two projector onto the first two coordinates.

**Remark (the root set is not closed).** The root set is open in $H^6=I_6$ but not closed in $M_6$: a limit of roots can have a repeated eigenvalue. The boundary is the discriminant intersected with the hypersurface. **The root is a simple-spectrum object; the repeated-root matrices are its degeneration.**

## Summary

The characteristic sextic of $A\in M_6(\mathbb{C})$ is

$$
\chi_A(t)=t^6-s_1t^5+s_2t^4-s_3t^3+s_4t^2-s_5t+s_6,
\qquad
s_1=\operatorname{tr}A,\quad s_6=\det A .
$$

Its multiplicity pattern is a partition of $6$. The stratum of a partition with $r$ parts has dimension $30+r$:

| Partition | $r$ | Dimension | Codimension |
|---|---|---|---|
| $(1^6)$ | $6$ | $36$ | $0$ |
| $(2,1^4)$ | $5$ | $35$ | $1$ |
| $(2,2,1,1)$ | $4$ | $34$ | $2$ |
| $(3,1,1,1)$ | $4$ | $34$ | $2$ |
| $(2,2,2)$ | $3$ | $33$ | $3$ |
| $(3,2,1)$ | $3$ | $33$ | $3$ |
| $(4,1,1)$ | $3$ | $33$ | $3$ |
| $(3,3)$ | $2$ | $32$ | $4$ |
| $(4,2)$ | $2$ | $32$ | $4$ |
| $(5,1)$ | $2$ | $32$ | $4$ |
| $(6)$ | $1$ | $31$ | $5$ |

$$
\boxed{\ \dim S_\lambda=30+r,\qquad \text{simple spectrum }36,\qquad \text{one root }31 .\ }
$$

A cyclic element has centralizer $\mathbb{C}[A]\cong\mathbb{C}[t]/(m_A)$, of dimension $6$; with simple spectrum this is $\mathbb{C}^6$, whose unit group is the maximal torus. Its orbit has dimension $30$. The root $H$ is cyclic, and its gauge is the projective centralizer of dimension $5$.

On the simple stratum the spectral projectors are the Lagrange projectors $P_i=\prod_{j\neq i}(A-\lambda_j)/(\lambda_i-\lambda_j)$; at a repeated root the individual projectors have poles, the cluster projectors extend, and the nilpotent part is the residue.

| Object | Data |
|---|---|
| Characteristic sextic | $\chi_A$, degree $6$ |
| Strata | $11$ partitions of $6$ |
| Simple stratum | open dense, dimension $36$ |
| Discriminant | codimension $1$, $S_{(2,1^4)}$ |
| Cyclic centralizer | $\mathbb{C}[t]/(m_A)$, dimension $6$ |
| Cyclic orbit | dimension $30$ |
| Root set | fibre over $t^6-1$, dimension $30$ |
| Projectors | Lagrange on $U$, cluster at the discriminant |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_A(t)$ | the characteristic sextic $\det(tI_6-A)$ |
| $s_1,\dots,s_6$ | the coefficients, elementary symmetric functions of the eigenvalues |
| $\lambda_1,\dots,\lambda_6$ | the eigenvalues with multiplicity |
| $\Delta(A)$ | the discriminant $\prod_{i<j}(\lambda_i-\lambda_j)^2$ |
| $S_\lambda$ | the stratum of multiplicity pattern $\lambda$ |
| $r$ | the number of distinct eigenvalues (parts of $\lambda$) |
| $Z(A)$ | the centralizer of $A$ in $M_6$ |
| $P_i$ | the Lagrange spectral projector of $\lambda_i$ |
| $\Pi_\gamma$ | the cluster projector of a contour $\gamma$ |

## Further Reading

- [Roots of Unity and the Lagrange Idempotents of $M_6(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m6c.html), for the root and its simple spectrum.
- [The Matrix Algebra $M_6(\mathbb{C})$](the-matrix-algebra-m6c.html), for the trace, the determinant and the characteristic polynomial.
- [The Element, the Coordinates and the Trace of $M_6(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m6c.html), for the scalar-traceless decomposition.
- [Spectral Theory and the Spectral Projectors of $M_6(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m6c.html), for the Hermitian spectral theorem.
- [The Geometry of the Idempotents of $M_6(\mathbb{C})$](the-geometry-of-the-idempotents-of-m6c.html), for the projectors as points of a homogeneous space.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 1995), for the contour integral projectors and their limits at a coalescence.
- James E. Humphreys, *Linear Algebraic Groups* (Springer, 1975), for the cyclic elements and the maximal torus.
