# __The Three Sectors of the Quaternion Algebra__

## Introduction

Two conditions cut the quaternion algebra into four cells: the vanishing of the quaternion norm and the vanishing of the squared length of the vector part. Because the norm is positive definite, one of the four cells is empty and the other three are nonempty. The three are the **sectors**: the non-real quaternions, the real axis minus the origin, and the origin. This article defines the cells, proves that exactly three are nonempty, describes each sector, computes its dimension and closure, and records the absence of defective elements and of nonzero norm-degenerate elements. A summary table collects the four cells.

The algebra is [Quaternion Algebra](quaternion-algebra.html); the norm is [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html); the spectral criterion is [Spectral Regularity and Degeneracy in the Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-quaternion-algebra.html); the comparison of the two conditions is [Relations between the Quaternion Norm and Spectral Regularity and Degeneracy](relations-between-the-quaternion-norm-and-spectral-regularity-and-degeneracy.html); the biquaternion analogue is [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html).

**Notation.** $\tilde q=q_t+\vec q=q_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, $\vec q^2=-|\vec q|^2e_t$, $\tilde q^{\natural}=q_t-\vec q$, $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$, $|\tilde q|=\sqrt{\langle\tilde q\rangle_{\natural}}$, $s=|\vec q|$.

## The Two Predicates and the Sectors

**Definition (the cells).** For $i,j\in\{0,1\}$ set
$$\Sigma_{ij}=\{\tilde q\in\mathbb H:\ |\tilde q|^2\ne0\iff i=1,\quad |\vec q|^2\ne0\iff j=1\}.$$
Explicitly,
$$\Sigma_{11}=\{|\tilde q|^2\ne0,\ |\vec q|^2\ne0\},\quad \Sigma_{10}=\{|\tilde q|^2\ne0,\ |\vec q|^2=0\},$$
$$\Sigma_{01}=\{|\tilde q|^2=0,\ |\vec q|^2\ne0\},\quad \Sigma_{00}=\{|\tilde q|^2=0,\ |\vec q|^2=0\}.$$

**Theorem (partition).** The four sets are pairwise disjoint and cover $\mathbb H$:
$$\mathbb H=\Sigma_{11}\sqcup\Sigma_{10}\sqcup\Sigma_{01}\sqcup\Sigma_{00}.$$

*Proof.* Each element has exactly one truth value for each of the two conditions, hence lies in exactly one of the four cells.

**Theorem (explicit description).**
$$\Sigma_{11}=\mathbb H\setminus\mathbb R,\qquad \Sigma_{10}=\mathbb R^\times,\qquad \Sigma_{01}=\varnothing,\qquad \Sigma_{00}=\{0\}.$$

*Proof.* The norm is positive definite, so $|\tilde q|^2=0$ exactly when $\tilde q=0$; the spectral form is positive semidefinite with radical the real axis, so $|\vec q|^2=0$ exactly when $\tilde q\in\mathbb R$. Hence $\Sigma_{11}$ is the set of nonzero quaternions outside $\mathbb R$, which is $\mathbb H\setminus\mathbb R$ because $0$ is real; $\Sigma_{10}$ is $\mathbb R\setminus\{0\}$; $\Sigma_{01}$ requires $\tilde q=0$ and $\tilde q\notin\mathbb R$, which is impossible; $\Sigma_{00}$ requires $\tilde q=0$ and $\tilde q\in\mathbb R$, which is the origin.

**Corollary (three nonempty, one empty).** The witnesses
$$\vec e_x\in\Sigma_{11},\qquad 1\in\Sigma_{10},\qquad 0\in\Sigma_{00}$$
show that the first, second and fourth cells are nonempty; the third is empty. The three nonempty cells are the **sectors**.

## The Sector of the Non-Real Quaternions

**Theorem.** $\Sigma_{11}=\mathbb H\setminus\mathbb R$. It is open, dense, connected and simply connected, of real dimension four. Its closure is $\mathbb H$, its boundary is the real axis $\mathbb R$, and it is not closed.

