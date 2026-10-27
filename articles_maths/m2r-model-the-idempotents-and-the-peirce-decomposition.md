# __$M_2(\mathbb{R})$ Model : The Idempotents and the Peirce Decomposition__

## Introduction

The idempotents of the split-quaternion algebra are the elements $\tilde\pi$ with $\tilde\pi^2=\tilde\pi$, and under the defining isomorphism they become the idempotent $2\times2$ real matrices. The matrix side is the classical theory of projections: an idempotent of rank one is the projection onto a line along a complementary line, and the general idempotent is a projection of rank zero, one or two.

This article reads the idempotents of the algebra in the model, proves that the non-trivial ones are exactly the rank-one projections, and computes the Peirce decomposition of the algebra by the standard idempotent $\tilde\pi_+=\tfrac12(1+\vec e_y)$. The four Peirce corners are the four matrix units in the basis adapted to the splitting of the plane by the projection. The algebra is simple, so a non-trivial idempotent is not central: a central idempotent would generate a proper two-sided ideal. The decomposition is therefore a decomposition of vector spaces, not of algebras.

The idempotents themselves are *Split-Quaternion Idempotents and Projections*; the Peirce decomposition is *Split-Quaternion Ideals and Peirce Decomposition*; the rank-one matrices and the null cone are *$M_2(\mathbb{R})$ Model : Rank-One Matrices and the Null Cone*; and the subspaces are the companion article *$M_2(\mathbb{R})$ Model : The Subspaces as Matrix Conditions*.

## The Halving Map

**Definition.** A **root of one** is an element $\tilde\xi$ with $\tilde\xi^2=1$. The **halving map** sends a root of one to

$$
\tilde\pi = \tfrac12(1+\tilde\xi),
$$

with inverse $\tilde\xi = 2\tilde\pi-1$.

**Proposition (roots and idempotents).** The halving map is a bijection from the roots of one onto the idempotents, and it exchanges the pair $\tilde\xi\leftrightarrow-\tilde\xi$ with the complementary pair $\tilde\pi\leftrightarrow1-\tilde\pi$.

**Proof.** If $\tilde\xi^2=1$ then $\tilde\pi^2=\tfrac14(1+2\tilde\xi+\tilde\xi^2)=\tfrac12(1+\tilde\xi)=\tilde\pi$. Conversely if $\tilde\pi^2=\tilde\pi$ then $(2\tilde\pi-1)^2=4\tilde\pi^2-4\tilde\pi+1=1$. The complement statement is immediate from the definition.

**Proposition (the roots of one).** An element $\tilde\xi$ satisfies $\tilde\xi^2=1$ exactly when either it is scalar and equals $\pm1$, or it is pure with $N(\tilde\xi)=-1$:

$$
\tilde\xi = \pm e_t \quad\text{or}\quad \tilde\xi\in V,\; N(\tilde\xi)=-1.
$$

**Proof.** Write $\tilde\xi = s+\vec v$ with $s$ scalar and $\vec v$ pure. Then $\tilde\xi^2=s^2-N(\vec v)+2s\vec v$, since $\vec v^2=-N(\vec v)e_t$. The equation $\tilde\xi^2=1$ gives $2s\vec v=0$ and $s^2-N(\vec v)=1$. If $s\neq0$ then $\vec v=0$ and $s=\pm1$. If $s=0$ then $N(\vec v)=-1$.

**Corollary (the idempotents).** The idempotents of the algebra are $0$, $1$, and the elements

$$
\tilde\pi = \tfrac12(1+\vec v), \qquad \vec v\in V,\; N(\vec v)=-1.
$$

The non-trivial idempotents form a connected two-dimensional one-sheeted hyperboloid in $V$.

**Proof.** The two scalar roots give $0$ and $1$. The pure roots give the displayed family. In $V$ the equation $N(\vec v)=-1$ reads $v_x^2-v_y^2-v_z^2=-1$, that is $v_y^2+v_z^2=v_x^2+1$, the one-sheeted hyperboloid, which is connected.

**Example.** The element $\vec v=\vec e_y$ has $N(\vec e_y)=-1$, and the halving map gives the two idempotents of the algebra

$$
\tilde\pi_+ = \tfrac12(1+\vec e_y), \qquad \tilde\pi_- = \tfrac12(1-\vec e_y),
$$

with $\tilde\pi_++\tilde\pi_-=1$ and $\tilde\pi_+\tilde\pi_-=0$. The element $\vec v=\vec e_x$ has $N(\vec e_x)=+1$ and gives no idempotent, since $\tfrac12(1+\vec e_x)$ is not idempotent; indeed $\vec e_x^2=-1$ is a root of $-1$, not of $1$.

## The Idempotents as Rank-One Projections

**Theorem (the model of the idempotents).** Under $\mathsf{M}_2$, the non-trivial idempotents become exactly the rank-one projections:

$$
\mathsf{M}_2(\tilde\pi) = \tfrac12\begin{pmatrix} 1-v_z & v_y-v_x \\ v_x+v_y & 1+v_z \end{pmatrix}, \qquad N(\vec v)=-1,
$$

