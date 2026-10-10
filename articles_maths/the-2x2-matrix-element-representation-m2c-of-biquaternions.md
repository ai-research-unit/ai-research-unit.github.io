# __The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, its remarkable subspaces and its norm $N$ are those of *Biquaternions as a Vector Space over $\mathbb{C}$*, *Introduction to the Remarkable Subspaces* and *Biquaternion Norm and Invertibility*.

The **matrix realization** $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$, the theorem that it is an algebra isomorphism, the trace $\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_0$ and the determinant $\det \mathsf{M}_2(\tilde Q)=N(\tilde Q)$, and the remarkable subspaces as matrix conditions are *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; they are used here and not restated. The term representation is used in both senses at once, the concrete realization of the algebra and the technical representation on a vector space.

This article is the further development of that realization. It owns the rank-one elements and the outer product, the characteristic polynomial and the spectrum, the Cayley–Hamilton identity, the matrix form of the four conjugations, the simple module $V$, the matrix units with the projective line, and the structural consequences of the isomorphism. It does not treat the spinor reading of $V$, which belongs to *Biquaternion Spin Geometry*; it does not re-derive the Clifford identification of *The Clifford Algebra Representation*; and it does not reprove the classification of the simple modules or Schur's lemma, which belong to *Modules over the General Plain Algebra of Biquaternions*. No physical vocabulary is used: the matrices below are not gamma matrices and the module is not a spinor of a physical field.

## The Rank-One Elements and the Outer Product

The invertibility corollary of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* says that the zero divisors are the nonzero singular matrices; the matrix form also says what such a matrix is.

**Proposition.** For $\tilde{Q}\neq0$ the following are equivalent: $N(\tilde{Q})=0$; $\mathsf{M}_2(\tilde{Q})$ is singular; $\mathsf{M}_2(\tilde{Q})$ is an outer product
$$
\mathsf{M}_2(\tilde{Q})=uv^{T},\qquad u=\binom{\alpha}{\beta}\neq0,\quad v=\binom{\gamma}{\delta}\neq0,
$$
the pair $(u,v)$ being determined up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$.

**Proof.** The first two are equivalent by $\det \mathsf{M}_2(\tilde{Q})=N(\tilde{Q})$, and $\tilde{Q}\neq0$ makes the matrix nonzero; a nonzero singular two-by-two matrix has rank one. Let $M=\mathsf{M}_2(\tilde{Q})$ have rank one and let $M_{pq}\neq0$ be an entry. Every two-by-two minor of $M$ vanishes, so $M_{iq}M_{pj}=M_{ij}M_{pq}$ for all $i,j$; hence, with $u$ the $q$-th column and $v^{T}$ the $p$-th row divided by $M_{pq}$,
$$
u=\binom{M_{1q}}{M_{2q}},\qquad v^{T}=\frac{1}{M_{pq}}\begin{pmatrix}M_{p1}&M_{p2}\end{pmatrix},
$$
one has $(uv^{T})_{ij}=M_{iq}M_{pj}/M_{pq}=M_{ij}$, so $M=uv^{T}$, and $u\neq0$ because its $p$-th entry is $M_{pq}\neq0$. A different pivot gives a pair differing by precisely the rescaling: the $j$-th columns of $uv^{T}=u'(v')^{T}$ give $u'=\lambda u$ for $\lambda=v_{j}/v'_{j}\neq0$, and the remaining entries give $v'=\lambda^{-1}v$.

**Worked example.** For $\tilde{Q}=e_2+ie_3$ the image is $\mathsf{M}_2(\tilde{Q})=\begin{pmatrix}1&-1\\1&-1\end{pmatrix}$, of rank one; the pivot $M_{11}=1$ gives $u=(1,1)^{T}$, $v=(1,-1)^{T}$, and the pivot $M_{12}=-1$ gives $u=(-1,-1)^{T}$, $v=(-1,1)^{T}$, the same pair rescaled by $\lambda=-1$.