*Proof.* The complement of the closed line $\mathbb R$ is open; a line has empty interior, so the complement is dense. The map $\tilde q\mapsto(q_t,\vec q)$ is a homeomorphism of $\mathbb H\setminus\mathbb R$ onto $\mathbb R\times(\mathbb R^3\setminus\{0\})$, which is homeomorphic to $\mathbb R\times S^2\times\mathbb R_{>0}$; this space is connected and simply connected. The closure is $\mathbb H$ because every real quaternion is a limit of non-real ones. The boundary is $\mathbb R$ because the set is open and its closure is $\mathbb H$.

**Spectral description.** For $\tilde q\in\Sigma_{11}$ the eigenvalues $q_t\pm i|\vec q|$ are distinct, each of algebraic and geometric multiplicity two; $L_{\tilde q}$ is semisimple and diagonalisable over $\mathbb C$, with no real eigenvector. Its real canonical form is two copies of the rotation-scaling block. The eigenbasis is constructed in [Eigenvalue Decomposition and Eigenbasis of a Quaternion](eigenvalue-decomposition-and-eigenbasis-of-a-quaternion.html).

**Norm description.** Every element is a unit, $|\tilde q|>0$, and the polar decomposition is $\tilde q=|\tilde q|(\cos\theta+\sin\theta J_{\tilde q})$ with $\theta\in(0,\pi)$ and $J_{\tilde q}=\vec q/|\vec q|$.

**Proposition (not a subgroup).** $\Sigma_{11}$ is invariant under conjugation, under inversion and under multiplication by nonzero real scalars, but it is not closed under multiplication:
$$(1+\vec e_x)(1-\vec e_x)=2\in\mathbb R.$$

*Proof.* The first three assertions follow from $|\tilde q^{\natural}|=|\tilde q|$, $|\tilde q^{-1}|=|\tilde q|^{-1}$ and $|\lambda\tilde q|^2=\lambda^2|\tilde q|^2$; the product computes to $1-\vec e_x^2=2$.

## The Sector of the Real Axis Minus the Origin

**Theorem.** $\Sigma_{10}=\mathbb R^\times$. It is a one-dimensional subgroup of $\mathbb H^\times$, central in $\mathbb H$, with two connected components $\mathbb R_{>0}$ and $\mathbb R_{<0}$. It is locally closed, not open and not closed in $\mathbb H$; its closure is $\mathbb R=\Sigma_{10}\cup\Sigma_{00}$, and its boundary is $\{0\}$.

*Proof.* The set is $\mathbb R\setminus\{0\}$; it is closed under multiplication and inversion, and real scalars commute with every quaternion. The two signs are the two components. A line has empty interior in $\mathbb R^4$, so it is not open; the origin is a limit point, so it is not closed; it is the intersection of the closed set $\mathbb R$ with the open set $\mathbb H\setminus\{0\}$, hence locally closed. The closure is $\mathbb R$, and the boundary is the origin.

**Spectral description.** For $q_t\ne0$, $L_{\tilde q}=q_t\,\mathrm{id}$, the spectrum is the singleton $\{q_t\}$, the eigenspace is all of $\mathbb H_{\mathbb C}$, and the minimal polynomial is $\lambda-q_t$. Every nonzero vector is an eigenvector and every basis is an eigenbasis; the element is semisimple. The spectrum is a single nonzero real point.

**Norm description.** $|\tilde q|^2=q_t^2>0$, the inverse is $q_t^{-1}$, and the polar angle is $\theta=0$ for $q_t>0$ and $\theta=\pi$ for $q_t<0$, with $J$ arbitrary. The positive ray is the identity component of the group.

**Remark (the only coexistence).** $\Sigma_{10}$ is the only sector whose elements are norm-regular and spectrally degenerate. Its elements are units and semisimple, so the degeneracy is neither non-invertibility nor defect: it is the collapse of the two eigenvalues onto the real axis. In the split-quaternion and biquaternion algebras the corresponding cell contains defective elements; see [Spectral Regularity and Degeneracy in the Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-quaternion-algebra.html).

