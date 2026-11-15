# __The Peirce Decomposition of $\operatorname{Sym}_2$ as a Jordan Algebra__

## Introduction

**The symmetric half with the Jordan product $x\circ y=\tfrac12(xy+yx)$ splits at a symmetric idempotent into three Peirce spaces $V_{2}$, $V_{1}$, $V_{0}$ of dimension one each, and the Jordan product obeys the rule $V_{i}\circ V_{j}\subseteq V_{i+j}$.**

The article defines the Jordan product on the symmetric half, identifies the Jordan multiplication by an idempotent with a projection whose eigenvalues are $1$, $\tfrac12$, $0$, computes the three dimensions, proves the Peirce rules, checks the Jordan identity, and compares the three-piece decomposition with the four-piece associative one. It assumes *The Jordan Algebra $\operatorname{Sym}_2$*, *The Peirce Decomposition in Two Dimensions* and *The Peirce Basis and the Corners at $n=2$*.

It defers the Hermitian idempotents and their sphere to *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*, and the corner recursion to *The Peirce Decomposition and the Corner Recursion of $M_2(\mathbb{C})$*.

## The Jordan Product on the Symmetric Half

**Definition.** The **Jordan product** of two matrices is $x\circ y=\tfrac12(xy+yx)$.

**Proposition.** The symmetric half is closed under the Jordan product, and the product is commutative but not associative.

**Proof.** The transpose of $\tfrac12(xy+yx)$ is $\tfrac12(y^{\mathsf T}x^{\mathsf T}+x^{\mathsf T}y^{\mathsf T})=\tfrac12(yx+xy)$ for symmetric $x$ and $y$, so the product stays symmetric; commutativity is the symmetry of the display; and the failure of associativity is the failure of the associative product in the symmetrised form.

**Corollary.** The symmetrised product of two symmetric matrices is $\tfrac12(xy+yx)$, which differs from $xy$ exactly when the two factors do not commute.

**Proof.** For commuting symmetric matrices $xy$ is symmetric and the symmetrisation is the product itself; otherwise $xy$ is not symmetric and the symmetrisation is a different matrix.

## The Multiplication by an Idempotent

**Definition.** The **Jordan multiplication** by an element $a$ is the operator $L_{a}(x)=a\circ x$.

**Proposition.** For a symmetric idempotent $e$ the operator $L_{e}$ is diagonalisable, with the eigenvalues $1$, $\tfrac12$ and $0$.

**Proof.** At the standard frame $e=E_{11}$ the three elements $e$, $w=E_{12}+E_{21}$ and $f=E_{22}$ form a basis of the symmetric half, and $e\circ e=e$, $e\circ w=\tfrac12 w$, $e\circ f=0$. A linear operator is determined by its values on a basis, so the matrix of $L_{e}$ in this basis is $\operatorname{diag}(1,\tfrac12,0)$.

**Corollary.** The symmetric half splits as the direct sum of the three eigenspaces $V_{2}$, $V_{1}$, $V_{0}$ of $L_{e}$, of dimension one each at the standard frame.

**Proof.** The operator is diagonal in the basis displayed, with three distinct eigenvalues, so the three eigenspaces are the three lines of the basis.

**Definition.** The **Peirce spaces** of the Jordan algebra are

$$
V_{2}=\{x: e\circ x=x\},\qquad V_{1}=\Bigl\{x: e\circ x=\tfrac12 x\Bigr\},\qquad V_{0}=\{x: e\circ x=0\}.
$$

**Corollary.** At the standard frame $V_{2}$ is the line of $e$, $V_{0}$ is the line of $f$, and $V_{1}$ is the line of $w=E_{12}+E_{21}$.

**Proof.** The three lines are the eigenspaces computed above, with the eigenvalues $1$, $0$ and $\tfrac12$.

**Corollary.** The Jordan splitting merges the two mixed corners: $V_{2}=A_{11}$, $V_{0}=A_{00}$, and $V_{1}$ is the symmetrisation of $A_{12}$ and $A_{21}$.

**Proof.** The diagonal corners are the eigenspaces of the eigenvalue $1$ and $0$, and the mixed corners are both mapped by the symmetrisation onto the line of $w$.

## The Dimensions

**Theorem.** For a symmetric rank-one idempotent the three Peirce spaces have dimension one each, and the dimensions sum to three, the dimension of the symmetric half.

**Proof.** At $e=E_{11}$ the symmetric half has the basis $E_{11}$, $E_{12}+E_{21}$, $E_{22}$; the first is $V_{2}$, the third is $V_{0}$, and the middle one satisfies $e\circ(E_{12}+E_{21})=\tfrac12(E_{12}+E_{21})$, so it spans $V_{1}$.

**Corollary.** The symmetric idempotent of rank one gives the finest Jordan splitting, and the antisymmetric part does not appear at all.

**Proof.** The symmetric half has dimension three and the three spaces have dimension one each, so no space can be further split; and the antisymmetric line is not contained in the symmetric half.

**Corollary.** At the two trivial idempotents $0$ and $I$ the splitting degenerates to the whole space in one piece.

**Proof.** $L_{0}$ is zero and $L_{I}$ is the identity on the symmetric half, so the only nonzero eigenspace is $V_{0}$ in the first case and $V_{2}$ in the second.

## The Peirce Rules

**Theorem.** The Jordan Peirce spaces satisfy