and those matrices satisfy $P^2=P$, $\operatorname{tr}P=1$ and $\det P=0$. Conversely every $2\times2$ matrix with these three properties is of that form.

**Proof.** The displayed matrix is $\tfrac12(I+\mathsf{M}_2(\vec v))$, and $\mathsf{M}_2(\vec v)$ has trace zero by the dictionary. Hence the trace of $P$ is one and its determinant is

$$
\det P = \tfrac14\bigl(1-v_z^2-(v_y-v_x)(v_x+v_y)\bigr) = \tfrac14\bigl(1-v_z^2-v_y^2+v_x^2\bigr) = \tfrac14\bigl(1+N(\vec v)\bigr)=0.
$$

The square is $P$ by the proposition on the halving map. Conversely, a matrix with $P^2=P$, $\operatorname{tr}P=1$ and $\det P=0$ has eigenvalues $1$ and $0$, so it has rank one and is a projection; its traceless part $\vec v=2P-I$ is pure with $\vec v^2=1$, that is $N(\vec v)=-1$.

**Corollary (the two standard idempotents).** The idempotents $\tilde\pi_\pm=\tfrac12(1\pm\vec e_y)$ become

$$
\mathsf{M}_2(\tilde\pi_+) = \tfrac12\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad
\mathsf{M}_2(\tilde\pi_-) = \tfrac12\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}.
$$

**Proof.** The image of $\vec e_y$ is $K=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, and the two formulas are $\tfrac12(I\pm K)$.

The two matrices are the projections onto the lines $L_+=\operatorname{span}(1,1)$ and $L_-=\operatorname{span}(1,-1)$. They are orthogonal as idempotents, $\mathsf{M}_2(\tilde\pi_+)\mathsf{M}_2(\tilde\pi_-)=0$, and they sum to the identity. In the algebra this is the pair $\tilde\pi_+\tilde\pi_-=0$ and $\tilde\pi_++\tilde\pi_-=1$, and it is the Peirce pair of the next section.

## The Peirce Decomposition

**Definition.** The **Peirce decomposition** of the algebra by the idempotent $\tilde\pi_+$ is the direct sum of the four corners

$$
A = A_{++}\oplus A_{+-}\oplus A_{-+}\oplus A_{--}, \qquad A_{\epsilon\delta}=\tilde\pi_\epsilon A\tilde\pi_\delta,
$$

with $\tilde\pi_-=1-\tilde\pi_+$.

**Theorem (the four corners).** With $L_+=\operatorname{span}(1,1)$ and $L_-=\operatorname{span}(1,-1)$, the four corners are one-dimensional and are spanned by the following elements:

| corner | basis element | matrix | as a map |
|---|---|---|---|
| $A_{++}$ | $\tilde\pi_+$ | $\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$ | projection onto $L_+$ along $L_-$ |
| $A_{--}$ | $\tilde\pi_-$ | $\tfrac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ | projection onto $L_-$ along $L_+$ |
| $A_{+-}$ | $\tilde\pi_+E_{11}\tilde\pi_-=\tfrac14(\vec e_x-\vec e_z)$ | $\tfrac14\begin{pmatrix}1&-1\\1&-1\end{pmatrix}$ | maps $L_-$ onto $L_+$, kills $L_+$ |
| $A_{-+}$ | $\tilde\pi_-E_{11}\tilde\pi_+=-\tfrac14(\vec e_x+\vec e_z)$ | $\tfrac14\begin{pmatrix}1&1\\-1&-1\end{pmatrix}$ | maps $L_+$ onto $L_-$, kills $L_-$ |

**Proof.** In the basis of $L_+$ and $L_-$ the two idempotents are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$, so the four corners are the four matrix units and each is one-dimensional. The off-diagonal basis elements are computed from the dictionary, and they are nilpotent: the square of a matrix unit $E_{12}$ or $E_{21}$ is zero.

**Proposition (the Peirce identities).** The corners multiply by the rule

$$
A_{\epsilon\delta}A_{\delta'\eta}\subseteq\delta_{\delta\delta'}A_{\epsilon\eta},
$$

and the only non-zero products between distinct off-diagonal corners are

$$
\bigl(\tilde\pi_+E_{11}\tilde\pi_-\bigr)\bigl(\tilde\pi_-E_{11}\tilde\pi_+\bigr)=\tfrac14\tilde\pi_+, \qquad
\bigl(\tilde\pi_-E_{11}\tilde\pi_+\bigr)\bigl(\tilde\pi_+E_{11}\tilde\pi_-\bigr)=\tfrac14\tilde\pi_-.
$$

**Proof.** The inclusion is the definition of the corners and the orthogonality $\tilde\pi_\epsilon\tilde\pi_\delta=\delta_{\epsilon\delta}\tilde\pi_\epsilon$. The two products are computed in the model, where the corner basis elements are $E_{12}$ and $E_{21}$: $E_{12}E_{21}=E_{11}$ and $E_{21}E_{12}=E_{22}$.

