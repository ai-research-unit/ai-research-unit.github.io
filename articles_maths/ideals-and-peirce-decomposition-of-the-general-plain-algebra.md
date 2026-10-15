# __Ideals and Peirce Decomposition of the General Plain Algebra__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$, as established in the article on biquaternion algebra. This article studies the ideal structure of $\mathbb{B}$ and the decomposition of $\mathbb{B}$ relative to a family of idempotents.

Two facts organize the discussion. The algebra $\mathbb{B}$ is **simple**: its only two-sided ideals are $0$ and $\mathbb{B}$. Its ideal theory is therefore a theory of one-sided ideals: the main results are the classification of the left ideals — $0$, the minimal ones, and $\mathbb{B}$ — and the Peirce decomposition into four one-dimensional corners. The decomposition is attached to a root of $+1$: a root $\tilde\Xi$ carries the two orthogonal idempotents $\tilde\Pi_+=\tfrac12(e_0+\tilde\Xi)$ and $\tilde\Pi_-=\tfrac12(e_0-\tilde\Xi)$, the pair gives the four corners, and so there are **as many Peirce decompositions of $\mathbb{B}$ as roots of $+1$**, a root and its opposite giving the same one (§*The Peirce Decomposition*). The Peirce decomposition is developed in detail below: it is read in coordinates, and the coordinates turn out to be the four entries of the matrix element representation of the algebra; it is a grading by the signs of the corners; the three conjugations of the algebra act on it; one idempotent, equivalently one root, already forces it, the complement being determined; and it is rigid, in the sense that all systems of matrix units that realise it are conjugate.

Because the biquaternions carry both a complex and a real structure, every statement is tagged with the field over which it is made. The sections before the last work over $\mathbb{C}$; §*The Real Structure* discusses the $\mathbb{R}$-view, where the ideal lattice itself is unchanged but the real structure leaves further traces. The notation follows the article on biquaternion algebra: $e_0$ is the unit, $e_1, e_2, e_3$ are the quaternion units with $e_1 e_2 = e_3$, $i$ is the central scalar imaginary, and a general element is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. The definitions of the article on rings apply to the noncommutative algebra $\mathbb{B}$, where "left" and "right" must be distinguished.

## Ideals in an Algebra

Let $A$ be an associative unital algebra over a field $k$. An additive subgroup $I \subseteq A$ is a **left ideal** if $A I \subseteq I$, a **right ideal** if $I A \subseteq I$, and a **two-sided ideal** if it is both. The distinction matters only when $A$ is noncommutative; for $\mathbb{B}$ the three notions genuinely differ. The ideals $0$ and $A$ are called trivial.

A base-field remark will be used repeatedly. If $A I \subseteq I$, then $I$ is automatically a $k$-subspace, since $\lambda \tilde Q = (\lambda 1) \tilde Q \in I$ for $\lambda \in k$, $\tilde Q \in I$, as $\lambda 1 \in A$. So the left ideals of a unital algebra do not depend on which field of scalars inside the centre is used to view it; in particular the ideal lattice of $\mathbb{B}$ is the same in the $\mathbb{C}$-view and the $\mathbb{R}$-view (§*The Real Structure*).

For a two-sided ideal $I$, the **quotient algebra** $A/I$ is the set of cosets with the induced operations, well defined precisely because $I$ absorbs multiplication on both sides. Kernels of algebra homomorphisms are two-sided ideals, and the first isomorphism theorem gives $A/\ker\varphi \cong \operatorname{im}\varphi$. For a left ideal only, $A/I$ is still a left $A$-module but not in general an algebra. Thus the left ideals govern module theory and the two-sided ideals govern quotient algebras.

## The Two-Sided Ideals: Simplicity of $\mathbb{B}$

**Theorem.** Over $\mathbb{C}$, the only two-sided ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$. Equivalently, $\mathbb{B}$ is a **simple** $\mathbb{C}$-algebra.

**Proof.** Let $I \neq 0$ be a two-sided ideal. It is a $\mathbb{C}$-subspace, because multiplication by the central element $i$ is left multiplication by an element of $\mathbb{B}$. Fix $0 \neq \tilde{Q} = \sum_\mu Q_\mu e_\mu \in I$. For every unit $\tilde B \in \mathbb{B}$ the conjugate $\tilde B\tilde{Q}\tilde B^{-1}$ lies in $I$, since $I$ is two-sided.

Average the conjugates over the finite group $\{\pm e_0, \pm e_1, \pm e_2, \pm e_3\}$. For $\mu = 1, 2, 3$, conjugation by $e_\mu$ fixes $e_0$ and $e_\mu$ and reverses the other two imaginary units, while conjugation by $e_0$ is the identity; in each case $e_\mu$ and $-e_\mu$ give the same conjugate, and the sum over the four representatives $e_0, e_1, e_2, e_3$ is

$$
\tilde Q + \big(Q_0 e_0 + Q_1 e_1 - Q_2 e_2 - Q_3 e_3\big) + \big(Q_0 e_0 - Q_1 e_1 + Q_2 e_2 - Q_3 e_3\big) + \big(Q_0 e_0 - Q_1 e_1 - Q_2 e_2 + Q_3 e_3\big) = 4 Q_0 e_0,
$$

the sum over all eight is twice this, and the average is that sum divided by $8$, giving $Q_0 e_0 \in I$. If $Q_0 \neq 0$ then $e_0 = Q_0^{-1}(Q_0 e_0) \in I$ and $I = \mathbb{B}$. If $Q_0 = 0$ then $\tilde{Q}$ is nonzero and pure, so some coefficient $Q_k \neq 0$ with $k \in \{1,2,3\}$. Since $I$ is a two-sided ideal, the product $\tilde{Q} e_k$ lies in $I$, and its scalar part is $-Q_k \neq 0$; the averaging applied to $\tilde{Q} e_k$ then gives $-Q_k e_0 \in I$, so $e_0 \in I$ and again $I = \mathbb{B}$.

Consequences over $\mathbb{C}$:

- The only quotient algebras of $\mathbb{B}$ are $\mathbb{B}$ and $0$.
- Every nonzero element generates $\mathbb{B}$ as a two-sided ideal.
- The centre of $\mathbb{B}$ is the scalar copy of $\mathbb{C}$, so $\mathbb{B}$ is a **central simple** $\mathbb{C}$-algebra; in particular it is not a product $A_1 \times A_2$ of nonzero algebras, since each factor would give a nontrivial two-sided ideal.
- The many one-sided ideals of §*Minimal Left and Right Ideals* and §*The Lattice of Left Ideals* are all non-two-sided, so they do not contradict simplicity.

## Artinian, Semisimple, and Length Two

A nonzero module is **simple** if it has no submodules other than $0$ and itself. A **composition series** is a finite strictly increasing chain $0 = M_0 \subset M_1 \subset \cdots \subset M_r = M$ with simple successive quotients $M_i/M_{i-1}$; the number $r$ is the **length** of $M$. A ring is **left artinian** if every descending chain of left ideals stabilizes, and **semisimple** if its left regular module is a direct sum of simple modules.

Over $\mathbb{C}$, every descending chain of left ideals of $\mathbb{B}$ is a descending chain of $\mathbb{C}$-subspaces, so it stabilizes; thus $\mathbb{B}$ is artinian. By Wedderburn–Artin, a unital ring is semisimple if and only if it is artinian with zero Jacobson radical, and every simple artinian ring is semisimple. Hence $\mathbb{B}$ is **semisimple**, and every left ideal is a direct sum of minimal left ideals.

All simple left $\mathbb{B}$-modules are isomorphic, since a simple artinian ring has a unique simple module up to isomorphism. With the idempotents $\tilde\Pi_+, \tilde\Pi_-$ of §*Idempotents and Orthogonal Idempotents*, the algebra as a left module over itself reads $\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_-$, with $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ both minimal left ideals. Hence $0 \subset \mathbb{B}\tilde\Pi_+ \subset \mathbb{B}$ is a composition series, and the **length of $\mathbb{B}$ as a left module over itself is $2$**, with both factors isomorphic. The right regular module has length $2$ as well. All of this is over $\mathbb{C}$.

## Idempotents and Orthogonal Idempotents

Let $A$ be an associative unital algebra. An element $e \in A$ is an **idempotent** if $e^2 = e$, and two idempotents $e, f$ are **orthogonal** if $ef = fe = 0$. A nonzero idempotent $e$ is **primitive** if it is not a sum of two nonzero orthogonal idempotents, and for a semisimple algebra