## The Sector of the Origin

**Theorem.** $\Sigma_{00}=\{0\}$. It is a single point, closed, of dimension zero, and the unique non-unit of $\mathbb H$. For $\tilde q=0$, $L_0=0$, the characteristic polynomial is $\lambda^4$, the minimal polynomial is $\lambda$, and the spectrum is $\{0\}$; every nonzero vector is an eigenvector and every basis is an eigenbasis.

*Proof.* The cell was computed above; the norm is zero only at the origin, so the origin is the only non-unit. The matrix of $L_0$ is zero, and the polynomial statements are immediate.

**Proposition (semisimple).** The origin is semisimple: $\mathbb R[0]=\mathbb R$ is a field, and the minimal polynomial $\lambda$ is squarefree.

**Proposition (closure).** The origin lies in the closure of both $\Sigma_{11}$ and $\Sigma_{10}$; it is the boundary of $\Sigma_{10}$ and a frontier point of $\Sigma_{11}$.

*Proof.* Every neighborhood of $0$ contains nonzero real quaternions and non-real quaternions.

**Remark (doubly degenerate, but not a cone).** The origin is the only element that is both norm-degenerate and spectrally degenerate. In the split-quaternion and biquaternion algebras the doubly degenerate set is a cone with nonzero points; here the positive definiteness of both forms collapses it to a point.

## Dimensions and Closures

The dimensions are the real dimensions of the cells as subsets of $\mathbb H\cong\mathbb R^4$.

| sector | condition | description | dimension |
|---|---|---|---|
| $\Sigma_{11}$ | $|\tilde q|^2\ne0,\ |\vec q|^2\ne0$ | non-real quaternions; open, dense, connected; closure $\mathbb H$ | $4$ |
| $\Sigma_{10}$ | $|\tilde q|^2\ne0,\ |\vec q|^2=0$ | real axis minus the origin; two components; closure $\mathbb R$ | $1$ |
| $\Sigma_{01}$ | $|\tilde q|^2=0,\ |\vec q|^2\ne0$ | empty | — |
| $\Sigma_{00}$ | $|\tilde q|^2=0,\ |\vec q|^2=0$ | the origin; closed; closure $\{0\}$ | $0$ |

**Theorem (the closures).** The closures of the four cells are
$$\overline{\Sigma_{11}}=\mathbb H,\qquad \overline{\Sigma_{10}}=\mathbb R,\qquad \overline{\Sigma_{01}}=\varnothing,\qquad \overline{\Sigma_{00}}=\{0\}.$$
Each closure is a union of cells, so the partition satisfies the frontier condition of a stratification.

*Proof.* The only nontrivial closure is that of $\Sigma_{11}$, which is $\mathbb H$ because the real axis is approximated by non-real quaternions; $\mathbb R$ is closed, and the remaining two cells are closed or empty. The closures are $\Sigma_{11}\cup\Sigma_{10}\cup\Sigma_{00}$, $\Sigma_{10}\cup\Sigma_{00}$, $\varnothing$ and $\Sigma_{00}$ respectively.

**Remark (the dimensions do not add).** $4+1+0=5>4$. The cells are disjoint, but the closures overlap: the real axis is the boundary of the open sector, and the origin is the boundary of the line. The dimension count of a stratification is not the dimension of the ambient space.

**Corollary (the boundary).** The boundary of $\Sigma_{11}$ is $\Sigma_{10}\cup\Sigma_{00}=\mathbb R$; the boundary of $\Sigma_{10}$ is $\Sigma_{00}$; the boundary of $\Sigma_{00}$ is $\Sigma_{00}$.

## Absence of Defect and of Nonzero Norm-Degenerate Elements

**Theorem (no defect).** Every element of every sector is semisimple, and there is no defective element in $\mathbb H$. The minimal polynomial is $\lambda-q_t$ on $\Sigma_{10}\cup\Sigma_{00}$ and $(\lambda-q_t)^2+|\vec q|^2$ on $\Sigma_{11}$; both are squarefree.