## The Characteristic Polynomial and the Spectrum

**Definition.** The **spectrum** of a biquaternion $\tilde{Q}$ is the spectrum of the matrix $\mathsf{M}_2(\tilde{Q})$, that is, its two eigenvalues in $\mathbb{C}$. This is the unqualified meaning of the word in the series; the other inequivalent spectra are the subject of *Biquaternion Spectral Theory*.

**Proposition (characteristic polynomial).** The characteristic polynomial of $\mathsf{M}_2(\tilde{Q})$ is

$$
\det\bigl(\lambda I - \mathsf{M}_2(\tilde{Q})\bigr) = \lambda^2 - 2Q_0\,\lambda + N(\tilde{Q}),
$$

so the spectrum is $\{Q_0 + iB,\; Q_0 - iB\}$ with $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$, the trace is $2Q_0$, and the determinant is $N(\tilde{Q})$.

**Proof.** For a $2 \times 2$ matrix the characteristic polynomial is $\lambda^2 - \operatorname{Tr}(M)\lambda + \det(M)$, and $\operatorname{Tr}\mathsf{M}_2(\tilde{Q}) = 2Q_0$, $\det \mathsf{M}_2(\tilde{Q}) = N(\tilde{Q})$ by the trace-and-determinant proposition of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. The eigenvalues are the two roots $Q_0 \pm \sqrt{Q_0^2 - N(\tilde{Q})}$, and $Q_0^2 - N(\tilde{Q}) = -(Q_1^2 + Q_2^2 + Q_3^2) = -B^2$.

**Remark (similarity).** Two biquaternions are similar, $\tilde{Q}' = S\tilde{Q}S^{-1}$ with $S$ invertible, exactly when their matrices are similar, so the spectrum is a similarity invariant. The similarity classification, the eigenvalue dichotomy, and the resolvent are the subject of *Biquaternion Spectral Theory*, which also records the several inequivalent meanings of "spectrum".

## The Cayley–Hamilton Identity

**Proposition.** Every biquaternion satisfies the **Cayley–Hamilton identity**

$$
\tilde{Q}^2 - 2Q_0\,\tilde{Q} + N(\tilde{Q})\,e_0 = 0 .
$$

**Proof.** Cayley–Hamilton for the $2 \times 2$ matrix $\mathsf{M}_2(\tilde{Q})$ reads $\mathsf{M}_2(\tilde{Q})^2 - \operatorname{Tr}\mathsf{M}_2(\tilde{Q})\,\mathsf{M}_2(\tilde{Q}) + \det \mathsf{M}_2(\tilde{Q})\,I = 0$. Substituting the trace and the determinant of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, $\operatorname{Tr}\mathsf{M}_2(\tilde{Q}) = 2Q_0$ and $\det \mathsf{M}_2(\tilde{Q}) = N(\tilde{Q})$, and transporting back along the injective map $\mathsf{M}_2$ gives the identity.

**Remark.** This is the identity that reduces every power of $\tilde{Q}$ to a combination of $e_0$ and $\tilde{Q}$, and it is the starting point for the closed forms of the exponential and the trigonometric functions in *Biquaternion Elementary Functions*.

## The Conjugations in Matrix Form

The four conjugations of $\mathbb{B}$ act on the matrices, and three of the four are read off at once: quaternion conjugation is the adjugate, Hermitian conjugation is the conjugate transpose, and anti-Hermitian conjugation is its negative. Complex conjugation is the one that requires care.

**Proposition (quaternion conjugation is the adjugate).** For every biquaternion $\tilde{Q}$,

$$
\mathsf{M}_2(\tilde{Q}^{\natural}) = \operatorname{adj}\bigl(\mathsf{M}_2(\tilde{Q})\bigr), \qquad \det \mathsf{M}_2(\tilde{Q}^{\natural}) = N(\tilde{Q}^{\natural}) = N(\tilde{Q}),
$$