$$
V_{2}\circ V_{2}\subseteq V_{2},\quad V_{2}\circ V_{1}\subseteq V_{1},\quad V_{2}\circ V_{0}=0,\quad V_{1}\circ V_{1}\subseteq V_{2}\oplus V_{0},\quad V_{1}\circ V_{0}\subseteq V_{1},\quad V_{0}\circ V_{0}\subseteq V_{0}.
$$

**Proof.** Read the six products in the basis $e$, $w$, $f$ of the standard frame, where $e\circ e=e$, $e\circ w=\tfrac12 w$, $e\circ f=0$, $w\circ w=I=e+f$, $w\circ f=\tfrac12 w$ and $f\circ f=f$. Each product lands in the space named by the two eigenvalues, and the middle product $w\circ w$ is the only one that needs both diagonal pieces.

**Corollary.** The single departure from the sum rule is $V_{1}\circ V_{1}\subseteq V_{2}\oplus V_{0}$, whose second summand is the price of the identity element.

**Proof.** At the standard frame the product of $w$ with itself is the identity, half of which is $e$ in $V_{2}$ and half $f$ in $V_{0}$.

**Corollary.** $V_{2}\circ V_{0}=0$ and $V_{1}\circ V_{1}=\mathbb{C}I$, so the product of the two diagonal eigenspaces vanishes and the square of the middle space is the line of the identity.

**Proof.** The first is the vanishing of $e\circ f$, and the second is $w\circ w=I$ with $w$ spanning $V_{1}$.

## The Jordan Identity

**Proposition.** The product satisfies the Jordan identity

$$
(x\circ y)\circ(x\circ x)=x\circ\bigl(y\circ(x\circ x)\bigr)
$$

for all symmetric $x$ and $y$.

**Proof.** The identity is the linearisation of the associativity of the powers in the symmetrised product, and it is checked directly on the three-dimensional space, where every product is a polynomial identity in the entries.

**Corollary.** The symmetric half with the Jordan product is a Jordan algebra of dimension three, and it is special: it comes from the associative algebra by symmetrisation.

**Proof.** The product is the symmetrisation of the associative product of the ambient algebra, so the Jordan algebra is special by construction; and its dimension is three.

**Corollary.** The trace form restricts to a positive definite form on the symmetric half, which is the trace form of the Jordan algebra.

**Proof.** The restriction of $\operatorname{tr}(xy)$ to the symmetric half is positive definite with the eigenvalues $1,1,2$ in the Pauli basis, as computed in *The Two Halves as Orthogonal Complements at $n=2$*.

## The Comparison with the Associative Splitting

**Proposition.** The associative Peirce decomposition has four pieces and the Jordan decomposition has three: the two mixed corners merge.

**Proof.** The associative decomposition separates $A_{12}$ from $A_{21}$ by the right multiplication, which distinguishes left from right; the Jordan product is commutative and cannot tell the two apart, so their symmetrisation is a single space.

**Corollary.** The dimension count is $1+1+1+1=4$ for the associative algebra and $1+1+1=3$ for the symmetric half, and the difference is the antisymmetric line.

**Proof.** The two mixed corners contribute two dimensions in the algebra and one in the symmetric half, and the antisymmetric line accounts for the remaining difference.

**Corollary.** The Jordan Peirce space $V_{1}$ is the graph of the identity map between the two mixed corners under the symmetrisation.

**Proof.** An element of $V_{1}$ is the symmetrisation of an element of $A_{12}$ and an element of $A_{21}$, and at the standard frame the representative is $E_{12}+E_{21}$.

## Summary

The symmetric half with the Jordan product $x\circ y=\tfrac12(xy+yx)$ is a Jordan algebra of dimension three. A symmetric rank-one idempotent $e$ gives the operator $L_{e}$ with the eigenvalues $1$, $\tfrac12$, $0$, and the three Peirce spaces $V_{2}$, $V_{1}$, $V_{0}$ of dimension one each, spanned at the standard frame by $E_{11}$, $E_{12}+E_{21}$, $E_{22}$.

The Peirce rules hold, with $V_{1}\circ V_{1}\subseteq V_{2}\oplus V_{0}$ the single departure from the sum rule and $V_{2}\circ V_{0}=0$, the Jordan identity holds, and the Jordan splitting is the associative four-piece splitting with the two mixed corners merged, since the commutative product cannot separate left from right.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x\circ y$ | $\tfrac12(xy+yx)$, the Jordan product |
| $L_{a}$ | Jordan multiplication by $a$ |
| $V_{2},V_{1},V_{0}$ | the three Jordan Peirce spaces |
| $e$ | a symmetric rank-one idempotent |
| $w$ | $E_{12}+E_{21}$, the off-diagonal element |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Peirce decomposition of a Jordan algebra and the rules $V_{i}\circ V_{j}\subseteq V_{i+j}$.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (AMS, 1968), for the Jordan identity and the special Jordan algebras.
- [The Jordan Algebra $\operatorname{Sym}_2$](the-jordan-algebra-sym-2.html), for the product and its identities in the associative setting.
- [The Peirce Decomposition in Two Dimensions](the-peirce-decomposition-in-two-dimensions.html), for the associative decomposition that the Jordan one merges.
- [The Two Halves as Orthogonal Complements at $n=2$](the-two-halves-as-orthogonal-complements-at-n-2.html), for the trace form restricted to the symmetric half.