$$
e \text{ primitive} \iff Ae \text{ is a minimal left ideal} \iff eAe \text{ is a division ring}.
$$

**The pair of a root of $+1$.** Over $\mathbb{C}$ every idempotent of this article comes from a root of $+1$. Let $\tilde\Xi$ be a root of $+1$, $\tilde\Xi^2=e_0$. Its **two idempotents** are

$$
\tilde\Pi_+=\tilde\Pi_+(\tilde\Xi)=\frac{e_0+\tilde\Xi}{2}, \qquad \tilde\Pi_-=\tilde\Pi_-(\tilde\Xi)=\frac{e_0-\tilde\Xi}{2},
$$

the subscript $+$ naming the member attached to $+1$ and the subscript $-$ the member attached to $-1$ (§*The Idempotent Convention* of *Conventions in Mathematics*). Each is idempotent by the same computation, $\tilde\Pi_+^2=\tfrac14(e_0+\tilde\Xi)^2=\tfrac14(e_0+2\tilde\Xi+e_0)=\tilde\Pi_+$ and $\tilde\Pi_-^2=\tfrac14(e_0-\tilde\Xi)^2=\tfrac14(e_0-2\tilde\Xi+e_0)=\tilde\Pi_-$; the two are orthogonal, $\tilde\Pi_+\tilde\Pi_-=\tfrac14(e_0-\tilde\Xi^2)=0=\tilde\Pi_-\tilde\Pi_+$; and they are **complete**, $\tilde\Pi_+ + \tilde\Pi_-=e_0$. The root is their difference, $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$, and the two members are the two eigenvalues of multiplication by the root,

$$
\tilde\Xi\tilde\Pi_+=\tilde\Pi_+\tilde\Xi=\tilde\Pi_+, \qquad \tilde\Xi\tilde\Pi_-=\tilde\Pi_-\tilde\Xi=-\tilde\Pi_- .
$$

The construction inverts: a nontrivial idempotent $e$ gives the root $2e-e_0$, since $(2e-e_0)^2=4e^2-4e+e_0=e_0$, and the root returns $e$ as $\tilde\Pi_+(2e-e_0)=e$. So the complete orthogonal pairs of idempotents of $\mathbb{B}$ are exactly the pairs of the roots of $+1$, and a root and its opposite give the same pair. The computation and the classification of the roots are *Square Roots of One and the Idempotents of the General Plain Algebra*, §*The Two Idempotents of a Root* and §*The Correspondence With the Roots of One*.

The **standard pair** is the pair of the root $ie_3$, for which $(ie_3)^2=i^2e_3^2=e_0$:

$$
\tilde\Pi_+=\tilde\Pi_+(ie_3)=\frac{e_0+i e_3}{2}, \qquad \tilde\Pi_-=\tilde\Pi_-(ie_3)=\frac{e_0-i e_3}{2}.
$$

The two are orthogonal, sum to $e_0$, are Hermitian, $\tilde\Pi_+^{*}=\tilde\Pi_+$ and $\tilde\Pi_-^{*}=\tilde\Pi_-$, and are primitive; they generate the off-diagonal elements of the next section.

In the matrix model the primitive idempotents are exactly the nontrivial ones. An idempotent of $M_2(\mathbb{C})$ is diagonalisable with eigenvalues in $\{0,1\}$, hence of rank $0$, $1$ or $2$: the two extremes are the trivial idempotents $0$ and $e_0$, and a rank-one idempotent is primitive, because a sum of two nonzero orthogonal idempotents would have image of dimension at least two. So the nontrivial idempotents of $\mathbb{B}$ and its primitive idempotents are the same set, and each nontrivial idempotent $e$ comes with the complementary primitive idempotent $e_0 - e$.

The classification of the idempotents of $\mathbb{B}$ — the trivial idempotents, the halving map on the roots of $+1$, the Hermitian projections and the dimension of the idempotent set — is the subject of *Square Roots of One and the Idempotents of the General Plain Algebra*.

## The Off-Diagonal Elements

The two off-diagonal corners are spanned by the elements

$$
\hat\Upsilon_1 = \frac{i e_1 - e_2}{2}, \qquad \hat\Upsilon_2 = \frac{i e_1 + e_2}{2}.
$$

Then $\{\tilde\Pi_+, \hat\Upsilon_1, \hat\Upsilon_2, \tilde\Pi_-\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$; the element $\hat\Upsilon_1$ spans the corner $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ and $\hat\Upsilon_2$ the corner $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$, and the multiplication is

$$
\tilde\Pi_+\hat\Upsilon_1 = \hat\Upsilon_1 = \hat\Upsilon_1\tilde\Pi_-, \qquad \tilde\Pi_-\hat\Upsilon_2 = \hat\Upsilon_2 = \hat\Upsilon_2\tilde\Pi_+, \qquad \hat\Upsilon_1\hat\Upsilon_2 = \tilde\Pi_+, \qquad \hat\Upsilon_2\hat\Upsilon_1 = \tilde\Pi_-,
$$

together with $\hat\Upsilon_1\tilde\Pi_+ = \tilde\Pi_-\hat\Upsilon_1 = \tilde\Pi_+\hat\Upsilon_2 = 0$, $\hat\Upsilon_2\tilde\Pi_- = 0$, and $\hat\Upsilon_1^2 = \hat\Upsilon_2^2 = 0$.

## The Peirce Decomposition

The **Peirce decomposition** is the decomposition of an algebra relative to a family of orthogonal idempotents; it is the algebraic form of a block decomposition of a matrix. In $\mathbb{B}$ the family is the pair of a root of $+1$: the nontrivial idempotents are the rank-one projectors of $M_2(\mathbb{C})$ (§*Idempotents and Orthogonal Idempotents*), so a complete orthogonal family has at most two members and the two-member case is the only one that occurs. The decomposition is therefore attached to a root of $+1$, and the roots modulo the sign change count the decompositions (§*As Many Decompositions as Roots of One*).

### One Idempotent

Let $e \in A$ be idempotent and $f = 1-e$. Every $a \in A$ expands as $a = eae + eaf + fae + faf$, giving the direct sum

$$
A = eAe \oplus eAf \oplus fAe \oplus fAf,
$$

whose summands are the **Peirce spaces**. The corner $eAe$ is a subalgebra with identity $e$; the off-diagonal corners are bimodules over the diagonal ones and carry no identity. The expansion, the directness of the four terms and the product rule below are proved in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, where the case of a **central** idempotent is also separated: for a central $e$ the off-diagonal corners vanish and the sum is a product of algebras. That special case does not arise here, since the idempotents of this article lie in a simple algebra and no nontrivial idempotent of $\mathbb{B}$ is central. In $\mathbb{B}$ the pair $(e, f)$ is the pair of the root $\tilde\Xi=e-f=2e-e_0$ of $+1$, so the decomposition written here is the one attached to that root (§*From One Idempotent to Its Complement*).

### A Complete Orthogonal Family

If $\{e_1, \dots, e_n\}$ is complete and pairwise orthogonal, the same expansion gives

$$
A = \bigoplus_{i,j=1}^{n} e_i A e_j, \qquad (e_i A e_j)(e_k A e_l) \subseteq \delta_{jk}\, e_i A e_l.
$$

Each diagonal corner $e_i A e_i$ is an algebra with identity $e_i$, and each off-diagonal piece is a bimodule over the corresponding corners.

**The mixed spaces are square-zero subalgebras.** For the mixed space $eAf$ and $a, a' \in A$ one has $(eaf)(ea'f) = e\,af e\,a'f = 0$, since $fe = 0$; so $eAf \cdot eAf = 0$, and likewise $fAe \cdot fAe = 0$. A mixed Peirce space is therefore closed under the product, but with the identically zero product: it is a subalgebra without a unit, and it carries no algebra structure that could enter a decomposition of $A$ as a product. In the biquaternion case this is the nilpotence of the two mixed basis elements, $\hat\Upsilon_1^2 = \hat\Upsilon_2^2 = 0$ (§*The Off-Diagonal Elements*).

**Rows and columns.** The sums of a row and of a column of the table are the one-sided ideals generated by the idempotents,

$$
\bigoplus_{j=1}^n e_i A e_j = e_i A, \qquad \bigoplus_{i=1}^n e_i A e_j = A e_j ,
$$

the first being the right ideal generated by $e_i$ and the second the left ideal generated by $e_j$. The Peirce decomposition therefore contains the right-ideal decomposition as its rows and the left-ideal decomposition as its columns, and the two groupings of the same spaces differ exactly as the two groupings of §*The Decomposition into Minimal Left and Right Ideals* differ.

