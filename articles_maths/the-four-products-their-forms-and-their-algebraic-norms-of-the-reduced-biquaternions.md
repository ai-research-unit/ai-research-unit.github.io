# __The Four Products, Their Forms and Their Algebraic Norms__

## Introduction

The reduced biquaternion space carries **four** general products, and each carries a scalar-part form and an algebraic norm. The products are the **general plain bilinear product** $\breve Q_{1}\breve Q_{2}$, the **general tessarine bilinear product** $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$, the **general plain sesquilinear product** $\breve Q_{1}\breve Q_{2}^{*}$ and the **general tessarine sesquilinear product** $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$; the four scalar-part forms are written $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\mathrm{ts}}, \langle\cdot,\cdot\rangle_{\mathrm{ts}*}$, the forms of the pairs $(\mathrm{id},\mathrm{id})$, $(\mathrm{id},{}^{*})$, $({}_{\mathrm{ts}},\mathrm{id})$ and $({}_{\mathrm{ts}},{}^{*})$; and the algebraic norm of each is the diagonal of its form,
$$
\langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2},\qquad \langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2},\qquad \langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2},\qquad \langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}.
$$

This is the article of the **definition of the four products and of the four algebraic norms**, following *The Four Products of the Biquaternion $\mathbb{C}$ Space*, *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* of the biquaternion category. The clause that decides which product is which is the **slot**: the first slot carries either the identity or the tessarine sign, the second either the identity or the star, and the two choices give the four. The forms are recorded with their Gram matrices and their signatures; the norms with their fields of values; the relations between the products are recorded; and the products are compared.

**The results.** The general plain bilinear product is the **multiplication** of the algebra; it is the only **associative** one and the only **commutative** one, its form is $\mathbb{C}$-bilinear and symmetric and its norm $\langle\cdot\rangle$ is complex-valued, indefinite of real signature $(2,2)$, and **not multiplicative**. The general tessarine bilinear product has the same bilinearity and symmetry but is neither associative nor commutative; its norm $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ is complex-valued, indefinite of real signature $(2,2)$, and it is the **multiplicative** one, $\langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}$, the **reduced norm** of the algebra and its **invertibility criterion**. The general plain sesquilinear product is $\mathbb{C}$-linear in the first variable and $\mathbb{C}$-antilinear in the second, Hermitian, and its norm $\langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$ is real-valued, indefinite of real signature $(2,2)$ and not multiplicative. The general tessarine sesquilinear product is Hermitian like the former, and its norm $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$ is real-valued and **positive definite**, of real signature $(4,0)$, the **topological norm** of the space.

**The one warning of this article.** An **algebraic norm** is an element of the algebra — a complex number here for $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\mathrm{ts}}$, a real number for $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\mathrm{ts}*}$ — and it is the diagonal of the scalar-part form of a product; it is **not** the positive real that the word *norm* means in topology and analysis. Only $\langle\cdot\rangle_{\mathrm{ts}*}$ is positive definite, so only $\langle\cdot\rangle_{\mathrm{ts}*}$ is a topological norm (squared). The two uses of the word are never conflated, and *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, below this article, reads the algebraic norm of the multiplication against the criterion of invertibility.

## The Four General Products

**Each product has a coordinate table in the two complex coordinates $Q_{1\blacktriangle}$ and $Q_{1\blacktriangledown}$, read off from the relations $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$ and the four maps of the involutions.**

**Definition.** For $\breve Q_{1}=Q_{1\blacktriangle}+jQ_{1\blacktriangledown}$ and $\breve Q_{2}=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$, the four general products are
$$
\breve Q_{1}\breve Q_{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j,
$$
$$
\breve Q_{1,\mathrm{ts}}\breve Q_{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle})j,
$$
$$
\breve Q_{1}\breve Q_{2}^{*}=(Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown})+(Q_{1\blacktriangledown}\bar Q_{2\blacktriangle}-Q_{1\blacktriangle}\bar Q_{2\blacktriangledown})j,
$$
$$
\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}=(Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown})-(Q_{1\blacktriangle}\bar Q_{2\blacktriangledown}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangle})j,
$$
where the first slot carries $\mathrm{id}$ in the first and third and ${}_{\mathrm{ts}}$ in the second and fourth, and the second slot carries $\mathrm{id}$ in the first and second and ${}^{*}$ in the third and fourth. The scalar part of each is the **general plain bilinear**, the **general tessarine bilinear**, the **general plain sesquilinear** and the **general tessarine sesquilinear form** respectively.