where $\operatorname{adj}(M)$ is the adjugate of $M$, the transpose of the cofactor matrix. Equivalently, $\mathsf{M}_2(\tilde{Q}^{\natural}) = \epsilon\, \mathsf{M}_2(\tilde{Q})^{\mathsf{T}} \epsilon^{-1}$ with $\epsilon = i\sigma_2$.

**Proof.** The adjugate of a $2 \times 2$ matrix satisfies $M \operatorname{adj}(M) = \det(M) I$ and has entries the cofactors. Replacing $Q_1, Q_2, Q_3$ by their negatives in the explicit formula for $\mathsf{M}_2(\tilde{Q})$ and comparing with the cofactor matrix gives the identity directly. For the second form, note that $\epsilon \mathsf{M}_2(\tilde{Q})^{\mathsf{T}}\epsilon^{-1}$ equals the adjugate for every $2 \times 2$ matrix $M$, since $\operatorname{adj}(M) = \det(M) M^{-1}$ when $M$ is invertible and the identity is polynomial in the entries. The determinant identity is $N(\tilde{Q}^{\natural}) = N(\tilde{Q})$, the invariance of the determinant $N$ under quaternion conjugation.

**Remark (the delicate point: complex conjugation is not entrywise).** Complex conjugation does **not** act entrywise on $\mathsf{M}_2(\tilde{Q})$. The realization is built with the same $i$ that conjugates the coefficients, and the two operations compete: conjugating the entries of $\mathsf{M}_2(\tilde{Q})$ sends $-i\sigma_1 \mapsto +i\sigma_1$, which is the negative of the image of $e_1$, while the image of $e_2$ is a real matrix and is preserved. Entrywise conjugation is therefore not $\mathsf{M}_2(\bar{\tilde{Q}})$, and it is not the image of any of the four involutions of the algebra. The correct correspondence dresses the conjugation with the **antisymmetric form**

$$
\epsilon = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = i\sigma_2 = \mathsf{M}_2(-e_2), \qquad \epsilon^{\mathsf{T}} = -\epsilon, \qquad \epsilon^2 = -I :
$$

$$
\mathsf{M}_2(\bar{\tilde{Q}}) = \epsilon \, (\mathsf{M}_2(\tilde{Q}))^{\natural} \, \epsilon^{-1}, \qquad (\mathsf{M}_2(\tilde{Q}))^{\natural} \neq \mathsf{M}_2(\bar{\tilde{Q}}) \text{ in general}.
$$

For $\tilde{Q} = e_1$ the two sides differ by a sign: $\overline{\mathsf{M}_2(e_1)} = +i\sigma_1 = -\mathsf{M}_2(e_1)$, while $\epsilon \overline{\mathsf{M}_2(e_1)}\epsilon^{-1} = \mathsf{M}_2(e_1)$ because $e_1^* = e_1$. For $\tilde{Q} = e_2$ the matrices agree entrywise, since $\mathsf{M}_2(e_2)$ is real. This is the single place in the matrix realization where the plausible guess is wrong, and it is the reason the correspondence is stated with the antisymmetric form and not with transposition alone.

**Proposition (Hermitian and anti-Hermitian conjugation).** For every biquaternion $\tilde{Q}$,

$$
\mathsf{M}_2(\tilde{Q}^{*}) = \mathsf{M}_2(\tilde{Q})^\dagger, \qquad \mathsf{M}_2(\tilde{Q}^\flat) = -\mathsf{M}_2(\tilde{Q})^\dagger,
$$

where ${}^\dagger$ on the right is the conjugate transpose.

**Proof.** Hermitian conjugation is the composite ${}^{\natural} \circ \bar{\cdot}$, so $\mathsf{M}_2(\tilde{Q}^{*}) = \mathsf{M}_2\bigl(\bar{\bar{\tilde{Q}}}\bigr) = \epsilon\,\mathsf{M}_2(\bar{\tilde{Q}})^{\mathsf{T}}\,\epsilon^{-1}$, and substituting the correspondence for $\bar{\cdot}$ gives