### The Biquaternion Case

Take the complete orthogonal family $\tilde\Pi_+, \tilde\Pi_-$ of §*Idempotents and Orthogonal Idempotents*, the pair of the root $\tilde\Xi$ of $+1$. Write $\mathbb{B}_{st}$ for the corner $\tilde\Pi_s\mathbb{B}\tilde\Pi_t$, with $s,t\in\{+,-\}$. The Peirce decomposition of $\mathbb{B}$ is

$$
\mathbb{B} = \mathbb{B}_{++} \oplus \mathbb{B}_{+-} \oplus \mathbb{B}_{-+} \oplus \mathbb{B}_{--}, \qquad \mathbb{B}_{st} = \tilde\Pi_s\mathbb{B}\tilde\Pi_t,
$$

and by the multiplication table of §*The Off-Diagonal Elements* each corner is one-dimensional over $\mathbb{C}$:

$$
\mathbb{B}_{++} = \mathbb{C}\tilde\Pi_+, \qquad \mathbb{B}_{+-} = \mathbb{C}\hat\Upsilon_1, \qquad \mathbb{B}_{-+} = \mathbb{C}\hat\Upsilon_2, \qquad \mathbb{B}_{--} = \mathbb{C}\tilde\Pi_-,
$$

so the Peirce decomposition reads

$$
\mathbb{B} = \mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\hat\Upsilon_1 \oplus \mathbb{C}\hat\Upsilon_2 \oplus \mathbb{C}\tilde\Pi_- .
$$

**The root on the corners.** The two signs of the pair are the two eigenvalues of multiplication by the root, and each corner collects one eigenvalue on the left and one on the right:

$$
x\in\mathbb{B}_{st} \iff \tilde\Xi x = s\,x \ \text{ and } \ x\tilde\Xi = t\,x ,
$$

so $\mathbb{B}_{st}$ is the joint eigenspace of the operators of left and right multiplication by $\tilde\Xi$ with the eigenvalues $s$ and $t$. The root splits the algebra twice, once by each multiplication, and the diagonal corners $\mathbb{B}_{++}$ and $\mathbb{B}_{--}$ are the components on which the two signs agree.

**The corners multiply by their signs.** For $x\in\mathbb{B}_{st}$ and $y\in\mathbb{B}_{uv}$ one has $\tilde\Xi(xy)=(\tilde\Xi x)y=s\,xy$ and $(xy)\tilde\Xi=x(y\tilde\Xi)=v\,xy$, and the product vanishes unless the inner signs agree,

$$
\mathbb{B}_{st}\mathbb{B}_{uv} \subseteq \delta_{tu}\,\mathbb{B}_{sv}.
$$

This is the rule of §*A Complete Orthogonal Family* read on the signs: a product of two corners survives exactly when the two inner signs match, and it lies in the corner carrying the two outer signs. It makes the parity grading of §*The Decomposition as a Grading* the grading by the product of the two signs, the even part $\mathbb{B}_{++}\oplus\mathbb{B}_{--}$ against the odd part $\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}$.

### As Many Decompositions as Roots of One

**The Peirce decompositions of $\mathbb{B}$ relative to a complete orthogonal pair of idempotents are in bijection with the roots of $+1$ modulo the sign change $\tilde\Xi\sim-\tilde\Xi$: a root and its opposite give the same decomposition, and no two other roots give the same one.**

The map of §*Idempotents and Orthogonal Idempotents* sends a root $\tilde\Xi$ to the pair $\tilde\Pi_+(\tilde\Xi),\tilde\Pi_-(\tilde\Xi)$, hence to its decomposition. It is surjective, because a complete orthogonal pair $(e,f)$ gives the root $\tilde\Xi=e-f$, whose square is

$$
\tilde\Xi^2 = e^2-ef-fe+f^2 = e+f = e_0 ,
$$

so the pair is the pair of a root and its decomposition is the one of that root. It is injective on the classes, because the root is read back from the pair, $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$, so a pair determines the root up to the interchange of its two members; and the interchange is exactly the replacement of the root by its opposite, $\tilde\Pi_+(-\tilde\Xi)=\tilde\Pi_-(\tilde\Xi)$ and $\tilde\Pi_-(-\tilde\Xi)=\tilde\Pi_+(\tilde\Xi)$. So the classes $\{\tilde\Xi,-\tilde\Xi\}$, the unordered pairs of idempotents and the decompositions correspond one to one.

Read on the three families of the roots of $+1$ (§*Statement of the Theorem* of *Square Roots of One and the Idempotents of the General Plain Algebra*), the count is:

- the trivial class $\{\pm e_0\}$ gives the pair $(e_0,0)$ and the **degenerate decomposition**, whose corners are $\mathbb{B}$ and $0$ rather than four lines;
- the purely imaginary class $\{\pm i\vec n\}$, over the pure real quaternions $\vec n$ with $\vec n^2=-e_0$, is a two-real-parameter family; the change $\vec n\mapsto-\vec n$ leaves the class unchanged, so the classes form a real projective plane, and the two idempotents are Hermitian, the members of the second family of §*The Families of Idempotents* of the companion article, lying in $\mathbb{M}_+$;
- the non-trivial class, the roots $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions of §*The Non-Trivial Roots* of the companion article, is a four-real-parameter family.

So the Peirce decompositions of $\mathbb{B}$ form a two-real-parameter family of Hermitian decompositions and a four-real-parameter family, together with the one degenerate decomposition. Each of them carries the reciprocal $\mathbb{C}^\times$ of normalised mixed bases of §*Systems of Matrix Units*, and all of them are conjugate by an inner automorphism, by the rigidity proved there.

### From One Idempotent to Its Complement

Over $\mathbb{B}$ the decomposition relative to a pair of idempotents is forced by a single idempotent, equivalently by a single root. Let $e \in \mathbb{B}$ be nontrivial and put $f = e_0 - e$; then

$$
\tilde\Xi = e - f = 2e - e_0
$$

is a root of $+1$, since $\tilde\Xi^2 = e + f = e_0$, and $e = \tilde\Pi_+(\tilde\Xi)$, $f = \tilde\Pi_-(\tilde\Xi)$: a nontrivial idempotent is a root in disguise, and the idempotent, the root $\tilde\Xi = 2e-e_0$, the unordered pair $\{e,f\}$ and the decomposition carry the same information. By §*Idempotents and Orthogonal Idempotents* both $e$ and $f$ are primitive, they are orthogonal, and $e + f = e_0$, so $e$ alone determines the pair $(e, f)$ and the decomposition

$$
\mathbb{B} = e\mathbb{B}e \oplus e\mathbb{B}f \oplus f\mathbb{B}e \oplus f\mathbb{B}f .
$$

Every nontrivial idempotent is conjugate to $\tilde\Pi_+$ (§*Systems of Matrix Units*), so this is the decomposition of §*The Biquaternion Case* transported by a unit: each corner is the conjugate of the corresponding standard corner and is therefore a line over $\mathbb{C}$,

$$
e\mathbb{B}e = \mathbb{C}e, \qquad f\mathbb{B}f = \mathbb{C}f, \qquad e\mathbb{B}f = \mathbb{C}u, \qquad f\mathbb{B}e = \mathbb{C}w,
$$

where $u$ and $w$ are any nonzero elements of the two mixed corners. The shape does not move with $e$; only the four lines do. The two mixed corners are square-zero, so their nonzero elements are nilpotent (§*A Complete Orthogonal Family*), and a normalised pair multiplies back onto the diagonal, $e = uw$ with $u^2 = w^2 = 0$: every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents (§*Systems of Matrix Units*).

Read in the matrix model, the idempotent $e$ is a rank-one projector. The standard pair is the two diagonal projectors

$$
\mathsf{M}_2(\tilde\Pi_+)=\begin{pmatrix}1&0\\0&0\end{pmatrix}, \qquad \mathsf{M}_2(\tilde\Pi_-)=\begin{pmatrix}0&0\\0&1\end{pmatrix},
$$