*Proof.* On the real axis $\mathbb R[\tilde q]=\mathbb R$; off it $\mathbb R[\tilde q]\cong\mathbb C$. Both are fields, and the displayed minimal polynomials have distinct roots.

**Theorem (no nonzero norm-degenerate element).** The norm-degenerate set is $\Sigma_{00}=\{0\}$. It contains no zero divisor, and every nonzero quaternion is a unit:
$$\mathbb H^\times=\mathbb H\setminus\{0\}=\Sigma_{11}\cup\Sigma_{10}.$$

*Proof.* Positive definiteness gives the first statement; multiplicativity of the norm gives the absence of zero divisors; every nonzero element has the inverse $\tilde q^{\natural}/|\tilde q|^2$.

**Corollary (the sectors are exhaustive).** The three nonempty sectors are exactly the combinations that the positive definite norm permits; the fourth is forbidden. The table of the previous section is therefore complete.

**Remark (the contrast with the biquaternion algebra).** In $\mathbb B$ all four sectors are nonempty: the sector $\Sigma_{01}$ that is empty in $\mathbb H$ is present there, and its nonzero points are zero divisors. In $\mathbb H$ that sector is empty because the norm is definite. The comparison is in [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html).

## Summary

The two conditions $|\tilde q|^2\ne0$ and $|\vec q|^2\ne0$ partition $\mathbb H$ into four cells. Because the norm is positive definite and the spectral form has radical the real axis, the cells are
$$\Sigma_{11}=\mathbb H\setminus\mathbb R,\qquad \Sigma_{10}=\mathbb R^\times,\qquad \Sigma_{01}=\varnothing,\qquad \Sigma_{00}=\{0\}.$$
The first is open, dense, connected and four-dimensional; the second is a one-dimensional subgroup with two components, locally closed, with closure the real axis; the third is empty; the fourth is a closed point, the only non-unit, the only doubly degenerate element and the only element of the norm-degenerate set.

Every element is semisimple, so there is no defective element and no defective sector. No nonzero element is norm-degenerate, so every nonzero quaternion is a unit and $\mathbb H$ has no zero divisor. The fourth cell is empty precisely because the norm is definite; in the biquaternion algebra it is nonempty and carries zero divisors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Sigma_{ij}$ | the cell with norm truth value $i$ and spectral truth value $j$ |
| $\Sigma_{11}=\mathbb H\setminus\mathbb R$ | the non-real sector |
| $\Sigma_{10}=\mathbb R^\times$ | the punctured real axis |
| $\Sigma_{01}=\varnothing$ | the empty cell |
| $\Sigma_{00}=\{0\}$ | the origin |
| $\mathbb H^\times=\mathbb H\setminus\{0\}$ | the unit group |
| $|\tilde q|^2=q_t^2+|\vec q|^2$ | the quaternion norm |
| $|\vec q|^2$ | the spectral form |
| dimension | real dimension as a subset of $\mathbb H\cong\mathbb R^4$ |
| closure | topological closure in $\mathbb H$ |

## Further Reading

- [Quaternion Algebra](quaternion-algebra.html), for the multiplication and the scalar–vector decomposition.
- [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html), for the norm and the unit group.
- [Spectral Regularity and Degeneracy in the Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-quaternion-algebra.html), for the spectral criterion.
- [Eigenvalue Decomposition and Eigenbasis of a Quaternion](eigenvalue-decomposition-and-eigenbasis-of-a-quaternion.html), for the eigenbasis of the non-real sector.
- [Relations between the Quaternion Norm and Spectral Regularity and Degeneracy](relations-between-the-quaternion-norm-and-spectral-regularity-and-degeneracy.html), for the two forms and the chain of invariants.
- [Comparison of Norms and Invertibility](comparison-of-norms-and-invertibility.html), for the norms of the eight algebras.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors of $\mathbb B$ and their comparison with $\mathbb H$.
- [The Eight Algebras Compared](the-eight-algebras-compared.html), for the place of $\mathbb H$ among the eight.
