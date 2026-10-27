# __$M_2(\mathbb{R})$ Model : The Conjugations and the Adjoints__

## Introduction

The split-quaternion algebra carries three distinguished involutions: the conjugation, the principal involution and the reversal. Under the defining isomorphism they become three familiar operations on $2\times2$ matrices: the adjugate, the conjugation by a diagonal sign matrix, and the transpose twisted by a fixed symmetric matrix. The algebra also carries two natural bilinear forms, the polar form of the determinant and the trace form, and the involutions are the adjoint involutions of those forms.

This article proves the matrix identities, identifies the two forms and their signatures, and computes the adjoints of left and right multiplication for both. The result is the matrix explanation of the three involutions: the conjugation is the adjugate, the principal involution is inner, and the transpose is the fourth anti-involution, the one attached to the positive definite trace form rather than to the determinant.

The involutions themselves are *Split-Quaternion Subspaces and the Involutions* and *Split-Quaternion Involution Lattice*; the trace and the determinant are *Split-Quaternion Matrix Element Representations*; the sandwich action is *$M_2(\mathbb{R})$ Model : The Sandwich and the Adjoint Action*.

## The Three Involutions in the Model

**Theorem (the matrix identities).** For every $\tilde q$ with $M=\mathsf{M}_2(\tilde q)$,

$$
\mathsf{M}_2(\tilde q^{\natural})=\operatorname{adj}M, \qquad
\mathsf{M}_2(\alpha(\tilde q))=\Sigma M\Sigma^{-1}, \qquad
\mathsf{M}_2(\rho(\tilde q))=W M^{\mathsf T}W,
$$

where

$$
\Sigma=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=-D, \qquad W=\begin{pmatrix}0&1\\1&0\end{pmatrix}=K.
$$

**Proof.** Let $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $a=q_t-q_z$, $b=q_y-q_x$, $c=q_x+q_y$ and $d=q_t+q_z$. The adjugate is $\operatorname{adj}M=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$, and the dictionary gives $d=q_t+q_z$, $-b=q_x-q_y$, $-c=-(q_x+q_y)$ and $a=q_t-q_z$; this is the matrix of $q_t-q_x\vec e_x-q_y\vec e_y-q_z\vec e_z$, which is $\tilde q^{\natural}$.

For the principal involution, $\Sigma M\Sigma^{-1}=\Sigma M\Sigma$ changes the signs of $b$ and $c$ and leaves $a$ and $d$ fixed. The entries $b'=-b=q_x-q_y$ and $c'=-c=-(q_x+q_y)$ are those of $\alpha(\tilde q)=(q_t,-q_x,-q_y,q_z)$, while $a$ and $d$ are unchanged because $\alpha$ fixes $q_t$ and $q_z$.

For the reversal, $W M^{\mathsf T}W$ exchanges $a\leftrightarrow d$ and leaves $b$ and $c$ fixed, since $W M^{\mathsf T}W=\begin{pmatrix}d&b\\c&a\end{pmatrix}$. Those are the entries of $\rho(\tilde q)=(q_t,q_x,q_y,-q_z)$.

**Corollary (the coordinate sign patterns).** The four involutions act on the coordinates by

| involution | $q_t$ | $q_x$ | $q_y$ | $q_z$ | matrix formula | type |
|---|---|---|---|---|---|---|
| identity | $+$ | $+$ | $+$ | $+$ | $M$ | automorphism |
| ${}^{\natural}$ | $+$ | $-$ | $-$ | $-$ | $\operatorname{adj}M$ | anti-automorphism |
| $\alpha$ | $+$ | $-$ | $-$ | $+$ | $\Sigma M\Sigma^{-1}$ | automorphism |
| $\rho$ | $+$ | $+$ | $+$ | $-$ | $WM^{\mathsf T}W$ | anti-automorphism |
| $\tau$ | $+$ | $-$ | $+$ | $+$ | $M^{\mathsf T}$ | anti-automorphism |