and a general primitive idempotent is determined by two lines of $\mathbb{C}^2$: its **image** line $L$, on which it is the identity, and its **kernel** line $K$, which it annihilates, with $L \oplus K = \mathbb{C}^2$. The map $(L, K) \mapsto e$ is a bijection from the ordered pairs of distinct lines of $\mathbb{P}^1(\mathbb{C})$ onto the primitive idempotents, so these form the set $\mathbb{P}^1(\mathbb{C}) \times \mathbb{P}^1(\mathbb{C}) \setminus \Delta$, where $\Delta$ is the diagonal of equal pairs, of real dimension $4$; this is the four-dimensional idempotent manifold of *Square Roots of One and the Idempotents of the General Plain Algebra*, §*The Correspondence With the Roots of One*, read in the coordinates of the matrix model.

### The Peirce Table

The four products of the basis elements are collected in the table whose entry in row $S$ and column $T$ is the space containing the products of an element of $S$ with an element of $T$:

| $\cdot$ | $\mathbb{C}\tilde\Pi_+$ | $\mathbb{C}\hat\Upsilon_1$ | $\mathbb{C}\hat\Upsilon_2$ | $\mathbb{C}\tilde\Pi_-$ |
|---|---|---|---|---|
| $\mathbb{C}\tilde\Pi_+$ | $\mathbb{C}\tilde\Pi_+$ | $\mathbb{C}\hat\Upsilon_1$ | $0$ | $0$ |
| $\mathbb{C}\hat\Upsilon_1$ | $0$ | $0$ | $\mathbb{C}\tilde\Pi_+$ | $\mathbb{C}\hat\Upsilon_1$ |
| $\mathbb{C}\hat\Upsilon_2$ | $\mathbb{C}\hat\Upsilon_2$ | $\mathbb{C}\tilde\Pi_-$ | $0$ | $0$ |
| $\mathbb{C}\tilde\Pi_-$ | $0$ | $0$ | $\mathbb{C}\hat\Upsilon_2$ | $\mathbb{C}\tilde\Pi_-$ |

The table is the rule $\delta_{jk}$ of §*A Complete Orthogonal Family* read on the basis, and it is sparser than the rule suggests: the products $\hat\Upsilon_1^2$ and $\hat\Upsilon_2^2$ vanish, so the diagonal entries of the two mixed rows and columns are zero, and the surviving entries are the four basis elements themselves. Reading the table by rows gives the two right ideals and by columns the two left ideals, as in §*A Complete Orthogonal Family*.

### The Peirce Coordinates

The decomposition is read in coordinates. Write $\tilde Q = \sum_{\mu=0}^{3}Q_\mu e_\mu$, and let $a_{ij}$ be the coefficient of the one-dimensional corner $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ in the expansion of $\tilde Q$, the matrix position $1$ carrying the $+$ member of the pair and the position $2$ the $-$ member, so that $a_{11}$ is the coordinate on $\mathbb{B}_{++}$, $a_{12}$ on $\mathbb{B}_{+-}$, $a_{21}$ on $\mathbb{B}_{-+}$ and $a_{22}$ on $\mathbb{B}_{--}$; then

$$
a_{11} = Q_0 - iQ_3, \qquad a_{12} = -iQ_1 - Q_2, \qquad a_{21} = -iQ_1 + Q_2, \qquad a_{22} = Q_0 + iQ_3,
$$

so that

$$
\tilde Q = a_{11}\tilde\Pi_+ + a_{12}\hat\Upsilon_1 + a_{21}\hat\Upsilon_2 + a_{22}\tilde\Pi_- ,
$$

and conversely

$$
Q_0 = \tfrac12(a_{11}+a_{22}), \qquad Q_1 = \tfrac{i}{2}(a_{12}+a_{21}), \qquad Q_2 = \tfrac12(a_{21}-a_{12}), \qquad Q_3 = \tfrac{i}{2}(a_{11}-a_{22}).
$$

The four numbers $a_{ij}$ are the **Peirce coordinates** of $\tilde Q$. They are linear functions of $\tilde Q$; the mean of the two diagonal coordinates is the scalar part, and the determinant of their $2\times2$ array is the biquaternion norm,

$$
a_{11}a_{22} - a_{12}a_{21} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = N(\tilde Q)
$$

(*Norm and Invertibility in the General Quaternionic Algebra*). The coordinates are nothing but the four entries of the corpus's fixed matrix element representation: the isomorphism $\mathsf{M}_2 : \mathbb{B}\to M_2(\mathbb{C})$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, §*The Representation*, is

$$
\mathsf{M}_2(\tilde Q) = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}.
$$

The Peirce decomposition therefore supplies the matrix element representation directly: the four spaces are the four matrix units, and the coordinate functions are the entries. §*The Peirce Coordinates and the Matrix Model* below develops that reading.

### The Decomposition as a Grading

The Peirce decomposition of a complete orthogonal family carries a second structure, the parity of the indices. Let $A_0$ be the sum of the diagonal corners and $A_1$ the sum of the mixed ones; the rule $(e_iAe_j)(e_kAe_l)\subseteq\delta_{jk}e_iAe_l$ says that a product of two Peirce spaces vanishes unless the two inner indices agree, and that when they agree the outer indices combine. Reading the label $i+j$ modulo two, so that $A_0$ carries the even class and $A_1$ the odd one, the rule becomes

$$
A_0A_0 \subseteq A_0, \qquad A_0A_1 \subseteq A_1, \qquad A_1A_0 \subseteq A_1, \qquad A_1A_1 \subseteq A_0 ,
$$

which is the multiplication law of the group $\mathbb{Z}/2$: the decomposition $A = A_0\oplus A_1$ is a **grading** of the algebra, $A_0$ is a subalgebra and $A_1$ is a module over it. In the biquaternion case $A_0 = \mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\tilde\Pi_-$ and $A_1 = \mathbb{C}\hat\Upsilon_1 \oplus \mathbb{C}\hat\Upsilon_2$, and the four inclusions are the laws $\hat\Upsilon_1\hat\Upsilon_2 = \tilde\Pi_+$ and $\hat\Upsilon_2\hat\Upsilon_1 = \tilde\Pi_-$ together with $\hat\Upsilon_1^2 = \hat\Upsilon_2^2 = 0$. The grading is the checkerboard of a $2\times2$ matrix: two cells of like colour multiply into the diagonal part and two of unlike colour into the mixed part. In the biquaternion case the parity is the product $st$ of the two signs of the corner, and the checkerboard is the table of the sign products (§*The Biquaternion Case*).

### The Involutions on the Peirce Spaces

Each of the three conjugations permutes the four spaces, with a sign on the two mixed elements:

| | $\tilde\Pi_+$ | $\hat\Upsilon_1$ | $\hat\Upsilon_2$ | $\tilde\Pi_-$ |
|---|---|---|---|---|
| natural ${}^{\natural}$ | $\tilde\Pi_-$ | $-\hat\Upsilon_1$ | $-\hat\Upsilon_2$ | $\tilde\Pi_+$ |
| bar $\bar{\cdot}$ | $\tilde\Pi_-$ | $-\hat\Upsilon_2$ | $-\hat\Upsilon_1$ | $\tilde\Pi_+$ |
| Hermitian ${}^{*}$ | $\tilde\Pi_+$ | $\hat\Upsilon_2$ | $\hat\Upsilon_1$ | $\tilde\Pi_-$ |

the bar being the coefficient conjugation, which is the map $\sigma$ of §*The Real Structure*, and the Hermitian conjugation the composite ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (*Conventions in Mathematics*). All three preserve the set of the four Peirce spaces, and they act on it differently. The natural sign exchanges the two diagonal corners and preserves each mixed space, on which it acts as $-\mathrm{id}$. The bar exchanges the two diagonal corners and also exchanges the two mixed spaces. The Hermitian conjugation fixes each of the two diagonal corners and exchanges the two mixed spaces. The last statement is the general exchange theorem of *Hermitian Idempotents and the Peirce Decomposition*, §*The Involution on the Peirce Spaces*, read on $\mathbb{B}$: the standard idempotents are Hermitian, $\tilde\Pi_+^{*} = \tilde\Pi_+$ and $\tilde\Pi_-^{*} = \tilde\Pi_-$, so the involution carries each corner to itself and the mixed space $\tilde\Pi_+\mathbb{B}\tilde\Pi_-$ onto $\tilde\Pi_-\mathbb{B}\tilde\Pi_+$, exchanging $\hat\Upsilon_1$ and $\hat\Upsilon_2$ and giving the pairing of the two nilpotents recorded in *Conventions in Mathematics*, §*The nilpotent convention*. The bar and the natural sign are the two factors of the composite, and each of them fails to fix the standard idempotents; the Hermitian conjugation is the one that respects them.