**Proposition (the tables of the plain products).** The general plain bilinear product is the multiplication of the algebra, since ${}_{\mathrm{ts}}$ appears in neither slot; its table is the multiplication table of *Reduced Biquaternion Space*, and its scalar part and $j$-part are $Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ and $Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle}$.

*Proof.* With $\breve Q_{1}=Q_{1\blacktriangle}+jQ_{1\blacktriangledown}$ and $\breve Q_{2}=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$, $\breve Q_{1}\breve Q_{2}=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangle}Q_{2\blacktriangledown}j+Q_{1\blacktriangledown}Q_{2\blacktriangle}j+Q_{1\blacktriangledown}Q_{2\blacktriangledown}j^{2}$, and $j^{2}=+1$ gives the display. This is the product of the algebra and nothing else.

**Proposition (the tables of the tessarine products).** The tessarine sign in the first slot replaces $\breve Q_{1}$ by $\breve Q_{1,\mathrm{ts}}=Q_{1\blacktriangle}-jQ_{1\blacktriangledown}$; in the two tessarine products the coefficients $Q_{1\blacktriangledown}$ and $Q_{2\blacktriangledown}$ therefore change sign, and the tables are the second and fourth displays above.

*Proof.* $\breve Q_{1,\mathrm{ts}}\breve Q_{2}=(Q_{1\blacktriangle}-jQ_{1\blacktriangledown})(Q_{2\blacktriangle}+jQ_{2\blacktriangledown})=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangle}Q_{2\blacktriangledown}j-Q_{1\blacktriangledown}Q_{2\blacktriangle}j-Q_{1\blacktriangledown}Q_{2\blacktriangledown}j^{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle})j$, using $j^{2}=+1$; the same computation with $\breve Q_{2}$ replaced by $\breve Q_{2}^{*}$ gives the fourth display, and the third follows from the second by conjugating the coefficients of $\breve Q_{2}$ and using $Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}+\bar Q_{1\blacktriangledown}Q_{2\blacktriangledown}=2\operatorname{Re}(Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown})$, which is the source of the identity $\breve Q_{1}\breve Q_{2}^{*}=(Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown})+(Q_{1\blacktriangledown}\bar Q_{2\blacktriangle}-Q_{1\blacktriangle}\bar Q_{2\blacktriangledown})j$.

**Remark (the double-complex alternativity).** The four products are the double-complex analogue of the four products of the biquaternion category; the second slot's star is a **coefficient** conjugation, because the coefficients are complex, and the first slot's tessarine sign is the intrinsic conjugate of the algebra. The two categories carry the same four slot choices on different coordinates: the biquaternion element has the four complex coordinates $P_0,P_1,P_2,P_3$ and its products carry a cross-product term, while the reduced biquaternion element has the two coordinates $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$, so its $j$-part is one-dimensional over $\mathbb{C}$ and no cross-product term appears.

## The Scalar-Part Forms

**The scalar-part form of a product is $\mathrm{Sc}$ applied to the product, and the four forms are $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\mathrm{ts}}, \langle\cdot,\cdot\rangle_{\mathrm{ts}*}$.**

**Definition.** The **scalar-part form** of a product $\star$ is
$$
\mathrm{Form}_\star(\breve Q_{1},\breve Q_{2})=\mathrm{Sc}(\breve Q_{1}\star \breve Q_{2}),
$$
where $\mathrm{Sc}$ is the coefficient of $1$. The four forms are
$$
\langle \breve Q_{1},\breve Q_{2}\rangle=\mathrm{Sc}(\breve Q_{1}\breve Q_{2})=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2})=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown},
$$
$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{*}=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*})=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}.
$$

**Theorem (bilinear against sesquilinear).** $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ are $\mathbb{C}$-**bilinear** and $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ are $\mathbb{C}$-**sesquilinear**, linear in the first variable and antilinear in the second; $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ are **symmetric**, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ are **Hermitian**,
$$
\langle \breve Q_{1},\breve Q_{2}\rangle=\langle \breve Q_{2},\breve Q_{1}\rangle,\quad \langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{2},\breve Q_{1}\rangle_{\mathrm{ts}},\quad \langle \breve Q_{2},\breve Q_{1}\rangle_{*}=\overline{\langle \breve Q_{1},\breve Q_{2}\rangle_{*}},\quad \langle \breve Q_{2},\breve Q_{1}\rangle_{\mathrm{ts}*}=\overline{\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}}.
$$

