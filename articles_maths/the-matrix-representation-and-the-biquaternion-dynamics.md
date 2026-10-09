# __The Matrix Representation and the Biquaternion Dynamics__

## Introduction

The biquaternion algebra is isomorphic to the algebra of two-by-two complex matrices, and the isomorphism transports the quadratic family to the matrix family $M\mapsto M^2+N$ with $N=\Phi(\tilde C)$, the conjugations to the operations of adjugate, conjugate transpose and their composition, and the two norms $N$ and $\|\cdot\|_E$ to the determinant and, up to the factor $\sqrt2$, the Frobenius norm. The model is the working tool of the category: every computation in the biquaternion dynamics is a computation in $M_2(\mathbb{C})$, and every invariant of the element is an invariant of its matrix. The article states what the model carries, what it does not, and where the passage has a twist.

The isomorphism and its basic properties, the trace and the determinant, the spectrum and the Cayley–Hamilton identity are *Introduction to the 2×2 Matrix Representation of Biquaternions* and *Biquaternion 2×2 Matrix Element Representation*; the four conjugations in matrix form are in the second of these; the quadratic family is *The Biquaternion Quadratic Map and Its Julia Sets*; the norms are *Biquaternion Norm and Invertibility*. The several-variable complex theory the matrix family belongs to is *Several Complex Variables* and the holomorphic dynamics of Part III.

The article owns the transport of the family, the norm comparison that makes the escape notions agree, the eigenvalue and determinant invariants along the orbit, the reading of the dynamics as two-variable matrix iteration, and the warning that the isomorphism concerns the elements and not the operators on them. It does not re-derive the isomorphism or the conjugations.

**Standing convention.** $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ is the matrix realization, $M=\Phi(\tilde Q)$, $N=\Phi(\tilde C)$, and the matrix family is

$$
\Phi\circ F_{\tilde C}\circ\Phi^{-1}=\bigl(M\mapsto M^2+N\bigr).
$$

## The Model as a Model of the Dynamics

**Theorem (transport of the family).** For every $n$, $\Phi(F_{\tilde C}^n(\tilde Q))=p_n(\Phi(\tilde Q))$, where $p_0(M)=M$ and $p_{n+1}(M)=p_n(M)^2+N$. Consequently the map $\Phi$ restricts to a bijection

$$
\mathcal K_{\tilde C}\;\longleftrightarrow\;\{M\in M_2(\mathbb{C}) : (p_n(M))_{n\ge0} \text{ bounded}\}, \qquad J_{\tilde C}\leftrightarrow \text{the boundary} ,
$$

and the dynamics of the biquaternion family is conjugate to the dynamics of a polynomial map of the four complex entries of the matrix.

**Proof.** $\Phi$ is multiplicative and $\mathbb{C}$-linear, so $\Phi(\tilde Q^2+\tilde C)=\Phi(\tilde Q)^2+\Phi(\tilde C)$ and induction gives the transport of the orbit; a bijective linear map preserves boundedness and boundaries.

**Remark (the reduction to four complex coordinates).** The matrix has four complex entries; with $M=\left(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\right)$ the family is the four-dimensional complex map

$$
(\alpha,\beta,\gamma,\delta)\longmapsto(\alpha^2+\beta\gamma+n_1,\ \beta(\alpha+\delta)+n_2,\ \gamma(\alpha+\delta)+n_3,\ \gamma\beta+\delta^2+n_4)
$$

with $N=\left(\begin{smallmatrix}n_1&n_2\\n_3&n_4\end{smallmatrix}\right)$; the diagonal entries are quadratic in one line and the off-diagonal entries are linear in the trace $\alpha+\delta$ and the off-diagonal pair. **The map of the entries is a polynomial map of degree two of $\mathbb{C}^4$**, and the four complex dimensions of the space appear here for the first time.

## The Norm Comparison and the Escape Notions

**Proposition (the Frobenius and Euclidean norms).** For every biquaternion, $\|\Phi(\tilde Q)\|_F=\sqrt2\,\|\tilde Q\|_E$; for every pair, $\|\tilde P\tilde Q\|_E\le\sqrt2\,\|\tilde P\|_E\|\tilde Q\|_E$; and the induced operator norm satisfies $\|M\|_2\le\sqrt2\,\|\tilde Q\|_E$.

**Proof.** The Frobenius norm of the explicit matrix $\left(\begin{smallmatrix}Q_0-iQ_3&-iQ_1-Q_2\\-iQ_1+Q_2&Q_0+iQ_3\end{smallmatrix}\right)$ is the squared sum of the moduli of the entries, which is $\sum_\mu|Q_\mu|^2$ computed twice, hence $\|\Phi(\tilde Q)\|_F^2=2\|\tilde Q\|_E^2$. Multiplicativity of $\Phi$ and submultiplicativity of the Frobenius norm give $\sqrt2\|\tilde P\tilde Q\|_E=\|\Phi(\tilde P\tilde Q)\|_F\le\|\Phi(\tilde P)\|_F\|\Phi(\tilde Q)\|_F=2\|\tilde P\|_E\|\tilde Q\|_E$, hence the second inequality. The operator norm is bounded by the Frobenius norm, which is $\sqrt2\|\tilde Q\|_E$.