The diagonal part $\tilde\Pi_+\mathbb{B}\tilde\Pi_+ \oplus \tilde\Pi_-\mathbb{B}\tilde\Pi_- = \mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\tilde\Pi_-$ is a two-dimensional commutative subalgebra isomorphic to $\mathbb{C} \times \mathbb{C}$. Each diagonal corner is a division ring, namely $\mathbb{C}$, which is the primitivity criterion of §*Idempotents and Orthogonal Idempotents*.

A **null (light-cone) variant** of the same split is used in *The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation*. The idempotents there are the uniform nullquaternions $N = \tfrac12(1, \vec n)$ and $\bar N = \tfrac12(1, -\vec n)$, and the two Peirce components of a biquaternion are its **signed parts**, whose sign the source reads as the chirality of the Weyl spinor. The pair is orthogonal and complete in the article's own product — the **outer** product, for which $N \odot N = N$, $\bar N \odot \bar N = \bar N$, $N \odot \bar N = 0$ and $N + \bar N = e_0$ — and the article's matrix isomorphism carries the outer product to the ordinary matrix product and $N, \bar N$ to the two standard diagonal idempotents. It is the same orthogonal pair as above, transported to the light-cone coordinates with the product changed; these same elements are **not** idempotent under the Hamilton product of this article, so the chiral split is naturally stated in that paper's algebra rather than in this one.

## The Peirce Coordinates and the Matrix Model

### The Matrix Model

The Peirce coordinates of §*The Peirce Coordinates* do more than parametrise the elements: read as a matrix, they carry the whole multiplication.

**Proposition.** The map that sends $\tilde Q$ to the matrix $\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22}\end{pmatrix}$ of its Peirce coordinates is an isomorphism of $\mathbb{C}$-algebras $\mathbb{B}\to M_2(\mathbb{C})$, and it carries the four Peirce spaces onto the four matrix units,

$$
\tilde\Pi_+ \mapsto \begin{pmatrix}1&0\\0&0\end{pmatrix}=E_{11}, \qquad
\hat\Upsilon_1 \mapsto \begin{pmatrix}0&1\\0&0\end{pmatrix}=E_{12},
$$
$$
\hat\Upsilon_2 \mapsto \begin{pmatrix}0&0\\1&0\end{pmatrix}=E_{21}, \qquad
\tilde\Pi_- \mapsto \begin{pmatrix}0&0\\0&1\end{pmatrix}=E_{22}.
$$

*Proof.* The map is $\mathbb{C}$-linear and bijective, since the four basis elements of $\mathbb{B}$ go to the four basis matrices of $M_2(\mathbb{C})$; it is multiplicative because the four Peirce basis elements multiply as the four matrix units do — the Peirce table of §*The Peirce Table* is the table $E_{ij}E_{kl} = \delta_{jk}E_{il}$ of *Matrix Algebras*, §*Matrix Units* — and both multiplications are bilinear.

The isomorphism is the corpus's $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, written there as an assignment on the basis; what the Peirce decomposition adds is the reading of its four entries as the coordinates of the four corners. Its trace and its determinant are the two invariants of the Peirce decomposition, $\operatorname{tr} = a_{11}+a_{22} = 2Q_0$ and $\det = a_{11}a_{22}-a_{12}a_{21} = N(\tilde Q)$, so that the scalar part and the norm of the algebra are the two symmetric functions of the corner coordinates (§*The Peirce Coordinates*). In this model the left ideals are the columns and the right ideals the rows, which is the content of §*The Decomposition into Minimal Left and Right Ideals* read on the matrix side: $\mathbb{B}\tilde\Pi_+$ is the first column $\mathbb{C}E_{11}\oplus\mathbb{C}E_{21}$ and $\tilde\Pi_+\mathbb{B}$ is the first row $\mathbb{C}E_{11}\oplus\mathbb{C}E_{12}$, the two groupings of the four matrix units that *Matrix Algebras*, §*The Case $n = 2$* distinguishes.

### Systems of Matrix Units

**Definition.** A **system of $2\times2$ matrix units** in $\mathbb{B}$ is a family $\{E_{11}, E_{12}, E_{21}, E_{22}\}$ of elements of $\mathbb{B}$ with

$$
E_{ij}E_{kl} = \delta_{jk}E_{il}, \qquad E_{11} + E_{22} = e_0, \qquad E_{11} \neq 0 .
$$

The definition is the abstract form of the multiplication of the coordinate matrices, and it is redundant on purpose: the relations already give $E_{11}^2 = E_{11}$, $E_{22}^2 = E_{22}$ and $E_{11}E_{22} = E_{22}E_{11} = 0$, so that $E_{11}$ and $E_{22}$ are orthogonal idempotents summing to the unit, and the two off-diagonal elements are nilpotent, $E_{12}^2 = E_{21}^2 = 0$.

**Proposition.** A system of matrix units is the same data as a Peirce decomposition with two primitive idempotents, together with a basis of each of the two mixed spaces normalised by $E_{12}E_{21} = E_{11}$. The standard system is the one of §*The Off-Diagonal Elements*,

$$
E_{11} = \tilde\Pi_+, \qquad E_{12} = \hat\Upsilon_1, \qquad E_{21} = \hat\Upsilon_2, \qquad E_{22} = \tilde\Pi_- .
$$

**Construction from an arbitrary idempotent.** Fix a primitive $e$ and put $f = e_0 - e$; choose nonzero $u \in e\mathbb{B}f$ and $w \in f\mathbb{B}e$. Under a conjugacy carrying the standard pair to $(e, f)$ (§*From One Idempotent to Its Complement*), the elements $u$ and $w$ are the images of $\alpha\hat\Upsilon_1$ and $\beta\hat\Upsilon_2$ for some $\alpha, \beta \in \mathbb{C}^\times$, and the standard products $\hat\Upsilon_1\hat\Upsilon_2 = \tilde\Pi_+$ and $\hat\Upsilon_2\hat\Upsilon_1 = \tilde\Pi_-$ give

$$
u w = \alpha\beta\, e, \qquad w u = \alpha\beta\, f .
$$

With $\lambda = \alpha\beta \in \mathbb{C}^\times$ the same on both sides, the elements

$$
E_{11} = e, \qquad E_{22} = f, \qquad E_{12} = u, \qquad E_{21} = \lambda^{-1} w
$$

form a system of matrix units with $E_{11} = e$. The pair $(u, w)$ is not determined by $e$: replacing $u$ by $\mu u$ and $w$ by $\mu^{-1} w$ with $\mu \in \mathbb{C}^\times$ leaves $\lambda$ and every product of the system unchanged. A fixed primitive idempotent therefore determines its Peirce decomposition but carries a reciprocal $\mathbb{C}^\times$ of normalised mixed bases, the off-diagonal rescaling that appears as the diagonal torus in the proof of the theorem below.

**Proposition (a nontrivial idempotent is a product of two nilpotents).** Every nontrivial idempotent of $\mathbb{B}$ is a product of two nilpotents, and the two mixed units of its Peirce decomposition supply the factorisation.

*Proof.* Let $e$ be a nontrivial idempotent and $f = e_0 - e$ its complement, so that $e$ and $f$ are primitive, orthogonal and sum to $e_0$. The two mixed corners $e\mathbb{B}f$ and $f\mathbb{B}e$ are square-zero (§*From One Idempotent to Its Complement*), so every nonzero $u \in e\mathbb{B}f$ and every nonzero $w \in f\mathbb{B}e$ is nilpotent, $u^2 = w^2 = 0$. By the construction above, $uw = \lambda e$ for some $\lambda \in \mathbb{C}^\times$; replacing $w$ by $\lambda^{-1} w$ keeps it in $f\mathbb{B}e$, nonzero and square-zero, and gives $uw = e$. So $e$ is the product of the two nilpotents $u$ and $\lambda^{-1} w$. The standard case is the multiplication table of §*The Off-Diagonal Elements*, $\hat\Upsilon_1\hat\Upsilon_2 = \tilde\Pi_+$ and $\hat\Upsilon_2\hat\Upsilon_1 = \tilde\Pi_-$ with $\hat\Upsilon_1^2 = \hat\Upsilon_2^2 = 0$.

The trivial idempotent $e_0$ is the one idempotent that is not such a product: if $uv = e_0$ then $u$ has the right inverse $v$, so $u$ is a unit, whereas a nilpotent is not a unit. The other trivial idempotent, $0$, is a product of two nilpotents, $0 \cdot 0 = 0$. Among the idempotents of $\mathbb{B}$, therefore, all but $e_0$ are products of two nilpotents.