$$
\mathsf{M}_2(\tilde{Q}^{*}) = \epsilon \bigl( \epsilon (\mathsf{M}_2(\tilde{Q}))^{\natural} \epsilon^{-1} \bigr)^{\mathsf{T}} \epsilon^{-1} = \epsilon^{2}\,((\mathsf{M}_2(\tilde{Q}))^{\natural})^{\mathsf{T}}\,\epsilon^{-2},
$$

where the inner transposition passes through the two factors because $\epsilon^{-1} = \epsilon^{\mathsf{T}}$ and hence $(\epsilon M \epsilon^{-1})^{\mathsf{T}} = \epsilon M^{\mathsf{T}} \epsilon^{-1}$ for every $M$. Since $\epsilon^{2} = -I$ and $(-I)^{-1} = -I$, the two outer factors multiply to $I$, so $\mathsf{M}_2(\tilde{Q}^{*}) = ((\mathsf{M}_2(\tilde{Q}))^{\natural})^{\mathsf{T}} = \mathsf{M}_2(\tilde{Q})^\dagger$. The statement for $\flat$ is the definition $\flat = -{}^{*}$.

**Proposition (the congruence of a unit).** For every unit $\tilde{Q}$ and every $\tilde U$,
$$
\mathsf{M}_2\bigl(\tilde{Q}\tilde U\tilde{Q}^{*}\bigr)=\mathsf{M}_2(\tilde{Q})\,\mathsf{M}_2(\tilde U)\,\mathsf{M}_2(\tilde{Q})^{\dagger},
$$
read off from the multiplicativity of $\mathsf{M}_2$ and from $\mathsf{M}_2(\tilde{Q}^{*})=\mathsf{M}_2(\tilde{Q})^{\dagger}$. The identity is the action of the group of units on the matrix algebra by $*$-congruence: it preserves the Hermitian matrices as a set, multiplies the determinant by $\lvert N(\tilde{Q})\rvert^{2}$ and fixes the rank of $\mathsf{M}_2(\tilde U)$.

## The Simple Module

The matrix realization is the realization in which the module of the algebra is exhibited concretely.

**Definition.** The **simple module** of $\mathbb{B}$ is the complex vector space

$$
V = \mathbb{C}^2 = \left\{ v = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} : v_1, v_2 \in \mathbb{C} \right\}
$$

with the left action

$$
\tilde{Q} \cdot v = \mathsf{M}_2(\tilde{Q})\, v .
$$

**Proposition.** The action above makes $V$ a left $\mathbb{B}$-module, and $V$ is simple: it has no nonzero proper submodule.

**Proof.** The action is $\mathbb{C}$-linear in $v$ because $\mathsf{M}_2(\tilde{Q})$ is a matrix, and it is compatible with multiplication because $\mathsf{M}_2$ is a homomorphism: $\tilde{P}\cdot(\tilde{Q}\cdot v) = \mathsf{M}_2(\tilde{P})\mathsf{M}_2(\tilde{Q})v = \mathsf{M}_2(\tilde{P}\tilde{Q})v = (\tilde{P}\tilde{Q})\cdot v$, and $e_0 \cdot v = v$. For simplicity, a submodule is a subspace of $\mathbb{C}^2$ stable under every matrix in $M_2(\mathbb{C})$, because $\mathsf{M}_2$ is surjective; a nonzero stable subspace contains a nonzero vector, and applying the matrix units $E_{11}, E_{12}, E_{21}, E_{22}$ to it produces both standard basis vectors, so the subspace is all of $\mathbb{C}^2$.

**Theorem (uniqueness of the simple module).** Up to isomorphism, $V$ is the only simple left $\mathbb{B}$-module. Consequently every finitely generated $\mathbb{B}$-module is a direct sum of copies of $V$.