**Theorem (the diagonal and the off-diagonal parts).** The diagonal part $D=A_{++}\oplus A_{--}$ is the split-complex plane $\operatorname{span}\{1,\vec e_y\}$, and the off-diagonal part $N=A_{+-}\oplus A_{-+}$ is the plane $\operatorname{span}\{\vec e_x,\vec e_z\}$. Their squares satisfy

$$
D^2\subseteq D, \qquad D N\subseteq N, \qquad N D\subseteq N, \qquad N^2=D.
$$

**Proof.** The diagonal part is spanned by $\tilde\pi_+$ and $\tilde\pi_-$, which span the same plane as $1$ and $\vec e_y$. The off-diagonal part is spanned by $\tfrac14(\vec e_x-\vec e_z)$ and $\tfrac14(\vec e_x+\vec e_z)$, which span the same plane as $\vec e_x$ and $\vec e_z$. The first three inclusions are the Peirce rule. For the fourth, the products of the basis elements give $\vec e_x^2=-1$, $\vec e_x\vec e_z=-\vec e_y$ and $\vec e_z\vec e_x=\vec e_y$, all in $D$, and the two planes have the same dimension.

**Remark (the matrix reading).** In the basis adapted to the splitting of the plane by $\tilde\pi_+$, the algebra is the full matrix algebra $M_2(\mathbb{R})$ with its four matrix units, and the Peirce decomposition is the block decomposition

$$
\begin{pmatrix} * & * \\ * & * \end{pmatrix} = \begin{pmatrix} * & 0 \\ 0 & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & * \\ 0 & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & 0 \\ * & 0 \end{pmatrix} \oplus \begin{pmatrix} 0 & 0 \\ 0 & * \end{pmatrix}.
$$

The decomposition is a decomposition into four lines because the idempotent has rank one; in the basis adapted to it, no computation is needed to see the corners.

## Non-Centrality and the Contrast with the Reduced Biquaternions

**Proposition (the idempotent is not central).** The idempotent $\tilde\pi_+$ does not commute with $\vec e_x$:

$$
\tilde\pi_+\vec e_x = \tfrac12(\vec e_x-\vec e_z), \qquad \vec e_x\tilde\pi_+ = \tfrac12(\vec e_x+\vec e_z).
$$

**Proof.** Expand $\tilde\pi_+\vec e_x=\tfrac12(\vec e_x+\vec e_y\vec e_x)$. The product $\vec e_y\vec e_x=-\vec e_z$ gives the first identity, and $\vec e_x\vec e_y=\vec e_z$ gives the second.

**Corollary (no algebra decomposition).** The algebra is not the product of the two corners, and the Peirce decomposition is not a decomposition of algebras.

**Proof.** If the algebra were the product $A_{++}\times A_{--}$ then the two factors would be two-sided ideals and their identities $\tilde\pi_\pm$ would be central. They are not central by the proposition.

This is the structural difference from the reduced biquaternions. There the idempotents $\tfrac12(1\pm\vec e_y)$ are central, the algebra is the product $\mathbb{C}\times\mathbb{C}$, and the Peirce decomposition is an algebra decomposition (*Introduction to the Algebra of the Reduced Biquaternions*). Here the same formulas give a decomposition of vector spaces only, because the algebra is simple (*Split-Quaternion Algebra*, §*The Centre and Simplicity*).

## Summary

The idempotents of the split-quaternion algebra are the two scalars $0$ and $1$ together with the elements $\tfrac12(1+\vec v)$ over the pure vectors of norm $-1$. That family is a connected two-dimensional one-sheeted hyperboloid, and under the model it is exactly the family of rank-one projections: matrices with trace one, determinant zero and square equal to themselves.

The standard idempotents $\tfrac12(1\pm\vec e_y)$ become the projections onto the lines spanned by $(1,1)$ and $(1,-1)$. The Peirce decomposition by $\tfrac12(1+\vec e_y)$ has four one-dimensional corners, the four matrix units in the basis adapted to those lines. The diagonal part is the split-complex plane $\operatorname{span}\{1,\vec e_y\}$, the off-diagonal part is the plane $\operatorname{span}\{\vec e_x,\vec e_z\}$, and the off-diagonal part squares onto the diagonal part. The idempotent is not central, so the decomposition is not a product of algebras, in contrast with the reduced biquaternions.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\tilde\pi_\pm$ | the idempotents $\tfrac12(1\pm\vec e_y)$ | *Split-Quaternion Idempotents and Projections* |
| $\tilde\xi$ | a root of one, $\tilde\xi^2=1$ | this article |
| $A_{\epsilon\delta}$ | the Peirce corner $\tilde\pi_\epsilon A\tilde\pi_\delta$ | this article |
| $D$ | the diagonal part, $\operatorname{span}\{1,\vec e_y\}$ | this article |
| $N$ | the off-diagonal part, $\operatorname{span}\{\vec e_x,\vec e_z\}$ | this article |
| $L_\pm$ | the lines $\operatorname{span}(1,\pm1)$ | this article |
| $E_{ij}$ | the matrix units of $M_2(\mathbb{R})$ | *Split-Quaternion Matrix Element Representations* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition and the classification of idempotents.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the simplicity of a full matrix algebra and the centrality of its identity.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the idempotents of $\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$.