**Theorem (the Peirce decomposition is unique up to conjugation).** Every system of $2\times2$ matrix units of $\mathbb{B}$ is the image of the standard system under an inner automorphism: there is a unit $\tilde G \in \mathbb{B}$ with $E_{ij} = \tilde G\,\tilde E_{ij}\,\tilde G^{-1}$ for the standard system $\{\tilde E_{ij}\}$. Consequently all Peirce decompositions of $\mathbb{B}$ with two primitive idempotents are conjugate, and a statement about one of them is a statement about all.

*Proof.* By the matrix model of §*The Matrix Model* the question is the corresponding statement for $M_2(\mathbb{C})$, and there it is proved by change of basis. A primitive idempotent $P$ of $M_2(\mathbb{C})$ is the projector onto a line $\ell$ along another line $m$, $\ell$ being its image and $m$ its kernel; choosing a basis with first vector in $\ell$ and second in $m$, and letting $G$ be the matrix of that basis, gives $GPG^{-1} = E_{11}$. The stabiliser of $E_{11}$ is the diagonal torus, since a conjugation that fixes $E_{11}$ must preserve its image and its kernel; conjugating by the diagonal matrix $\operatorname{diag}(a,d)$ fixes $E_{11}$ and $E_{22}$ and multiplies $E_{12}$ by $a/d$ and $E_{21}$ by $d/a$. In a system of matrix units with $E_{11}$ and $E_{22}$ fixed, the two off-diagonal elements are determined by a single scalar, because they lie in the one-dimensional mixed spaces and satisfy $E_{12}E_{21} = E_{11}$; the diagonal conjugation is transitive on that scalar, so the system is carried to the standard one. The unit group of $\mathbb{B}$ acts by algebra automorphisms, since every automorphism of $\mathbb{B}$ is inner (*Biquaternion Automorphisms and Derivations*, §*Automorphisms over $\mathbb{C}$*), and an automorphism carries a system of matrix units to a system of matrix units.

The theorem is the rigidity of the Peirce decomposition, and it should be read with two counts that it does not contradict. The **idempotents** that occur are not unique: every primitive idempotent of $\mathbb{B}$ appears, and these form the real four-dimensional idempotent manifold of *Square Roots of One and the Idempotents of the General Plain Algebra*, §*The Correspondence With the Roots of One*, not the two points $\tilde\Pi_+, \tilde\Pi_-$. The **left ideals** that occur are not unique either: they form the projective line $\mathbb{P}^1(\mathbb{C})$ of §*The Lattice of Left Ideals*. What is unique is the decomposition up to conjugation: the idempotent may be carried anywhere by a unit, and the unit conjugation carries the decomposition with it. Equivalently, $\mathbb{B}$ has one Peirce decomposition of this shape modulo the inner automorphisms — the statement that the algebra has a single block structure, namely the $2\times2$ block structure of a matrix algebra, and that all the decompositions of §*The Peirce Decomposition* are that structure seen in different bases.

The **stabiliser** of the standard pair in the unit group of $\mathbb{B}$ is the torus $\{\,a\tilde\Pi_+ + b\tilde\Pi_- : a, b \in \mathbb{C}^\times\,\}$. It fixes $\tilde\Pi_+$ and $\tilde\Pi_-$ and acts on the two mixed elements by

$$
\hat\Upsilon_1 \mapsto \frac{a}{b}\,\hat\Upsilon_1, \qquad \hat\Upsilon_2 \mapsto \frac{b}{a}\,\hat\Upsilon_2,
$$

which is exactly the reciprocal $\mathbb{C}^\times$ scaling of the construction of §*Systems of Matrix Units*. The Peirce decompositions are therefore the points of the idempotent manifold — uncountably many — each carrying its $\mathbb{C}^\times$ of normalised mixed bases, and the inner automorphisms act transitively on the whole family.

## The Decomposition into Minimal Left and Right Ideals

The two idempotents group the basis into one-sided ideals in a second way. The two **left ideals** $\mathbb{B}\tilde\Pi_+, \mathbb{B}\tilde\Pi_-$ and the two **right ideals** $\tilde\Pi_+\mathbb{B}, \tilde\Pi_-\mathbb{B}$ are one-sided, and

$$
\mathbb{B} = \mathbb{B}\tilde\Pi_+ \oplus \mathbb{B}\tilde\Pi_- = (\mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\hat\Upsilon_2) \oplus (\mathbb{C}\hat\Upsilon_1 \oplus \mathbb{C}\tilde\Pi_-),
$$

$$
\mathbb{B} = \tilde\Pi_+\mathbb{B} \oplus \tilde\Pi_-\mathbb{B} = (\mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\hat\Upsilon_1) \oplus (\mathbb{C}\hat\Upsilon_2 \oplus \mathbb{C}\tilde\Pi_-).
$$

The first exhibits $\mathbb{B}$ as a direct sum of the two minimal left ideals; the second exhibits it as a direct sum of the two minimal right ideals. The two groupings of the same four basis elements differ: the Peirce decomposition groups $\tilde\Pi_+$ with $\hat\Upsilon_1$ and $\tilde\Pi_-$ with $\hat\Upsilon_2$, whereas the left-ideal decomposition groups $\tilde\Pi_+$ with $\hat\Upsilon_2$ and $\tilde\Pi_-$ with $\hat\Upsilon_1$. Each left ideal is two-dimensional over $\mathbb{C}$; each right ideal is its dual. Since $\mathbb{B}$ is simple, a one-sided ideal is never two-sided; for instance $\mathbb{B}\tilde\Pi_+$ is not stable under right multiplication by $\hat\Upsilon_1$.

**Why the sum is direct, and the dimensions.** Every $\tilde{Q} \in \mathbb{B}$ satisfies $\tilde{Q} = \tilde{Q}(\tilde\Pi_+ + \tilde\Pi_-) = \tilde{Q}\tilde\Pi_+ + \tilde{Q}\tilde\Pi_-$, so the two left ideals span. Their intersection is zero: if $\tilde{Q}\tilde\Pi_+ = \tilde{P}\tilde\Pi_-$, then multiplying on the right by $\tilde\Pi_+$ and using $\tilde\Pi_+^2 = \tilde\Pi_+$ and $\tilde\Pi_-\tilde\Pi_+ = 0$ gives $\tilde{Q}\tilde\Pi_+ = 0$. The basis above reads $\mathbb{B}\tilde\Pi_+ = \mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\hat\Upsilon_2$, of dimension $2$ over $\mathbb{C}$ and $4$ over $\mathbb{R}$, with $\mathbb{B}\tilde\Pi_- = \mathbb{C}\hat\Upsilon_1 \oplus \mathbb{C}\tilde\Pi_-$ for the second; together they account for $4 + 4 = 8 = \dim_{\mathbb{R}} \mathbb{B}$. Each is a minimal left ideal, by the primitivity of $\tilde\Pi_+$ and $\tilde\Pi_-$ (§*Idempotents and Orthogonal Idempotents*, §*Minimal Left and Right Ideals*).

**The module structure.** With the basis $\{\tilde\Pi_+, \hat\Upsilon_2\}$ the left $\mathbb{B}$-module $\mathbb{B}\tilde\Pi_+$ is $\mathbb{C}^2$, and the central element $i$ acts on it as the scalar $i$:
$$
i\,(\alpha \tilde\Pi_+ + \beta \hat\Upsilon_2) = (i\alpha)\tilde\Pi_+ + (i\beta)\hat\Upsilon_2 .
$$
So the simple module underlying each minimal left ideal is the standard two-dimensional one, with $i$ acting by the identity matrix.

## Minimal Left and Right Ideals

A **minimal left ideal** is a nonzero left ideal containing no nonzero proper left ideal; equivalently, a simple submodule of the left regular module. A **minimal right ideal** is defined the same way on the right.

Over $\mathbb{C}$, since $\mathbb{B}$ is semisimple, every left ideal of $\mathbb{B}$ is a direct sum of minimal left ideals, and every minimal left ideal is of the form $\mathbb{B}e$ for a primitive idempotent $e$. The examples are the left ideals $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$ of §*The Decomposition into Minimal Left and Right Ideals*, and all minimal left ideals are isomorphic as left $\mathbb{B}$-modules: a general one is obtained from $\mathbb{B}\tilde\Pi_+$ by an algebra automorphism, so it has the same shape in a suitable basis. Dually, every minimal right ideal is isomorphic to $\tilde\Pi_+\mathbb{B}$. Thus there is one isomorphism class of simple left modules and one of simple right modules. Being nonzero proper one-sided ideals, none of them is two-sided — which is exactly why their abundance is compatible with §*The Two-Sided Ideals: Simplicity of $\mathbb{B}$*.