**Corollary (the escape notions agree).** A biquaternion orbit is bounded in the Euclidean norm exactly when its matrix orbit is bounded in the Frobenius norm, and exactly when it is bounded in the operator norm. The filled Julia set and the Julia set are the same sets in the two models.

**Proof.** The three norms are pairwise comparable on the fixed finite-dimensional space, by the proposition, and a sequence is bounded for one exactly when it is bounded for the others. The biquaternion norm $N$ is a different object: it is the determinant of the matrix and the product $\tilde Q\tilde Q^{\natural}$, it is complex-valued and indefinite and vanishes on the zero divisors, so boundedness of $N$ is **not** equivalent to boundedness in the Euclidean norm — a nilpotent element has $N=0$ and arbitrarily large Euclidean norm.

**Remark (the constant $\sqrt2$ is the only discrepancy).** Every statement of the category phrased in a norm differs between the algebra and the model by at most the factor $\sqrt2$, and the escape radius of the model and of the algebra differ accordingly. **The factor is a normalisation and not a phenomenon**, but it must be tracked, because a radius of $2$ in the model is a radius of $\sqrt2$ in the algebra.

## The Invariants Along the Orbit

**Proposition (determinant and trace).** Along the orbit,

$$
\det\Phi(\tilde Q_n)=N(\tilde Q_n), \qquad \operatorname{tr}\Phi(\tilde Q_n)=2(Q_n)_0 ,
$$

and for the parameter zero, $N(\tilde Q_n)=N(\tilde Q)^{2^n}$.

**Proof.** $\det\Phi=N$ and $\operatorname{tr}\Phi=2Q_0$ are the trace-and-determinant proposition of the matrix-representation article, applied to the iterate. For a central zero parameter $\Phi(\tilde Q_n)=\Phi(\tilde Q)^{2^n}$ and the determinant is multiplicative.

**Theorem (the spectrum and the central parameter).** The spectrum of $\Phi(\tilde Q_n)$ is $\{q_n(\lambda_1),q_n(\lambda_2)\}$ for the spectrum $\{\lambda_1,\lambda_2\}$ of $\Phi(\tilde Q)$, where $q_n$ are the iterates of $\zeta\mapsto\zeta^2+C$ when $\tilde C=Ce_0$; in particular the trace and the determinant of the iterate are the elementary symmetric functions of the two transported eigenvalues.

**Proof.** The functional calculus of the polynomial $p_n$ on a two-by-two matrix and the elementary symmetric functions of the spectrum. This is the eigenvalue reduction of *The Biquaternion Quadratic Map and Its Julia Sets*, here read as a statement of the model.

## The Two-Variable Reading

The model turns the biquaternion dynamics into the iteration of a polynomial map of $\mathbb{C}^4$ with the special form above, and the general theory of such maps is the pluripotential and the Fatou theory of several variables.

**Remark (what the two-variable theory gives and what it needs).** For a polynomial map of $\mathbb{C}^4$ whose leading homogeneous part is proper, there is a Green's function, an equilibrium measure, a filled Julia set and a Fatou theory, and the equilibrium measure is the harmonic measure of the fractal (*Several Complex Variables*, *Plurisubharmonic Functions*, and the pluripotential article of the category). **The leading part of the matrix family is $M\mapsto M^2$, whose fibre over $0$ is the square-zero cone of the traceless singular matrices and is not finite**; the several-variable theory therefore applies to the restriction to the regular part and not to the whole map. This is the model form of the obstruction of *The Zero Divisors and the Singular Julia Sets*.

**Remark (the rank-one cone in the model).** In the model the zero divisors are the non-zero singular matrices; the determinant criterion, the rank-one elements and the outer product are *Biquaternion 2×2 Matrix Element Representation*, and the critical set is the union of the singular matrices with the traceless ones. **The two components of the critical set are the two classical degenerations of a two-by-two matrix, singular and traceless**, and this is the cleanest statement of the critical set in the whole category.

## The Warning: Elements and Operators

The isomorphism is an isomorphism of algebras, and an algebra isomorphism carries multiplication and its derived operations; it does not carry every operator that can be built on the underlying space.