**Proof.** Over the field $\mathbb{C}$, the algebra $\mathbb{B} \cong M_2(\mathbb{C})$ is semisimple, every simple module is a minimal left ideal, and all minimal left ideals of a full matrix algebra are isomorphic to the column space; the classification and Schur's lemma are the subject of *Modules over the General Plain Algebra of Biquaternions*, and the statement is cited from there.

**Remark (the minimal left ideals are the column spaces).** The standard minimal left ideal of $M_2(\mathbb{C})$ is the column space

$$
M_2(\mathbb{C}) E_{11} = \left\{ \begin{pmatrix} \alpha & 0 \\ \beta & 0 \end{pmatrix} : \alpha, \beta \in \mathbb{C} \right\},
$$

which is $V$ by the map $\begin{pmatrix} \alpha & 0 \\ \beta & 0 \end{pmatrix} \mapsto \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$. Under the inverse of $\mathsf{M}_2$ this is the minimal left ideal $\mathbb{B} \tilde\Pi_1$ of $\mathbb{B}$, where

$$
\tilde\Pi_1 = \tfrac{1}{2}(e_0 + i e_3), \qquad \mathsf{M}_2(\tilde\Pi_1) = E_{11},
$$

and the complementary ideal is $\mathbb{B} \tilde\Pi_2$ with $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - i e_3)$ and $\mathsf{M}_2(\tilde\Pi_2) = E_{22}$. The two ideals are isomorphic as left modules and satisfy $\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2$. The idempotents and the resulting Peirce decomposition are the subject of *Biquaternion Ideals and Peirce Decomposition* and are cited here only for the identification of $V$ with $\mathbb{B}\tilde\Pi_1$.

**Remark (the endomorphism algebra).** Two facts complete the picture of $V$. First, the commutant is one-dimensional, $\operatorname{End}_{\mathbb{B}}(V) = \mathbb{C}\,\mathrm{id}$, so $V$ is absolutely irreducible; this is Schur's lemma, and the element of $\operatorname{End}_{\mathbb{B}}(V)$ is the scalar action $\lambda v$, the diagonal copy of $\mathbb{C}$ in $M_2(\mathbb{C})$. Second, the double centralizer theorem gives $\mathbb{B} = \operatorname{End}_{\mathbb{C}}(V)$: the algebra is not merely contained in the endomorphisms of $V$, it is all of them. Both statements are proved in *Modules over the General Plain Algebra of Biquaternions*, where the module is exhibited with the matrix units and shown to reconstruct the algebra; that article writes the simple module $S$ and reads the regular module as $S \oplus S$, so its $S$ is the module called $V$ here. The reading of $V$ as a pair of chiral spinors with their dual and conjugate is the subject of *Biquaternion Spin Geometry*, which also writes the module $S$.

**Remark (the underlying real space).** Regarded over $\mathbb{R}$ by restriction of scalars, $V$ becomes a real vector space

$$
S = \operatorname{Res}_{\mathbb{C}/\mathbb{R}} V, \qquad \dim_{\mathbb{R}} S = 2 \dim_{\mathbb{C}} V = 4 .
$$

The real dimension of $S$ is four, and the left action of the eight-dimensional real algebra $\mathbb{B}$ on it is the restriction of the complex-linear action; the real structure carried by $S$ is treated in *Biquaternion Ideals and Peirce Decomposition*, §*The Real Structure*. The letter $S$ names the realification here, not the simple module: this article writes the simple module $V$, and *Modules over the General Plain Algebra of Biquaternions* writes it $S$.

## Matrix Units, the One-Sided Ideals, and the Projective Line

The four matrix units are realized by the two standard idempotents together with two off-diagonal elements,

$$
E_{11} = \mathsf{M}_2(\tilde\Pi_1) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad
E_{22} = \mathsf{M}_2(\tilde\Pi_2) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix},
$$
$$
E_{12} = \mathsf{M}_2(\tilde U), \qquad E_{21} = \mathsf{M}_2(\tilde S), \qquad
\tilde U = \frac{i e_1 - e_2}{2}, \qquad \tilde S = \frac{i e_1 + e_2}{2},
$$