*Proof.* $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ are built from the bilinear products $\breve Q_{1}\breve Q_{2}$ and $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$, which have no conjugation, so they are bilinear; the tessarine sign is $\mathbb{C}$-linear and the star is $\mathbb{C}$-antilinear (*The Two Involutions and the Group of Involutions*), so $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ are linear in the first variable and antilinear in the second. Symmetry of $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ is the commutativity of the complex multiplication in the formulas $Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ and $Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown}$; Hermiticity of $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is $\overline{Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}}=\bar Q_{1\blacktriangle}Q_{2\blacktriangle}-\bar Q_{1\blacktriangledown}Q_{2\blacktriangledown}=Q_{2\blacktriangle}\bar Q_{1\blacktriangle}-Q_{2\blacktriangledown}\bar Q_{1\blacktriangledown}$, the same form with the arguments exchanged.

**Theorem (the Gram matrices).** On the complex basis $1,j$ and on the real basis $1,i,j,ij$ the forms have the Gram matrices
$$
\boxed{\; G_{B}=\operatorname{diag}(1,1),\qquad G_{N}=\operatorname{diag}(1,-1),\qquad G_{H}=\operatorname{diag}(1,-1),\qquad G_{K}=\operatorname{diag}(1,1) \;}
$$
over $\mathbb{C}$, and
$$
\operatorname{diag}(1,-1,1,-1),\quad \operatorname{diag}(1,-1,-1,1),\quad \operatorname{diag}(1,1,-1,-1),\quad \operatorname{diag}(1,1,1,1)
$$
over $\mathbb{R}$; the four forms are non-degenerate, and their signatures and fields of values are those of the table of §*The Four Algebraic Norms*.

*Proof.* The complex Gram entries are the scalar parts of the products of the basis with itself conjugated or not: $\langle 1,1\rangle=\langle j,j\rangle=1$, since $j^{2}=1$; $\langle 1,1\rangle_{\mathrm{ts}}=1$, $\langle j,j\rangle_{\mathrm{ts}}=\mathrm{Sc}(j_{\mathrm{ts}}j)=\mathrm{Sc}(-j^{2})=-1$; $\langle 1,1\rangle_{*}=1$, $\langle j,j\rangle_{*}=\mathrm{Sc}(jj^{*})=\mathrm{Sc}(-1)=-1$; $\langle 1,1\rangle_{\mathrm{ts}*}=1$, $\langle j,j\rangle_{\mathrm{ts}*}=\mathrm{Sc}(j_{\mathrm{ts}}j^{*})=\mathrm{Sc}((-j)(-j))=\mathrm{Sc}(j^{2})=1$. The real matrices are the same entries read on the real basis: $\langle i,i\rangle=\mathrm{Sc}(i^{2})=-1$ and $\langle ij,ij\rangle=\mathrm{Sc}((ij)^{2})=-1$, giving $\operatorname{diag}(1,-1,1,-1)$; and likewise for the others, using $i^{*}=-i$ and $(ij)^{*}=ij$. Non-degeneracy is the non-vanishing of every diagonal entry.

## The Four Algebraic Norms

**The algebraic norm of a product is the diagonal of its scalar-part form, and the four norms are $\langle\cdot\rangle, \langle\cdot\rangle_{\mathrm{ts}}, \langle\cdot\rangle_{*}, \langle\cdot\rangle_{\mathrm{ts}*}$ read on one argument.**

**Definition.** The **algebraic norm of a product** is the diagonal of its scalar-part form,
$$
\mathrm{Norm}_\star(\breve Q)=\mathrm{Form}_\star(\breve Q,\breve Q),
$$
one object with two arities: the form with two arguments and its diagonal with one. The four algebraic norms are
$$
\boxed{\; \langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2},\qquad \langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2},\qquad \langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2},\qquad \langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2} \;}.
$$

This is the definition of *Conventions in Mathematics*, §*The Conjugations*, and of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* of the biquaternion category. The two arities of each letter are one object and are never given two letters.

**Theorem (the four norms, their values and their signatures).** The four norms have the following fields of values, real signatures and definiteness:

| norm | product | formula | values | real signature | definite? | multiplicative? |
|---|---|---|---|---|---|---|
| $\langle\cdot\rangle$ | plain bilinear | $Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2}$ | $\mathbb{C}$ | $(2,2)$ | no | **no** |
| $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ | tessarine bilinear | $Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | $\mathbb{C}$ | $(2,2)$ | no | **yes** |
| $\langle\cdot,\cdot\rangle_{*}$ | plain sesquilinear | $\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}$ | $\mathbb{R}$ | $(2,2)$ | no | no |
| $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ | tessarine sesquilinear | $\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$ | $\mathbb{R}$ | $(4,0)$ | **yes**, positive | no |

*Proof.* In the real coordinates $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$,
$$
\langle \breve Q\rangle=q_{\blacktriangle}^{2}-(q'_{\blacktriangle})^{2}+q_{\blacktriangledown}^{2}-(q'_{\blacktriangledown})^{2}+2i(q_{\blacktriangle}q'_{\blacktriangle}+q_{\blacktriangledown}q'_{\blacktriangledown}),\qquad \langle \breve Q\rangle_{\mathrm{ts}}=q_{\blacktriangle}^{2}-(q'_{\blacktriangle})^{2}-q_{\blacktriangledown}^{2}+(q'_{\blacktriangledown})^{2}+2i(q_{\blacktriangle}q'_{\blacktriangle}-q_{\blacktriangledown}q'_{\blacktriangledown}),
$$
$$
\langle \breve Q\rangle_{*}=q_{\blacktriangle}^{2}+(q'_{\blacktriangle})^{2}-q_{\blacktriangledown}^{2}-(q'_{\blacktriangledown})^{2},\qquad \langle \breve Q\rangle_{\mathrm{ts}*}=q_{\blacktriangle}^{2}+(q'_{\blacktriangle})^{2}+q_{\blacktriangledown}^{2}+(q'_{\blacktriangledown})^{2}.
$$
$\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ take complex values in general, and their real parts are indefinite quadratic forms of signature $(2,2)$; $\langle\cdot,\cdot\rangle_{*}$ is a real indefinite form of signature $(2,2)$; $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is the sum of four squares, hence real, positive definite and of signature $(4,0)$. The definiteness column is read from the signs: only $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is one-signed. The multiplicativity column is proved in the next section and in §*The Comparison of the Four Products*.

**Corollary (the topological norm is $\langle\cdot\rangle_{\mathrm{ts}*}$).** The only positive-definite one of the four is $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$, which is the square of the Euclidean norm of the four real coordinates; it is the **topological norm** of the space, and the other three are algebraic norms only.

*Proof.* $\langle \breve Q\rangle_{\mathrm{ts}*}=q_{\blacktriangle}^{2}+(q'_{\blacktriangle})^{2}+q_{\blacktriangledown}^{2}+(q'_{\blacktriangledown})^{2}$ is the sum of the four squares of the real coordinates, and it vanishes exactly at $\breve Q=0$; the other three vanish on nonzero elements, $\langle \breve Q\rangle$ and $\langle \breve Q\rangle_{\mathrm{ts}}$ in the complex plane and $\langle \breve Q\rangle_{*}$ on the two real lines $|Q_{\blacktriangle}|^{2}=|Q_{\blacktriangledown}|^{2}$, so none of them is positive definite.

### The Multiplicative Norm

**The only multiplicative one of the four norms is $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$, and its multiplicativity is under the multiplication; it is the reduced norm of the algebra and its invertibility criterion.**

**Theorem (the tessarine bilinear norm is multiplicative).** For all $\breve Q_{1},\breve Q_{2}$,
$$
\boxed{\; \langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\,\langle \breve Q_{2}\rangle_{\mathrm{ts}},\qquad \langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown}) \;}.
$$

*Proof.* In the idempotent coordinates $\breve Q_{1}=Q_{1+}\Pi_++Q_{1-}\Pi_-$ and $\breve Q_{2}=Q_{2+}\Pi_++Q_{2-}\Pi_-$, the product is componentwise (*Reduced Biquaternion Space*), so $\breve Q_{1}\breve Q_{2}$ has coordinates $\bigl(Q_{1+}Q_{2+},Q_{1-}Q_{2-}\bigr)$; the norm $\langle\cdot\rangle_{\mathrm{ts}}$ is the product of the two coordinates, which is multiplicative in the coordinates:
$$
Q_{1+}Q_{2+}\cdot Q_{1-}Q_{2-}=\bigl(Q_{1+}Q_{1-}\bigr)\bigl(Q_{2+}Q_{2-}\bigr)=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}.
$$