**Proof.** The first four rows are the theorem and the definitions. The last row is the transpose, computed from the dictionary: transposing $M$ exchanges $b$ and $c$, which gives $q_x\mapsto-q_x$ and leaves $q_y$ and $q_z$, since $c-b$ changes sign while $b+c$ and the diagonal entries do not.

**Proposition (the Klein group).** The three structural involutions satisfy

$$
\tilde q^{\natural}=\alpha(\rho(\tilde q))=\rho(\alpha(\tilde q)), \qquad \alpha^2=\rho^2=\operatorname{id}, \qquad (\tilde q^{\natural})^{\natural}=\tilde q, \qquad \alpha\rho=\rho\alpha,
$$

so that $\{\operatorname{id},\alpha,\rho,{}^{\natural}\}$ is a Klein four-group. The principal involution is inner, $\alpha=\operatorname{Int}_{\vec e_z}$, and the conjugation and the reversal are the two anti-automorphisms of the group.

**Proof.** The composition relations are checked on the generators in *Split-Quaternion Subspaces and the Involutions*. For the inner statement, $\Sigma=-D=-\mathsf{M}_2(\vec e_z)$, and conjugation by $-\vec e_z$ is the same automorphism as conjugation by $\vec e_z$, since the two signs cancel. By the theorem this automorphism is $\alpha$.

**Corollary (the transpose is a fourth anti-involution).** The transpose $\tau$ satisfies $\tau^2=\operatorname{id}$ and $\tau(\tilde p\tilde q)=\tau(\tilde q)\tau(\tilde p)$, and it is not one of the three structural involutions. In the algebra it is

$$
\tau(q_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z)=q_t e_t-q_x\vec e_x+q_y\vec e_y+q_z\vec e_z,
$$

and it is the composite $\tau=\operatorname{Int}_{\vec e_x}\circ{}^{\natural}$, where $\operatorname{Int}_{\vec e_x}$ negates $q_y$ and $q_z$.

**Proof.** The transpose of a product reverses the order, and transposing twice is the identity. The coordinate form is the last row of the table. For the composite, conjugation by $\vec e_x$ sends $\vec e_x\mapsto\vec e_x$, $\vec e_y\mapsto-\vec e_y$ and $\vec e_z\mapsto-\vec e_z$, so it sends $(q_t,-q_x,-q_y,-q_z)$ to $(q_t,-q_x,q_y,q_z)$.

**Remark (why four and not three).** The three structural involutions are those attached to the algebra: the conjugation, the principal automorphism and the reversal. The transpose is attached to the model: it is the Euclidean adjoint, and it depends on the Euclidean structure of $\mathbb{R}^2$, not on the algebra alone. It is nevertheless an anti-automorphism, because the transpose of a product reverses the order in every basis.

## The Two Bilinear Forms

**Definition.** The **determinant form** and the **trace form** on $M_2(\mathbb{R})$ are

$$
B_{\det}(X,Y)=\tfrac12\operatorname{tr}\bigl(\operatorname{adj}(X)\,Y\bigr), \qquad
B_{\operatorname{tr}}(X,Y)=\operatorname{tr}(X^{\mathsf T}Y).
$$

**Proposition (the determinant form is the polar form of the determinant).** For all $X,Y$,

$$
B_{\det}(X,Y)=\tfrac12\bigl(\det(X+Y)-\det X-\det Y\bigr),
$$

and in the split-quaternion coordinates

$$
B_{\det}(\tilde p,\tilde q)=p_tq_t+p_xq_x-p_yq_y-p_zq_z.
$$

Its matrix in the basis $1,\vec e_x,\vec e_y,\vec e_z$ is $\operatorname{diag}(1,1,-1,-1)$, of signature $(2,2)$.

**Proof.** In entries, $\operatorname{tr}(\operatorname{adj}(X)Y)=ad'+a'd-bc'-b'c$, which is the polar form of $ad-bc$. The coordinate expression is the polar form of the norm computed in *$M_2(\mathbb{R})$ Model : Rank-One Matrices and the Null Cone*.

**Proposition (the trace form is positive definite).** In entries,

$$
B_{\operatorname{tr}}(X,Y)=aa'+bb'+cc'+dd',
$$