so that $\{\tilde\Pi_1, \tilde U, \tilde S, \tilde\Pi_2\}$ is a $\mathbb{C}$-basis of $\mathbb{B}$ and the multiplication is the table of the matrix units,

$$
\tilde\Pi_1\tilde U = \tilde U = \tilde U\tilde\Pi_2, \qquad \tilde\Pi_2\tilde S = \tilde S = \tilde S\tilde\Pi_1, \qquad \tilde U\tilde S = \tilde\Pi_1, \qquad \tilde S\tilde U = \tilde\Pi_2,
$$

together with $\tilde U\tilde\Pi_1 = \tilde\Pi_2\tilde U = \tilde\Pi_1\tilde S = 0$, $\tilde S\tilde\Pi_2 = 0$, and $\tilde U^2 = \tilde S^2 = 0$.

The matrix units group the basis into one-sided ideals. The two **left ideals** $\mathbb{B}\tilde\Pi_1, \mathbb{B}\tilde\Pi_2$ are the column spaces and the two **right ideals** $\tilde\Pi_1\mathbb{B}, \tilde\Pi_2\mathbb{B}$ are the row spaces, and

$$
\mathbb{B} = \mathbb{B}\tilde\Pi_1 \oplus \mathbb{B}\tilde\Pi_2 = (\mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde S) \oplus (\mathbb{C}\tilde U \oplus \mathbb{C}\tilde\Pi_2),
$$
$$
\mathbb{B} = \tilde\Pi_1\mathbb{B} \oplus \tilde\Pi_2\mathbb{B} = (\mathbb{C}\tilde\Pi_1 \oplus \mathbb{C}\tilde U) \oplus (\mathbb{C}\tilde S \oplus \mathbb{C}\tilde\Pi_2).
$$

The two groupings of the same four basis elements differ: the Peirce decomposition groups $\tilde\Pi_1$ with $\tilde U$ and $\tilde\Pi_2$ with $\tilde S$, whereas the left-ideal decomposition groups $\tilde\Pi_1$ with $\tilde S$ and $\tilde\Pi_2$ with $\tilde U$. Each left ideal is two-dimensional over $\mathbb{C}$ and isomorphic to the simple module $V$; each right ideal is isomorphic to the dual $V^{*}$.

The minimal left ideals are parametrized by the projective line. For a $\mathbb{C}$-subspace $W \subseteq V = \mathbb{C}^2$ put

$$
L_W = \{\, M \in M_2(\mathbb{C}) : M|_W = 0 \,\},
$$

the matrices annihilating $W$; this is a left ideal, since $\ker(AM) \supseteq \ker M$ for every $A$, and $W \mapsto L_W$ reverses inclusions. One has $L_0 = \mathbb{B}$, $L_{\mathbb{C}^2} = 0$, and $L_W$ is minimal exactly when $\dim_{\mathbb{C}} W = 1$. Conversely every left ideal arises this way, because a left ideal is a submodule of the regular module $\mathbb{B} \cong V \oplus V$, and the only submodules of $V \oplus V$ are $0$, a copy of $V$, and the whole module. So the left ideals of $\mathbb{B}$ are exactly $0$, the whole algebra, and the minimal ideals $L_W$ indexed by the projective line

$$
\mathbb{P}^1(\mathbb{C}) = \{\, W \subseteq \mathbb{C}^2 : W \text{ a one-dimensional } \mathbb{C}\text{-subspace} \,\},
$$

which form the middle layer of the lattice; they are pairwise incomparable, and because the regular module has length two each is maximal as well as minimal. Right ideals admit the same description, with lines in the dual space and the rows as coordinate members.

## Structural Consequences of the Isomorphism

The matrix realization places the structure of $\mathbb{B}$ in view, and the consequences below are the ones the rest of the corpus uses.