**Corollary (the reduced norm and the criterion).** $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ is the determinant of the multiplication by $\breve Q$ in the two-dimensional idempotent coordinates, it is the **reduced norm** of the algebra, and
$$
\boxed{\; \breve Q\ \text{is invertible}\iff \langle \breve Q\rangle_{\mathrm{ts}}\neq0,\qquad \breve Q^{-1}=\frac{Q_{\blacktriangle}-Q_{\blacktriangledown}j}{Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}}=\frac{\breve Q_{\mathrm{ts}}}{\langle \breve Q\rangle_{\mathrm{ts}}} \;}.
$$

*Proof.* In the idempotent coordinates the multiplication by $\breve Q$ is $(U_1,U_2)\mapsto(Q_{+}U_1,Q_{-}U_2)$ with $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, so the determinant is $Q_{+}Q_{-}=\langle \breve Q\rangle_{\mathrm{ts}}$; it is nonzero exactly when both coordinates are nonzero, which is the criterion of *Reduced Biquaternion Space*. The inverse is verified by $\breve Q(Q_{\blacktriangle}-Q_{\blacktriangledown}j)=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\langle \breve Q\rangle_{\mathrm{ts}}$.

The three other norms are not multiplicative under their products. The failure of $\langle\cdot\rangle$ is exhibited in *Norm and Invertibility in the Algebra of the Reduced Biquaternions*: the pair $\Pi_+$, $\Pi_-$ separates the two sides, since $\Pi_+\Pi_-=0$ gives $\langle \Pi_+\Pi_-\rangle=0$ while $\langle \Pi_+\rangle\langle \Pi_-\rangle=\tfrac12\cdot\tfrac12=\tfrac14$. The norm $\langle\cdot\rangle_{\mathrm{ts}}$ is the reduced norm *and* the algebraic norm of the tessarine bilinear product, and the two roles coincide: it is the determinant of the multiplication in the idempotent coordinates and the diagonal of the tessarine bilinear form.

## Relations Between the Four Products

**The four products are linked by the idempotent coordinates and by the conjugate of a factor, and the links are recorded rather than used.**

**Theorem (the automorphism relations).** Each of the bar, the tessarine sign and the star commutes with the multiplication, so it moves a product to the product of the images; consequently the four products are the four ways of placing a conjugation in one or both slots, and
$$
\overline{\breve Q_{1}\breve Q_{2}}=\bar{\breve Q_{1}}\bar{\breve Q_{2}},\qquad (\breve Q_{1}\breve Q_{2})_{\mathrm{ts}}=\breve Q_{1,\mathrm{ts}}\breve Q_{2,\mathrm{ts}},\qquad (\breve Q_{1}\breve Q_{2})^{*}=\breve Q_{1}^{*}\breve Q_{2}^{*}.
$$

*Proof.* The three multiplicativities are those of *The Two Involutions and the Group of Involutions*, using the commutativity of the algebra.

**Theorem (the two-term relations).** The plain and the tessarine products differ by twice the $j$-part of the first factor times the second, and the sesquilinear products by twice the $j$-part of the first factor times the conjugated second:
$$
\breve Q_{1}\breve Q_{2}+\breve Q_{1,\mathrm{ts}}\breve Q_{2}=2Q_{1\blacktriangle}\breve Q_{2},\qquad \breve Q_{1}\breve Q_{2}-\breve Q_{1,\mathrm{ts}}\breve Q_{2}=2Q_{1\blacktriangledown}j\breve Q_{2},
$$
$$
\breve Q_{1}\breve Q_{2}^{*}+\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}=2Q_{1\blacktriangle}\breve Q_{2}^{*},\qquad \breve Q_{1}\breve Q_{2}^{*}-\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}=2Q_{1\blacktriangledown}j\breve Q_{2}^{*}.
$$

*Proof.* Directly from $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ and $\breve Q_{\mathrm{ts}}=Q_{\blacktriangle}-jQ_{\blacktriangledown}$: the sum has the $Q_{\blacktriangledown}j$ term cancelled and the difference the $Q_{\blacktriangle}$ term.