and in the split-quaternion coordinates its matrix in the basis $1,\vec e_x,\vec e_y,\vec e_z$ is $2I$, of signature $(4,0)$.

**Proof.** The entry formula is the definition. The basis is orthogonal for the trace form: $\operatorname{tr}(I^{\mathsf T}I)=2$ and $\operatorname{tr}(J^{\mathsf T}J)=\operatorname{tr}(K^{\mathsf T}K)=\operatorname{tr}(D^{\mathsf T}D)=2$, while the cross traces vanish because the product of two distinct basis matrices is traceless.

The two forms are different objects. The determinant form is indefinite and is the polar form of the split-quaternion norm; the trace form is positive definite and is the Euclidean form of the matrix space. The next theorem shows that each has its own adjoint involution.

## The Adjoints of Left and Right Multiplication

**Definition.** For a bilinear form $B$ and an operator $T$, the **adjoint** $T^*$ is defined by $B(TX,Y)=B(X,T^*Y)$ for all $X,Y$.

**Theorem (the adjoints for the determinant form).** For the determinant form,

$$
L_X^*=L_{\operatorname{adj}X}, \qquad R_X^*=R_{\operatorname{adj}X},
$$

where $L_X(Y)=XY$ and $R_X(Y)=YX$.

**Proof.** The adjugate is multiplicative in the reversed order, $\operatorname{adj}(XY)=\operatorname{adj}(Y)\operatorname{adj}(X)$. Hence

$$
B_{\det}(XY,Z)=\tfrac12\operatorname{tr}\bigl(\operatorname{adj}(Y)\operatorname{adj}(X)Z\bigr)=B_{\det}\bigl(Y,\operatorname{adj}(X)Z\bigr),
$$

which is the first identity. The second is the same computation with the order of the factors exchanged, using $\operatorname{adj}(YX)=\operatorname{adj}(X)\operatorname{adj}(Y)$.

**Theorem (the adjoints for the trace form).** For the trace form,

$$
L_X^*=L_{X^{\mathsf T}}, \qquad R_X^*=R_{X^{\mathsf T}}.
$$

**Proof.** Since $\operatorname{tr}((XY)^{\mathsf T}Z)=\operatorname{tr}(Y^{\mathsf T}X^{\mathsf T}Z)=\operatorname{tr}(Y^{\mathsf T}(X^{\mathsf T}Z))$, the left multiplication by $X$ has adjoint the left multiplication by $X^{\mathsf T}$. The right case is analogous.

**Corollary (the adjoint involutions).** The conjugation ${}^{\natural}$ is the adjoint involution of the determinant form, and the transpose $\tau$ is the adjoint involution of the trace form:

$$
B_{\det}(\tilde p X,\tilde q)=B_{\det}(X,\tilde p^{\natural}\tilde q), \qquad
B_{\operatorname{tr}}(X,Y)=B_{\operatorname{tr}}(X^{\mathsf T},Y^{\mathsf T}).
$$

**Proof.** The first identity is the theorem with $\operatorname{adj}\mathsf{M}_2(\tilde p)=\mathsf{M}_2(\tilde p^{\natural})$. The second is the symmetry of the trace form under transposition.

**Corollary (the self-adjoint and skew-adjoint subspaces).** For the determinant form, the self-adjoint elements are the scalars and the skew-adjoint elements are the traceless matrices:

$$
\{X : L_X^*=L_X\}=S, \qquad \{X : L_X^*=-L_X\}=V.
$$

For the trace form, the self-adjoint elements are the symmetric matrices and the skew-adjoint elements are the line $\mathbb{R}J$:

$$
\{X : X^{\mathsf T}=X\}=\operatorname{span}\{1,\vec e_y,\vec e_z\}, \qquad
\{X : X^{\mathsf T}=-X\}=\mathbb{R}\vec e_x.
$$