**Theorem (simple, central, with prescribed centre).** The algebra $\mathbb{B}$ is simple; its centre is the scalar subspace $\mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$, isomorphic to $\mathbb{C}$; and $\mathbb{B}$ is central simple over $\mathbb{C}$.

**Proof.** Simplicity and the centre are the two corollaries after the isomorphism theorem of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*. Central simple means simple with centre exactly the base field, and the centre is $\mathbb{C} e_0 \cong \mathbb{C}$.

**Theorem (endomorphism algebra).** The isomorphism $\mathsf{M}_2$ identifies $\mathbb{B}$ with the endomorphism algebra of the two-dimensional complex space $V$, so that $\mathbb{B} = \operatorname{End}_{\mathbb{C}}(V)$ under the identification.

**Proof.** The algebra $M_2(\mathbb{C})$ is by definition the algebra of $\mathbb{C}$-linear endomorphisms of $\mathbb{C}^2$, and $\mathsf{M}_2$ is an isomorphism onto $M_2(\mathbb{C})$.

**Corollary (zero divisors).** The zero divisors of $\mathbb{B}$ are exactly the nonzero elements $\tilde{Q}$ with $\det \mathsf{M}_2(\tilde{Q}) = N(\tilde{Q}) = 0$, that is, the nonzero elements whose matrix is singular. In matrix terms they are the elements of rank one, and they form the nonzero part of the determinantal variety $\det = 0$.

**Proof.** A nonzero matrix over a field is singular exactly when it is a zero divisor in the matrix algebra, and rank is one for the nonzero singular $2 \times 2$ matrices. The identification with the vanishing of the determinant $N$ is the determinant statement of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*.

Taken together, the three statements say that $\mathbb{B}$ is the full endomorphism algebra of a two-dimensional complex space, and that all of its one-sided ideal structure and all of its degeneracies are the corresponding structure of $M_2(\mathbb{C})$ transported along a fixed linear isomorphism. The classification of the conjugations, the trace and the determinant, and the module $V$ are the parts of that transport that the companion articles use.

## Summary