**Theorem (the two-term relations of the forms).** On the two arguments the forms are paired by their bilinear or sesquilinear partner:
$$
\langle \breve Q_{1},\breve Q_{2}\rangle+\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=2Q_{1\blacktriangle}Q_{2\blacktriangle},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle-\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=2Q_{1\blacktriangledown}Q_{2\blacktriangledown},
$$
$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{*}+\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=2Q_{1\blacktriangle}\bar Q_{2\blacktriangle},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{*}-\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=-2Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}.
$$

*Proof.* Add and subtract the displays of the definitions of the four forms.

## The Comparison of the Four Products

**The four products are distinguished by associativity, commutativity, the unit and the norm, and the table is the one below.**

| product | bilinear/sesquilinear | associative | commutative | unit | its algebraic norm | multiplicative norm |
|---|---|---|---|---|---|---|
| $\breve Q_{1}\breve Q_{2}$ | bilinear | **yes** | **yes** | two-sided $1$ | $\langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2}$ | no |
| $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$ | bilinear | no | no | left unit $1$ | $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | **yes** |
| $\breve Q_{1}\breve Q_{2}^{*}$ | sesquilinear | no | no | right unit $1$ | $\langle \breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}$ | no |
| $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$ | sesquilinear | no | no | none | $\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$ | no |

**Theorem (the multiplication is the associative and commutative case).** The general plain bilinear product $\breve Q_{1}\breve Q_{2}$ is the **multiplication** of the algebra; it is the only one of the four that is associative and the only one that is commutative, and it is the only one with a two-sided unit.

*Proof.* The associativity of $\breve Q_{1}\breve Q_{2}$ and the two-sided unit $1$ are *Reduced Biquaternion Space*. The other three products are not associative: for the tessarine bilinear product the triple $\breve Q_{1}=\breve Q_{2}=\breve Q_{3}=j$ separates $((\breve Q_{1,\mathrm{ts}}\breve Q_{2})_{\mathrm{ts}}\breve Q_{3})=(-j)$ from $\breve Q_{1,\mathrm{ts}}(\breve Q_{2,\mathrm{ts}}\breve Q_{3})=j$, and for the two sesquilinear products the triple $\breve Q_{1}=\breve Q_{2}=\breve Q_{3}=i$ separates the two sides, $((i\star i)\star i)=-i$ against $i\star(i\star i)=i$ in both cases. None of the other three is commutative: for the tessarine bilinear product the pair $\breve Q_{1}=1$, $\breve Q_{2}=j$ gives $\breve Q_{1,\mathrm{ts}}\breve Q_{2}=j$ against $\breve Q_{2,\mathrm{ts}}\breve Q_{1}=-j$. The one-sided units are read as in the table: $1$ is a left unit of $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$ because $1_{\mathrm{ts}}\breve Q_{2}=\breve Q_{2}$ and not a right unit because $\breve Q_{1,\mathrm{ts}}1=\breve Q_{1,\mathrm{ts}}\neq \breve Q_{1}$ in general, and $1$ is a right unit of $\breve Q_{1}\breve Q_{2}^{*}$ because $\breve Q_{1}1^{*}=\breve Q_{1}$ and not a left unit because $1\breve Q_{2}^{*}=\breve Q_{2}^{*}\neq \breve Q_{2}$ in general; the product $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$ has neither.

**Corollary (zero divisors and the absence of division).** The multiplication has zero divisors and is not a division algebra: every element of the first idempotent line annihilates every element of the second, and the invertible elements are those of non-vanishing reduced norm $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$.

*Proof.* The zero divisors are *Reduced Biquaternion Space* and are read again in *Zero Divisors of the Algebra of the Reduced Biquaternions*; the criterion is the corollary of §*The Multiplicative Norm*. The words *commutative*, *zero divisors* and *absence of division* are the ones the four products of this article bear, and they are stated wherever they bear on a result.

## Summary