**Proof.** For the determinant form, $\operatorname{adj}X=X$ forces $X$ to be scalar, and $\operatorname{adj}X=-X$ forces $\operatorname{tr}X=0$. For the trace form, the conditions are symmetry and skew-symmetry, and the symmetric and skew-symmetric subspaces are computed in *$M_2(\mathbb{R})$ Model : The Subspaces as Matrix Conditions*.

## The Killing Form of the Traceless Part

**Proposition (the Killing form).** On the Lie algebra $\mathfrak{sl}_2(\mathbb{R})=V$ the Killing form is

$$
B_{\mathrm{K}}(X,Y)=4\operatorname{tr}(XY),
$$

and it has signature $(2,1)$. It is not the trace form $B_{\operatorname{tr}}(X,Y)=\operatorname{tr}(X^{\mathsf T}Y)$ of the article: the two agree when $X$ is symmetric and differ by a sign when $X$ is skew.

**Proof.** For $\mathfrak{sl}_n$ the Killing form is $2n\operatorname{tr}(XY)$, which is $4\operatorname{tr}(XY)$ for $n=2$. For $X=\begin{pmatrix}a&b\\c&-a\end{pmatrix}$ one has $\operatorname{tr}(X^2)=2a^2+2bc$, and in the coordinates $u=b+c$ and $v=b-c$ this is $2a^2+\tfrac12(u^2-v^2)$, of signature $(2,1)$. The comparison with $B_{\operatorname{tr}}$ follows from $X^{\mathsf T}=X$ on symmetric matrices and $X^{\mathsf T}=-X$ on skew ones.

The Killing form is indefinite on $V$, while the trace form is positive definite on the whole algebra; the two forms coincide on the symmetric part and differ by a sign on the skew part. The determinant form restricted to $V$ has signature $(2,1)$ as well, since $\operatorname{diag}(1,1,-1,-1)$ restricts to the three last coordinates with signs $(+,-,-)$.

## Summary

The conjugation is the adjugate, the principal involution is conjugation by the diagonal matrix $D=\mathsf{M}_2(\vec e_z)$, and the reversal is the transpose twisted by $K=\mathsf{M}_2(\vec e_y)$. The three form a Klein four-group with the identity, and the transpose is a fourth anti-involution, $\tau=\operatorname{Int}_{\vec e_x}\circ{}^{\natural}$, which is not one of the three structural ones.

The algebra carries two natural forms: the determinant form $B_{\det}(X,Y)=\tfrac12\operatorname{tr}(\operatorname{adj}X\,Y)$, of signature $(2,2)$, whose adjoint involution is the conjugation, and the trace form $B_{\operatorname{tr}}(X,Y)=\operatorname{tr}(X^{\mathsf T}Y)$, of signature $(4,0)$, whose adjoint involution is the transpose. For the determinant form the self-adjoint elements are the scalars and the skew-adjoint elements the traceless matrices; for the trace form they are the symmetric matrices and the line $\mathbb{R}\vec e_x$. The Killing form of the traceless part is four times the bilinear form $\operatorname{tr}(XY)$, not the trace form, and it has signature $(2,1)$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| ${}^{\natural},\alpha,\rho$ | the conjugation, the principal involution, the reversal | *Split-Quaternion Subspaces and the Involutions* |
| $\tau$ | the transpose, a fourth anti-involution | this article |
| $\operatorname{adj}$ | the adjugate, $\operatorname{adj}M=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ | this article |
| $\Sigma,W$ | $\operatorname{diag}(1,-1)=-D$ and $K=\mathsf{M}_2(\vec e_y)$ | *Split-Quaternion Matrix Element Representations* |
| $B_{\det}$ | the determinant form, signature $(2,2)$ | this article |
| $B_{\operatorname{tr}}$ | the trace form, signature $(4,0)$ | this article |
| $L_X,R_X$ | left and right multiplication by $X$ | this article |
| $B_{\mathrm{K}}$ | the Killing form of $\mathfrak{sl}_2(\mathbb{R})$ | *Split-Quaternion Algebra* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the adjugate, the trace form and the involutions of a matrix algebra.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the two forms and the involutions of $\mathrm{Cl}_{1,1}$.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the Killing form of $\mathfrak{sl}_2$ and its signature.