## The Lattice of Left Ideals

Over $\mathbb{C}$, every left ideal of the simple artinian algebra $\mathbb{B}$ is a direct sum of minimal left ideals, so the left ideals are exactly $0$, the minimal ones, and $\mathbb{B}$. The minimal left ideals form the middle layer of the lattice,

$$
0 \;\subset\; \{\, L : L \text{ a minimal left ideal} \,\} \;\subset\; \mathbb{B},
$$

the elements of the middle layer being pairwise incomparable, each covering $0$ and covered by $\mathbb{B}$. Because the length of $\mathbb{B}$ as a left module over itself is $2$, every minimal left ideal is also a **maximal** left ideal, nothing lying strictly between it and $\mathbb{B}$. The minimal left ideals are parametrized by the projective line $\mathbb{P}^1(\mathbb{C})$. Right ideals admit the same description, with the dual parametrization.

The parameter space deserves a caution. In the Wedderburn–Artin decomposition $M_n(D)$ of a simple artinian algebra, the minimal one-sided ideals are parametrized by the projective space $\mathbb{P}^{n-1}(D)$ over the **division ring** $D$, not over an arbitrary base field. Here $D = \mathbb{C}$ and $n = 2$, so the parameter space is $\mathbb{P}^1(\mathbb{C})$. In particular, regarding $\mathbb{B}$ as an $\mathbb{R}$-algebra does not replace this by $\mathbb{P}^1(\mathbb{R})$: the one-sided ideals are still parametrized by $\mathbb{P}^1(\mathbb{C})$. The real projective line appears only as the subfamily that the real structure preserves, not as a set of fixed minimal left ideals: §*The Real Structure* shows that no minimal left ideal is stable under coefficient conjugation.

## The Radical

The **Jacobson radical** $J(A)$ is the intersection of all maximal left ideals of $A$, equivalently of all maximal right ideals; it is a two-sided ideal. For an artinian ring, $J(A)$ is the largest nilpotent ideal and $A/J(A)$ is semisimple; an artinian ring is semisimple if and only if its radical is zero.

Over $\mathbb{C}$, the radical of $\mathbb{B}$ vanishes:

$$
J(\mathbb{B}) = 0.
$$

Indeed $J(\mathbb{B})$ is a two-sided ideal, hence by simplicity is $0$ or $\mathbb{B}$; it cannot be $\mathbb{B}$, since in a unital algebra the radical is proper. This restates the semisimplicity of §*Artinian, Semisimple, and Length Two* in terms of the radical. Consequences over $\mathbb{C}$:

- $\mathbb{B}$ has no nonzero **nilpotent two-sided ideals**; the nilradical is zero.
- It has no nonzero nilpotent left or right ideals either, since such an ideal generates a nonzero nilpotent two-sided ideal.
- The absence of a radical is not the absence of nilpotent **elements**: $\hat\Upsilon_1^2 = \hat\Upsilon_2^2 = 0$ (§*The Off-Diagonal Elements*) — nilpotents of the biquaternion layer, written $\hat\Upsilon_1$ and $\hat\Upsilon_2$ for the two particular units and $\tilde\Upsilon$ where the class is what is meant (§*The nilpotent convention* of *Conventions in Mathematics*) — yet the left ideal generated by $\hat\Upsilon_1$ is not nilpotent.
- Every left $\mathbb{B}$-module is semisimple.

## The Real Structure

Everything so far was stated over $\mathbb{C}$. We now regard the same set $\mathbb{B}$ as an eight-dimensional algebra over $\mathbb{R}$ and record what changes.

**(a) The ideal lattice does not change.** By the base-field remark of §*Ideals in an Algebra*, an additive subgroup closed under left multiplication by $\mathbb{B}$ is automatically a complex subspace, because multiplication by $i$ is left multiplication by the central element $i e_0$. So an $\mathbb{R}$-left ideal is the same thing as a $\mathbb{C}$-left ideal, and the same holds on the right and for two-sided ideals. In particular, over $\mathbb{R}$: $\mathbb{B}$ is still simple, with two-sided ideals only $0$ and $\mathbb{B}$; the minimal left ideals are the same subsets, parametrized by $\mathbb{P}^1(\mathbb{C})$; the radical is still zero; and the length as a module over itself is still $2$.

**(b) The algebra is not central over $\mathbb{R}$.** The centre of $\mathbb{B}$ is the copy of $\mathbb{C}$ spanned by $e_0$ and $i e_0$ — the **complex subspace** $\mathbb{C}_{\mathbb{B}}$ — a proper field extension of $\mathbb{R}$ of degree $2$. Thus $\mathbb{B}$ is a simple $\mathbb{R}$-algebra but not a **central simple** one. In the Wedderburn–Artin description $\mathbb{B} \cong M_n(D)$ over $\mathbb{R}$, one has $n = 2$ and $D = \mathbb{C}$.

**(c) The enrichment appears after extension of scalars.** The complexification of the real algebra $\mathbb{B}$ is