The reduced biquaternion space carries four general products, $\breve Q_{1}\breve Q_{2}$, $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$, $\breve Q_{1}\breve Q_{2}^{*}$ and $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$, defined by which slot carries the tessarine sign and which carries the star, with the coordinate tables of §*The Four General Products*. Their scalar-part forms are
$$
B=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad N=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad H=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},\qquad K=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},
$$
the first two $\mathbb{C}$-bilinear and symmetric, the last two $\mathbb{C}$-sesquilinear and Hermitian, and their Gram matrices are $\operatorname{diag}(1,1)$, $\operatorname{diag}(1,-1)$, $\operatorname{diag}(1,-1)$, $\operatorname{diag}(1,1)$ on the complex basis. Their algebraic norms are the diagonals
$$
\langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2},\quad \langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2},\quad \langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2},\quad \langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2},
$$
complex-valued and indefinite of real signature $(2,2)$ for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$, real-valued and indefinite of signature $(2,2)$ for $\langle\cdot,\cdot\rangle_{*}$, and real-valued positive definite of signature $(4,0)$ for $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$.

The **multiplicative** one is $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})$, the reduced norm of the algebra and its invertibility criterion, $\breve Q$ invertible $\iff \langle \breve Q\rangle_{\mathrm{ts}}\neq0$; the positive-definite one is $\langle\cdot\rangle_{\mathrm{ts}*}$, the topological norm. The **algebraic norm is an element of the algebra** and is not the topological norm, and only $\langle\cdot\rangle_{\mathrm{ts}*}$ is both. The general plain bilinear product is the **multiplication**: it is the only associative and the only commutative one, with unit $1$, while the other three are neither associative nor commutative, with the one-sided units of the table; and the multiplication **has zero divisors and is not a division algebra**. The forms are linked by the relations $B+N=2Q_{1\blacktriangle}Q_{2\blacktriangle}$, $B-N=2Q_{1\blacktriangledown}Q_{2\blacktriangledown}$, $H+K=2Q_{1\blacktriangle}\bar Q_{2\blacktriangle}$ and $H-K=-2Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$, and the four products by $\breve Q_{1}\breve Q_{2}\pm \breve Q_{1,\mathrm{ts}}\breve Q_{2}=2Q_{1\blacktriangle}\breve Q_{2},2jQ_{1\blacktriangledown}\breve Q_{2}$ and $\breve Q_{1}\breve Q_{2}^{*}\pm \breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}=2Q_{1\blacktriangle}\breve Q_{2}^{*},2jQ_{1\blacktriangledown}\breve Q_{2}^{*}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\breve Q_{1}\breve Q_{2}$ | the general plain bilinear product, the multiplication |
| $\breve Q_{1,\mathrm{ts}}\breve Q_{2}$ | the general tessarine bilinear product |
| $\breve Q_{1}\breve Q_{2}^{*}$ | the general plain sesquilinear product |
| $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}$ | the general tessarine sesquilinear product |
| $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{\mathrm{ts}}, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ | the four scalar-part forms, with two arguments |
| $\langle \breve Q\rangle,\langle \breve Q\rangle_{\mathrm{ts}},\langle \breve Q\rangle_{*},\langle \breve Q\rangle_{\mathrm{ts}*}$ | the four algebraic norms, the diagonals |
| $\langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2}$ | the plain bilinear algebraic norm, complex, not multiplicative |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | the tessarine bilinear algebraic norm, complex, **multiplicative**, the reduced norm |
| $\langle \breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}$ | the plain sesquilinear algebraic norm, real, indefinite |
| $\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$ | the tessarine sesquilinear algebraic norm, real, positive definite, the topological norm |
| $\operatorname{diag}(1,1),\operatorname{diag}(1,-1)$ | the complex Gram matrices of $B,K$ and of $N,H$ |
| $(2,2),(4,0)$ | the real signatures of $B,N,H$ and of $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ |

## Further Reading

- [Reduced Biquaternion Space](reduced-biquaternion-space.html), above this article in this category, for the multiplication, the idempotents and the isomorphism $\mathbb{C}\oplus\mathbb{C}$.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), above this article, for the tessarine sign and the star that define the four slots.
- [Conventions of the Norms and the Unitary Convention](conventions-of-the-norms-and-the-unitary-convention.html), §*The Norm Convention*, for the rule that the algebraic norm is the diagonal of a form.
- [Introduction to the Algebra of the Reduced Biquaternions](introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the multiplication read as an algebra.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), below this article, for the algebraic norm of the multiplication and the criterion of invertibility.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four general products of the non-commutative companion and the two slots they carry.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms and the Gram matrices of the companion.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the algebraic norms of the companion.