**Proposition (the element and the operator are different objects).** Let $L_{\tilde Q}:\mathbb{B}\to\mathbb{B}$ be left multiplication, $L_{\tilde Q}(\tilde P)=\tilde Q\tilde P$. Then $L_{\tilde Q}$ is a complex-linear endomorphism of the four-dimensional space, represented by a $4\times4$ matrix in any basis, while $\Phi(\tilde Q)$ is the two-by-two matrix corresponding to the element $\tilde Q$. The two are different objects: $\Phi(L_{\tilde Q})$ is not defined, and the eigenvalues of the $4\times4$ matrix $L_{\tilde Q}$ are $\{Q_0+iB,Q_0+iB,Q_0-iB,Q_0-iB\}$ with $B=\sqrt{\sum_kQ_k^2}$, the eigenvalues of $\Phi(\tilde Q)$ each counted twice.

**Proof.** Under the identification $\mathbb{B}=\mathbb{C}^4$ the operator $L_{\tilde Q}$ is the left regular representation, and its characteristic polynomial is the square of that of $\Phi(\tilde Q)$ because $\mathbb{B}\cong M_2(\mathbb{C})$ is the direct sum of two copies of the simple module on which $M=\Phi(\tilde Q)$ acts by $M$ (*Modules over the General Plain Algebra of Biquaternions*). The eigenvalues of $M$ are $Q_0\pm iB$ by the characteristic polynomial of the matrix-representation article.

**Corollary (where the operator enters the dynamics).** The derivative of the quadratic family is the sum of two operators on the space and not an element,

$$
dF_{\tilde C}\big|_{\tilde Q}(\tilde P)=\tilde Q\tilde P+\tilde P\tilde Q=L_{\tilde Q}(\tilde P)+R_{\tilde Q}(\tilde P),
$$

which is why the critical set is read from the pair of eigenvalues of $\Phi(\tilde Q)$ — $\det dF=4N(\tilde Q)(2Q_0)^2$ — and not from the matrix of the element alone.

**Proof.** The product rule; the determinant computation is the critical-set proposition of *The Biquaternion Quadratic Map and Its Julia Sets*.

**Remark (the moral of the warning).** A statement about the element $\tilde Q$ transports along $\Phi$ and can be read from the two-by-two matrix; a statement about the operator $\tilde Q\mapsto\tilde Q\tilde P$ or about a product of the space does not, and must be proven in the algebra. **The model is a model of the elements and of their multiplication, and every use of the model must name which of the two objects is meant.** The four general products of the space are the standard trap: they are not carried by $\Phi$, which is the isomorphism for one product only.

## Summary

The matrix model conjugates the biquaternion quadratic family to the polynomial map $M\mapsto M^2+N$ of the four complex entries of a two-by-two matrix, carries the filled Julia set and the Julia set bijectively to their matrix counterparts, and compares the two norms by the single factor $\sqrt2$: the Frobenius norm of the matrix is $\sqrt2$ times the Euclidean norm of the element, and the submultiplicativity constant is $\sqrt2$. The determinant and the trace of the iterate are the biquaternion norm and twice the scalar part, the spectrum of the iterate is the image of the spectrum under the scalar quadratic map for a central parameter, and the two-variable complex theory applies to the model on the regular part, its obstruction being the square-zero cone that its leading part is not proper over. The article closes with the warning that the isomorphism concerns the elements and not the operators built on them: left multiplication is a $4\times4$ operator with the eigenvalues of the element doubled, and the derivative of the family is the sum of two such operators, which is where the operator enters and the reason the critical set is the union of the singular matrices and the traceless ones.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | the matrix realization |
| $M=\Phi(\tilde Q)$, $N=\Phi(\tilde C)$ | the matrix of the point and of the parameter |
| $\|\cdot\|_F$, $\|\cdot\|_2$ | the Frobenius and operator norms |
| $\|\cdot\|_E$ | the Euclidean norm on $\mathbb{B}$ |
| $p_n$ | the iterated polynomial, $p_{n+1}=p_n^2+N$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication operators |
| $dF_{\tilde C}=\tilde Q\tilde P+\tilde P\tilde Q$ | the derivative, the sum of two operators |
| $\det dF=4N(\tilde Q)(2Q_0)^2$ | the determinant of the derivative |

## Further Reading

- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`) and *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the isomorphism, the trace and the determinant, the spectrum and the conjugations in matrix form.
- *The Biquaternion Quadratic Map and Its Julia Sets* (`articles_maths/the-biquaternion-quadratic-map-and-its-julia-sets.md`), for the family, the eigenvalue reduction and the critical set.
- *Modules over the General Plain Algebra of Biquaternions* (`articles_maths/modules-over-the-general-plain-algebra-of-biquaternions.md`), for the regular representation and the doubling of the spectrum.
- *The Zero Divisors and the Singular Julia Sets* (`articles_maths/the-zero-divisors-and-the-singular-julia-sets.md`), for the cone that the leading part of the matrix family is not proper over.
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm $N$ and the Euclidean norm compared here.