The matrix realization $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* identifies $\mathbb{B}$ with $M_2(\mathbb{C})$, with trace $2Q_0$ and determinant $N(\tilde{Q})$; on that identification the present article develops the element theory. A nonzero null element, $N(\tilde{Q}) = 0$, is a singular matrix and hence a rank-one outer product $\mathsf{M}_2(\tilde{Q}) = uv^{T}$. The characteristic polynomial is $\lambda^2 - 2Q_0\lambda + N(\tilde{Q})$ and the Cayley–Hamilton identity is $\tilde{Q}^2 - 2Q_0\tilde{Q} + N(\tilde{Q})e_0 = 0$, so every power reduces to a combination of $e_0$ and $\tilde{Q}$. Quaternion conjugation is the adjugate, Hermitian conjugation is the conjugate transpose, and complex conjugation is **not** entrywise: it is dressed with the antisymmetric matrix $\epsilon = i\sigma_2 = \mathsf{M}_2(-e_2)$, as $\mathsf{M}_2(\bar{\tilde{Q}}) = \epsilon(\mathsf{M}_2(\tilde{Q}))^{\natural}\epsilon^{-1}$. The remarkable subspaces are the scalar, traceless, quaternionic, anti-quaternionic, Hermitian and anti-Hermitian matrices. The algebra is simple with centre the scalar matrices and is the full endomorphism algebra of the simple module $V = \mathbb{C}^2$ of complex dimension $2$, on which it acts by matrix multiplication; the minimal left ideals are the column spaces, and $V$ is the only simple module. The two dimensions $2$ of the module and $2$ of the matrix are the same two, because the algebra is the endomorphism algebra of the module.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra |
| $e_0, e_1, e_2, e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ | Developed form, $Q_\mu \in \mathbb{C}$ |
| $Q^\mu = (Q^0, Q^1, Q^2, Q^3)$ | Four-vector of *The Four-Vector Element Representation of Biquaternions* |
| $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ | Matrix realization of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, $\mathsf{M}_2(e_0) = I$, $\mathsf{M}_2(e_k) = -i\sigma_k$ |
| $\sigma_1, \sigma_2, \sigma_3$ | Pauli matrices, a shorthand for the images of $e_1, e_2, e_3$ |
| $N(\tilde{Q}) = \det \mathsf{M}_2(\tilde{Q}) = \sum_\mu Q_\mu^2$ | The determinant of the matrix, the norm |
| $\mathsf{M}_2(\tilde{Q}) = uv^{T}$ | Rank-one form of a nonzero null element, $N(\tilde{Q}) = 0$; the columns $u = (\alpha,\beta)^{T}$ and $v = (\gamma,\delta)^{T}$ are nonzero and determined up to $(\lambda u,\lambda^{-1}v)$ |
| $\epsilon = i\sigma_2 = \mathsf{M}_2(-e_2)$ | Antisymmetric matrix, $\mathsf{M}_2(\bar{\tilde{Q}}) = \epsilon(\mathsf{M}_2(\tilde{Q}))^{\natural}\epsilon^{-1}$ |
| $\operatorname{Tr}\mathsf{M}_2(\tilde{Q}) = 2Q_0$ | Trace of the matrix realization |
| $\operatorname{spec}\tilde{Q} = \{Q_0 \pm iB\}$ | Spectrum, the eigenvalues of $\mathsf{M}_2(\tilde{Q})$, $B = \sqrt{Q_1^2 + Q_2^2 + Q_3^2}$ |
| $H_2(\mathbb{C})$ | Hermitian $2 \times 2$ matrices, the image of $\mathbb{M}_+$ under $\mathsf{M}_2$ |
| $\mathrm{SL}(2,\mathbb{C})$ | Traceless matrices, the image $\mathsf{M}_2(\mathrm{Vect}(\mathbb{B}))$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | Quaternion, complex, Hermitian and anti-Hermitian conjugations |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B}), \mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}, \mathbb{M}_+, \mathbb{M}_-$ | The remarkable subspaces |
| $V = \mathbb{C}^2$ | Simple left $\mathbb{B}$-module, complex dimension $2$ |
| $S = \operatorname{Res}_{\mathbb{C}/\mathbb{R}} V$ | Restriction of scalars, real dimension $4$ |
| $\tilde\Pi_1 = \tfrac{1}{2}(e_0 + ie_3)$, $\tilde\Pi_2 = \tfrac{1}{2}(e_0 - ie_3)$ | Orthogonal idempotents, $\mathsf{M}_2(\tilde\Pi_1) = E_{11}$, $\mathsf{M}_2(\tilde\Pi_2) = E_{22}$ |
| $E_{ij}$ | Matrix units, $E_{ij}E_{kl} = \delta_{jk}E_{il}$ |
| $\operatorname{End}_{\mathbb{C}}(V) \cong M_2(\mathbb{C})$ | Endomorphism algebra identified with $\mathbb{B}$ |

## Further Reading

- *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the map, the isomorphism, the trace and the determinant, and the remarkable subspace conditions

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the structure of the full matrix algebra, its centre, its simplicity and its idempotents.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the simple modules of a semisimple algebra and the classification of minimal left ideals.
- William Fulton and Joe Harris, *Representation Theory: A First Course*, Graduate Texts in Mathematics 129 (Springer, 1991), for Schur's lemma, the double centralizer theorem and the modules of a matrix algebra.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the relation between quaternion algebras, their complexification and the matrix algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the matrix realizations of the complexified quaternions.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the explicit matrix model of the biquaternions and its invariants.
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-element-representation.md`), the first of the four articles reading the four forms on the $2\times2$ matrix, each with the structure attached to its form.
- *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* (`articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.md`), for the remarkable subspaces read in this model and in the regular one at once, and for the block-diagonal bridge between them