$$
\mathbb{B} \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}) \otimes_{\mathbb{R}} \mathbb{C} \cong (\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong (\mathbb{C} \oplus \mathbb{C}) \otimes_{\mathbb{R}} \mathbb{H} \cong \mathbb{B} \oplus \mathbb{B},
$$

using $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \oplus \mathbb{C}$ and the associativity and commutativity of $\otimes_{\mathbb{R}}$. The algebra on the right is **not simple**: its two-sided ideals are $0$, the two summands, and the whole ring. So the real biquaternion algebra is **not absolutely simple**: simple over $\mathbb{R}$, but with a complexification that splits as a product of two simple algebras. This is the precise sense in which the real structure carries a richer two-sided ideal theory — not in the lattice of $\mathbb{B}$ itself, which is $\{0, \mathbb{B}\}$ in both views, but in the lattice produced by base change. In contrast, $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{B}$ is simple: it is the real biquaternion algebra, not $\mathbb{H}$, whose complexification splits.

**(d) The action of complex conjugation on the lattice.** Complex conjugation $\tilde{Q} \mapsto \bar{\tilde{Q}} = \sum_\mu \bar{Q}_\mu e_\mu$ is an $\mathbb{R}$-algebra automorphism of $\mathbb{B}$ (it is $\mathbb{C}$-antilinear); write $\sigma$ for it. It permutes the left ideals, $\sigma(\mathbb{B}\tilde{\chi}) = \mathbb{B}\sigma(\tilde{\chi})$. Since $\sigma(\tilde\Pi_+) = \tilde\Pi_-$ and $\sigma(\tilde\Pi_-) = \tilde\Pi_+$, it **interchanges the two standard left ideals**:

$$
\sigma(\mathbb{B}\tilde\Pi_+) = \mathbb{B}\tilde\Pi_-, \qquad \sigma(\mathbb{B}\tilde\Pi_-) = \mathbb{B}\tilde\Pi_+.
$$

On the parametrizing projective line the induced map $t \mapsto -1/\bar{t}$ has no fixed point, so **no minimal left ideal is stable under complex conjugation**. The **real lines** still form the real projective line $\mathbb{P}^1(\mathbb{R}) \subset \mathbb{P}^1(\mathbb{C})$, which $\sigma$ preserves and acts on as the antipodal map. So although the lattice of left ideals is unchanged from $\mathbb{C}$ to $\mathbb{R}$, the real structure does not mark out conjugation-stable minimal left ideals; what it marks out is the subfamily $\mathbb{P}^1(\mathbb{R})$ that it preserves.

**(e) The real structure on the Peirce spaces.** Each of the four Peirce spaces of §*The Peirce Decomposition* is a complex line, hence a real plane of dimension $2$; the decomposition into four real planes is what the real view adds to the complex statement. The coefficient conjugation $\sigma$ acts on the four spaces as in §*The Involutions on the Peirce Spaces*: it exchanges the two diagonal corners, $\sigma(\mathbb{C}\tilde\Pi_+) = \mathbb{C}\tilde\Pi_-$, and it exchanges the two mixed corners, $\sigma(\mathbb{C}\hat\Upsilon_1) = \mathbb{C}\hat\Upsilon_2$. It therefore preserves the Peirce grading of §*The Decomposition as a Grading* as a pair of subspaces — it fixes $A_0$ and $A_1$ — while permuting the two summands inside each, and it fixes none of the four spaces individually. The Hermitian conjugation, the composite of $\sigma$ with the natural sign, is the conjugation that respects the standard idempotents: it fixes each diagonal corner and exchanges the two mixed ones, the exchange of *Hermitian Idempotents and the Peirce Decomposition*, §*The Involution on the Peirce Spaces*. So the real structure does not single out a Peirce space; what it singles out is the pair of Hermitian idempotents $\tilde\Pi_+, \tilde\Pi_-$ whose corners it fixes, and it is by that pair that the real and the complex Peirce decompositions are matched.

## Summary

| Statement | Over $\mathbb{C}$ | Over $\mathbb{R}$ |
|---|---|---|
| Dimension | $4$ | $8$ |
| Algebra type | simple $\mathbb{C}$-algebra, $\dim 4$ | simple $\mathbb{R}$-algebra, $\dim 8$ |
| Two-sided ideals | $0$, $\mathbb{B}$ (simple) | $0$, $\mathbb{B}$ (simple) |
| Central simple? | yes, centre $\mathbb{C}$ | no, centre $\mathbb{C} \neq \mathbb{R}$ |
| Left ideals | $0$, the $\mathbb{P}^1(\mathbb{C})$ of minimal ones, $\mathbb{B}$ | same lattice |
| Minimal left ideals | all isomorphic | same; $\sigma$ pairs them, none stable |
| Minimal right ideals | all isomorphic | same |
| Peirce decomposition | $\mathbb{C}\tilde\Pi_+ \oplus \mathbb{C}\hat\Upsilon_1 \oplus \mathbb{C}\hat\Upsilon_2 \oplus \mathbb{C}\tilde\Pi_-$, four one-dimensional corners | the same four real planes; $\sigma$ permutes them in pairs |
| Peirce datum | one primitive idempotent $e$, equivalently the root $2e - e_0$ of $+1$; the complement $e_0 - e$ is forced, and a root and its opposite give the same decomposition | the same |
| Mixed basis | a reciprocal $\mathbb{C}^\times$ of normalised bases of the two mixed lines | the same |
| Peirce coordinates | the entries of $\mathsf{M}_2(\tilde Q)$; $a_{11}a_{22}-a_{12}a_{21} = N(\tilde Q)$ | the same, over $\mathbb{R}$ |
| Matrix units | the standard system $\tilde\Pi_+, \hat\Upsilon_1, \hat\Upsilon_2, \tilde\Pi_-$ | the same; every system is conjugate to it |
| Grading | $A_0 \oplus A_1$, $A_0 = \mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_- \cong \mathbb{C}\times\mathbb{C}$, $A_1 = \mathbb{C}\hat\Upsilon_1\oplus\mathbb{C}\hat\Upsilon_2$ | the same; $\sigma$ preserves both parts |
| Jacobson radical | $0$ | $0$ |
| Length as module over itself | $2$ | $2$ |
| Base change $\otimes_{\mathbb{R}}\mathbb{C}$ | — | not simple; splits into two simple factors |

The Peirce decomposition is the second reading of the same four-dimensional space. It is attached to a root of $+1$: the root carries the two idempotents $\tilde\Pi_+$ and $\tilde\Pi_-$, the pair carries the four corners, and there are as many decompositions as roots of $+1$ modulo the sign change — the degenerate one, the two-real-parameter Hermitian family, and the four-real-parameter family of the rest. It carries four structures that the lattice of ideals alone does not show. It is a decomposition into four one-dimensional corners, of which the two diagonal ones are the division ring $\mathbb{C}$ and the two mixed ones are square-zero subalgebras. It is the table of a $2\times2$ matrix, and its four coordinate functions are the entries of the corpus's matrix element representation, so that the scalar part is their mean and the biquaternion norm is their determinant. It is a $\mathbb{Z}/2$-grading, whose even part is the diagonal subalgebra $\mathbb{C}\times\mathbb{C}$ and whose odd part carries the two mixed spaces and the products $\hat\Upsilon_1\hat\Upsilon_2 = \tilde\Pi_+$ and $\hat\Upsilon_2\hat\Upsilon_1 = \tilde\Pi_-$, which make every nontrivial idempotent a product of two nilpotents. And it is acted on by the three conjugations, the natural sign and the bar exchanging the diagonal corners and the Hermitian conjugation fixing them and exchanging the mixed ones. The decomposition is rigid in the only sense available: every system of $2\times2$ matrix units is the image of the standard one under an inner automorphism, so the algebra has a single block structure, and the choices that remain are the idempotent manifold, the reciprocal $\mathbb{C}^\times$ of mixed bases of each decomposition, and the projective line of minimal left ideals of the earlier sections.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra; dimension $4$ over $\mathbb{C}$, $8$ over $\mathbb{R}$ |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary; $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ is the centre |
| $\tilde\Pi_+, \tilde\Pi_-$ | The two idempotents of a root of $+1$, attached to $+1$ and to $-1$: a complete orthogonal pair, $\tilde\Pi_+ + \tilde\Pi_- = e_0$, $\tilde\Pi_+\tilde\Pi_- = \tilde\Pi_-\tilde\Pi_+ = 0$ |
| $\hat\Upsilon_1, \hat\Upsilon_2$ | Nilpotent off-diagonal elements, $\hat\Upsilon_1 = \tfrac{i e_1 - e_2}{2}$, $\hat\Upsilon_2 = \tfrac{i e_1 + e_2}{2}$, $\hat\Upsilon_1^2 = \hat\Upsilon_2^2 = 0$ |
| $\mathbb{B}\tilde\Pi_+ \cong \mathbb{C}^2$ | The minimal left ideal, a simple left $\mathbb{B}$-module, $i$ acting as the scalar $i$ |
| $\mathbb{P}^1(\mathbb{C})$ | The projective line parameterising the minimal left ideals |
| $a_{ij}$ | Peirce coordinate, the coefficient of the corner $\mathbb{B}_{st} = \tilde\Pi_s\mathbb{B}\tilde\Pi_t$; the $(i,j)$ entry of $\mathsf{M}_2(\tilde Q)$, the position $1$ carrying the $+$ member and the position $2$ the $-$ member |
| $\mathsf{M}_2$ | The matrix element representation $\mathbb{B} \cong M_2(\mathbb{C})$, whose entries are the Peirce coordinates |
| $E_{ij}$ | A system of $2\times2$ matrix units, $E_{ij}E_{kl} = \delta_{jk}E_{il}$, $E_{11}+E_{22} = e_0$ |
| $\tilde\Xi = \tilde\Pi_+ - \tilde\Pi_-$ | A root of $+1$ and its pair; a root and its opposite give the same pair, and the root of an idempotent $e$ is $2e - e_0$ |
| $e, f = e_0 - e$ | A primitive idempotent and its complement, the pair of the root $2e - e_0$; one nontrivial $e$ forces the pair $(e, f)$ |
| $u \in e\mathbb{B}f$, $w \in f\mathbb{B}e$ | Nonzero mixed elements; $uw = \lambda e$ and $wu = \lambda f$ with $\lambda \in \mathbb{C}^\times$ |
| $A_0, A_1$ | The diagonal and the mixed parts of the Peirce decomposition, the two graded components |
| $\natural, \bar{\cdot}, {}^{*}$ | The natural, the bar (coefficient) and the Hermitian conjugations, with ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ |
| $\sigma$ | The real structure, pairing the two standard minimal left ideals and the Peirce corners |
| $\mathcal{J}$ | Jacobson radical; it is $0$ for $\mathbb{B}$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982). The standard reference for the Peirce decomposition and the structure theory of finite-dimensional algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001). Simplicity, semisimplicity, the Jacobson radical, and matrix rings.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009). Wedderburn–Artin theory and the radical.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002). Ring and module theory, central simple algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001). The algebraic structure of the biquaternion algebra.
- The companion articles of the Peirce theory: *Unital Algebras* (the general Peirce decomposition and the central case), *Matrix Algebras* (the matrix units, the matrix algebra and the Skolem–Noether theorem), *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (the isomorphism of which the Peirce coordinates are the entries), *Square Roots of One and the Idempotents of the General Plain Algebra* (the roots of $+1$, the two idempotents of a root, and the idempotent manifold), *Hermitian Idempotents and the Peirce Decomposition* (the involution on the Peirce spaces) and *Biquaternion Automorphisms and Derivations* (the inner automorphisms that make the decomposition rigid).
