# __The Forms of the Algebra of the Reduced Biquaternions__

## Introduction

The general plain algebra of the reduced biquaternions carries two distinguished pairings, a **bilinear** one and a **sesquilinear** one, and this article reads them as objects. The pairing is the scalar part of a product with the four slot conventions of *The Four Products, Their Forms and Their Algebraic Norms*: the first slot may be read plain or through the **tessarine sign** ${}_{\mathrm{ts}}$, and the second slot plain or through the **star** ${}^{*}$. The four combinations give the four forms
$$
\langle \breve Q_{1},\breve Q_{2}\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},
$$
for $\breve Q_{1}=Q_{1\blacktriangle}+jQ_{1\blacktriangledown}$ and $\breve Q_{2}=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$. The first two are **$\mathbb{C}$-bilinear**, since the tessarine sign is $\mathbb{C}$-linear; the last two are **$\mathbb{C}$-sesquilinear**, since the star is $\mathbb{C}$-antilinear. Each form is the scalar part of the corresponding general product, $\langle\cdot,\cdot\rangle=\mathrm{Sc}(\breve Q_{1}\breve Q_{2})$, $\langle\cdot,\cdot\rangle_{\mathrm{ts}}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2})$, $\langle\cdot,\cdot\rangle_{*}=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*})$, so the four forms are the four products read at their scalar part.

**The results.** The four forms are non-degenerate and independent, with the Gram matrices
$$
B=\mathrm I_{2},\qquad N=\operatorname{diag}(1,-1),\qquad H=\operatorname{diag}(1,-1),\qquad K=\mathrm I_{2}
$$
in the complex basis $1,j$, and the signatures $(2,2)$, $(2,2)$, $(2,2)$ and $(4,0)$ over $\mathbb{R}$. The two sesquilinear forms are **Hermitian**, $\langle \breve Q_{2},\breve Q_{1}\rangle_{*}=\overline{\langle \breve Q_{1},\breve Q_{2}\rangle_{*}}$ and $\langle \breve Q_{2},\breve Q_{1}\rangle_{\mathrm{ts}*}=\overline{\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}}$, and their diagonals are the algebraic norms $\langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$ and $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$; the two bilinear forms are symmetric with complex values. The general plain sesquilinear form $\langle\cdot,\cdot\rangle_{*}$ is the one the layer of sesquialgebras selects: it is **compatible with the product**, $\langle \breve Q_{1}\breve Q_{2},\breve Q_{3}\rangle_{*}=\langle \breve Q_{2},\breve Q_{1}^{*}\breve Q_{3}\rangle_{*}$, equivalently $(L_{\breve Q})^{H}=L_{\breve Q^{*}}$. The two sesquilinear forms are tied by the **bridge identity** $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\langle \breve Q_{1,\mathrm{ts}},\breve Q_{2}\rangle_{*}=\langle \breve Q_{1},\breve Q_{2,\mathrm{ts}}\rangle_{*}$, with the tessarine sign as the self-adjoint involution, fixing the scalar line and negating the $j$-line; this is why $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is definite and $\langle\cdot,\cdot\rangle_{*}$ indefinite, and why their signatures are $(4,0)$ and $(2,2)$. At the real base the four forms collapse to two, $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\mathrm{ts}}$, and the sesquilinear pair is bilinear.

**Boundaries.** The four products, their forms and their algebraic norms are stated together in *The Four Products, Their Forms and Their Algebraic Norms*, above this article in this category; the norm of the multiplication and the invertibility criterion are *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the vanishing sets of the norms are the zero divisors of *Zero Divisors of the Algebra of the Reduced Biquaternions*. The forms read on the remarkable subspaces are *Remarkable Subspaces and the Four General Products*; the operators the forms adjoint are *The Multiplication Operators of the Algebra of the Reduced Biquaternions*. The biquaternion counterpart of the layer selection is *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## The Two Slots and the Two Layers

### The Linearity of the Slot Maps

**The tessarine sign is $\mathbb{C}$-linear and the star is $\mathbb{C}$-antilinear; a pairing is bilinear when its second slot is plain and sesquilinear when its second slot carries the star.**

**Proposition (the slot maps).** For $\lambda\in\mathbb{C}$ and $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$,
$$
(\lambda \breve Q)_{\mathrm{ts}}=\lambda\,\breve Q_{\mathrm{ts}},\qquad (\lambda \breve Q)^{*}=\bar\lambda\,\breve Q^{*}.
$$

*Proof.* The tessarine sign negates the second coordinate, $\breve Q_{\mathrm{ts}}=Q_{\blacktriangle}-jQ_{\blacktriangledown}$, and does not touch the coefficients, so it commutes with the complex scalars; the star is $\bar{\cdot}\circ{}_{\mathrm{ts}}$ (*The Two Involutions and the Group of Involutions of the Reduced Biquaternions*), and the composite of a $\mathbb{C}$-linear and a $\mathbb{C}$-antilinear map is antilinear, so $(\lambda \breve Q)^{*}=\overline{\lambda}\,\overline{\breve Q}_{\mathrm{ts}}=\bar\lambda\,\breve Q^{*}$.

**Proposition (which pairings are sesquilinear).** Of the four pairings $\mathrm{Sc}(X\,\breve Q_{1}\,Y\,\breve Q_{2})$, the two with $\mathrm{id}$ in the second slot, $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$, are $\mathbb{C}$-bilinear, and the two with the star there, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$, are $\mathbb{C}$-sesquilinear, linear in the first slot and antilinear in the second.

*Proof.* The scalar part is $\mathbb{C}$-linear, and the slot maps are the ones of the preceding proposition; a $\mathbb{C}$-antilinear slot map makes the pairing antilinear in that slot, a linear one keeps it linear.

**Remark (the two layers).** The bilinear pairings belong to the bilinear layer of *Bilinear Forms*; the sesquilinear pairings belong to the layer of *Sesqualgebras with a Form*, and the layer's involution is the star, as the next section shows. The dichotomy is not a property of the particular forms but of the two slot maps the algebra carries, exactly as in the biquaternion category.

### The Admissible Involution

**The star is the involution of the layer's form: it is $\mathbb{C}$-antilinear of square one and compatible with the plain sesquilinear form; the tessarine sign is $\mathbb{C}$-linear, so it pairs with the bilinear forms; and the bar is $\mathbb{C}$-antilinear too but pairs with the tessarine sesquilinear form, because in the commutative algebra the reversal of the factors is invisible and does not separate the bar from the star.**

**Theorem.** The star satisfies $(\breve Q_{1}\breve Q_{2})^{*}=\breve Q_{1}^{*}\breve Q_{2}^{*}$ and is $\mathbb{C}$-antilinear of square one; the bar satisfies $(\breve Q_{1}\breve Q_{2})^{\bar{}}=\breve Q_{1}^{\bar{}}\breve Q_{2}^{\bar{}}$ and is $\mathbb{C}$-antilinear of square one as well; the tessarine sign satisfies $(\breve Q_{1}\breve Q_{2})_{\mathrm{ts}}=\breve Q_{1,\mathrm{ts}}\breve Q_{2,\mathrm{ts}}$ and is $\mathbb{C}$-linear. The tessarine sign is therefore excluded from the sesquilinear layer, but the bar and the star are not separated by their product type, since in a commutative algebra a product-compatible map is at once an automorphism and an anti-automorphism. What separates them is the form they serve, and the compatibility identity of §*The Compatibility of the Plain Sesquilinear Form* singles out the star for the plain sesquilinear form $\langle\cdot,\cdot\rangle_{*}$; the bar serves the tessarine sesquilinear form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$.

*Proof.* All three maps are computed coordinatewise on $\breve Q_{1}=Q_{1\blacktriangle}+jQ_{1\blacktriangledown}$ and $\breve Q_{2}=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$. The star conjugates the coefficients and negates the second slot, and the two operations are compatible with the product because the product is $\mathbb{C}$-bilinear in the coordinates; the same holds for the bar and the tessarine sign. The star is antilinear by the proposition above, and ${}^{*}\circ{}^{*}=\mathrm{id}$ because ${}_{\mathrm{ts}}\circ{}_{\mathrm{ts}}=\mathrm{id}$ and $\bar{\cdot}\circ\bar{\cdot}=\mathrm{id}$. Of the three, the tessarine sign is linear, so it is excluded from the sesquilinear layer; the bar and the star are both antilinear and of square one, and in the commutative algebra both are at once automorphisms and anti-automorphisms, so the product type does not separate them. The compatibility identity of §*The Compatibility of the Plain Sesquilinear Form* is what selects the star for the plain sesquilinear form $\langle\cdot,\cdot\rangle_{*}$, the bar serving the tessarine sesquilinear form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$.

## The Four Forms

**The four forms are the scalar parts of the four general products: $\langle\cdot,\cdot\rangle=\mathrm{Sc}(\breve Q_{1}\breve Q_{2})$, $\langle\cdot,\cdot\rangle_{\mathrm{ts}}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2})$, $\langle\cdot,\cdot\rangle_{*}=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})$, $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*})$.**

**Proposition (the four forms on the coordinates).** For $\breve Q_{1}=Q_{1\blacktriangle}+jQ_{1\blacktriangledown}$ and $\breve Q_{2}=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$,
$$
\langle \breve Q_{1},\breve Q_{2}\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown},
$$
$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown},\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown} .
$$

*Proof.* Compute each product and take its scalar part. For $\langle\cdot,\cdot\rangle$, $\breve Q_{1}\breve Q_{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j$, so $\mathrm{Sc}(\breve Q_{1}\breve Q_{2})=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$. For $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$, $\breve Q_{1,\mathrm{ts}}\breve Q_{2}=(Q_{1\blacktriangle}-jQ_{1\blacktriangledown})(Q_{2\blacktriangle}+jQ_{2\blacktriangledown})=(Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle})j$. For $\langle\cdot,\cdot\rangle_{*}$, $\breve Q_{1}\breve Q_{2}^{*}=(Q_{1\blacktriangle}+jQ_{1\blacktriangledown})(\bar Q_{2\blacktriangle}-j\bar Q_{2\blacktriangledown})=(Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown})+(Q_{1\blacktriangledown}\bar Q_{2\blacktriangle}-Q_{1\blacktriangle}\bar Q_{2\blacktriangledown})j$, using $j^{2}=+1$. For $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$, $\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*}=(Q_{1\blacktriangle}-jQ_{1\blacktriangledown})(\bar Q_{2\blacktriangle}-j\bar Q_{2\blacktriangledown})=(Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown})-(Q_{1\blacktriangle}\bar Q_{2\blacktriangledown}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangle})j$.

**The two bilinear forms.** $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ are symmetric and $\mathbb{C}$-valued, with no Hermitian condition; their diagonals are $\langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2}$ and $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$, the algebraic norms of the general plain and the general tessarine bilinear products. $\langle\cdot,\cdot\rangle$ is the **general plain bilinear form**, the form of the multiplication; $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ is the **general tessarine bilinear form**, and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ alone is multiplicative, which is the mechanism of *The Group of Units of the Algebra of the Reduced Biquaternions*.

**The two sesquilinear forms.** $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ are Hermitian and real on the diagonal, with $\langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$ and $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$. $\langle\cdot,\cdot\rangle_{*}$ is the **general plain sesquilinear form** and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ the **general tessarine sesquilinear form**; $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is positive definite, with square root the Euclidean norm, and $\langle \breve Q\rangle_{*}$ is indefinite of signature $(2,2)$.

## The Gram Matrices and the Signatures

**In the complex basis $1,j$ the Gram matrices are $B=\mathrm I_{2}$, $N=H=\operatorname{diag}(1,-1)$ and $K=\mathrm I_{2}$; over the real basis the signatures are $(2,2)$, $(2,2)$, $(2,2)$ and $(4,0)$.**

**Proposition (the Gram matrices).** In the complex basis $\{1,j\}$,
$$
G_{B}=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
G_{N}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
G_{H}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
G_{K}=\begin{pmatrix}1&0\\0&1\end{pmatrix},
$$
so all four forms are non-degenerate, each with radical $\{0\}$.

*Proof.* Evaluate each form on the pairs of basis elements: $\langle 1,1\rangle=\langle 1,1\rangle_{\mathrm{ts}}=\langle 1,1\rangle_{*}=\langle 1,1\rangle_{\mathrm{ts}*}=1$; $\langle j,j\rangle=1$, $\langle j,j\rangle_{\mathrm{ts}}=\langle j,j\rangle_{*}=\langle j,j\rangle_{\mathrm{ts}*}$ is $\pm1$ according to the sign in front of $Q_{1\blacktriangledown}Q_{2\blacktriangledown}$; and the cross terms $\langle 1,j\rangle=\langle 1,j\rangle_{\mathrm{ts}}=\langle 1,j\rangle_{*}=\langle 1,j\rangle_{\mathrm{ts}*}=0$ because $\langle\cdot,\cdot\rangle=0$ or $Q_{2\blacktriangle}=0$ in each. Non-degeneracy is the non-vanishing of each determinant, $1$, $-1$, $-1$ and $1$.

**Corollary (the signatures over $\mathbb{R}$).** In the real basis $\{1,i,j,ij\}$ the real parts have the diagonal Gram matrices
$$
\operatorname{diag}(1,-1,1,-1),\qquad \operatorname{diag}(1,-1,-1,1),\qquad \operatorname{diag}(1,1,-1,-1),\qquad \mathrm I_{4},
$$
so the signatures are $(2,2)$ for $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ and $\langle\cdot,\cdot\rangle_{*}$ and $(4,0)$ for $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$. Over $\mathbb{C}$ the inertia indices are $(1,1,0)$ for $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ and $\langle\cdot,\cdot\rangle_{*}$ and $(2,0,0)$ for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$.

*Proof.* Read the real coordinates $Q_{1\blacktriangle}=q_{1\blacktriangle}+iq'_{1\blacktriangle}$, $Q_{1\blacktriangledown}=q_{1\blacktriangledown}+iq'_{1\blacktriangledown}$ and $Q_{2\blacktriangle}=q_{2\blacktriangle}+iq'_{2\blacktriangle}$, $Q_{2\blacktriangledown}=q_{2\blacktriangledown}+iq'_{2\blacktriangledown}$ on each form; the real part of $\langle\cdot,\cdot\rangle$ is $q_{1\blacktriangle}q_{2\blacktriangle}-q'_{1\blacktriangle}q'_{2\blacktriangle}+q_{1\blacktriangledown}q_{2\blacktriangledown}-q'_{1\blacktriangledown}q'_{2\blacktriangledown}$, whose Gram matrix is the displayed one, and the other three are computed the same way. The signs follow from $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$, $\langle \breve Q\rangle_{*}=|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$ and $\langle \breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$ on the real basis.

**Remark (definite and indefinite).** $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is the only definite form of the four, positive definite; $\langle\cdot,\cdot\rangle_{*}$ is indefinite of signature $(2,2)$; and the two bilinear forms are complex-valued, so their "signature" is read on their real parts only. This is the reduced biquaternion instance of the table of *The Four Products, Their Forms and Their Algebraic Norms*, and the four norms are the diagonals of §*The Four Forms*.

## The Bridge Identity and the Fundamental Symmetry

**The two sesquilinear forms are related by the tessarine sign, which is an $\langle\cdot,\cdot\rangle_{*}$-self-adjoint involution; this is why $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is definite and $\langle\cdot,\cdot\rangle_{*}$ is indefinite.**

**Theorem (the bridge identity).** The tessarine sign is an $\langle\cdot,\cdot\rangle_{*}$-self-adjoint involution,
$$
\langle \breve Q_{1,\mathrm{ts}},\breve Q_{2}\rangle_{*}=\langle \breve Q_{1},\breve Q_{2,\mathrm{ts}}\rangle_{*}=\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*},
$$
and it fixes the scalar line $\mathbb{C}$ and negates the $j$-line $\mathbb{C}j$; the two lines are $\langle\cdot,\cdot\rangle_{*}$-orthogonal, and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ restricted to them is $+H$ and $-H$ respectively.

*Proof.* $\langle \breve Q_{1,\mathrm{ts}},\breve Q_{2}\rangle_{*}=\langle Q_{1\blacktriangle}-jQ_{1\blacktriangledown},Q_{2\blacktriangle}+jQ_{2\blacktriangledown}\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-(-Q_{1\blacktriangledown})\bar Q_{2\blacktriangledown}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}=\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}$; the mirror computation gives $\langle \breve Q_{1},\breve Q_{2,\mathrm{ts}}\rangle_{*}=\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}$; the two together are the self-adjointness. The tessarine sign fixes $Q_{\blacktriangle}$ and negates $Q_{\blacktriangledown}$, hence fixes the scalar line and negates the $j$-line. The orthogonality is $\langle Q_{1\blacktriangle},Q_{2\blacktriangledown}j\rangle_{*}=Q_{1\blacktriangle}\cdot\bar 0-0\cdot\bar Q_{2\blacktriangledown}=0$ for scalar $Q_{1\blacktriangle}$ and for $Q_{2\blacktriangledown}j$ in the $j$-line. The signs of $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ on the two lines follow from $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=H\circ(\mathrm{ts},\mathrm{id})$ and the eigenvalues $\pm1$ of the tessarine sign.

**Corollary (the definiteness).** $\langle \breve Q\rangle_{\mathrm{ts}*}=\langle \breve Q_{\mathrm{ts}},\breve Q\rangle_{*}$, so $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is $\langle\cdot,\cdot\rangle_{*}$ read through the involution: on the scalar line $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=+H>0$ and on the $j$-line $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=-H>0$, and the two positive contributions give the definiteness of $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ and the signature $(2,2)$ of $\langle\cdot,\cdot\rangle_{*}$. The involution is the **fundamental symmetry** of the pair $(H,K)$.

## The Compatibility of the Plain Sesquilinear Form

**The general plain sesquilinear form is compatible with the multiplication, and the general tessarine one is not.**

**Theorem (the compatibility).** The form $\langle\cdot,\cdot\rangle_{*}$ satisfies
$$
\langle \breve Q_{1}\breve Q_{2},\breve Q_{3}\rangle_{*}=\langle \breve Q_{2},\breve Q_{1}^{*}\breve Q_{3}\rangle_{*}\qquad\text{for all }\breve Q_{1},\breve Q_{2},\breve Q_{3},
$$
equivalently $(L_{\breve Q})^{H}=L_{\breve Q^{*}}$, so the left multiplication by $\breve Q$ is the $\langle\cdot,\cdot\rangle_{*}$-adjoint of the left multiplication by $\breve Q^{*}$.

*Proof.* Expand both sides. On the one hand $\langle \breve Q_{1}\breve Q_{2},\breve Q_{3}\rangle_{*}=\mathrm{Sc}\bigl((\breve Q_{1}\breve Q_{2})\breve Q_{3}^{*}\bigr)$. On the other $\langle \breve Q_{2},\breve Q_{1}^{*}\breve Q_{3}\rangle_{*}=\mathrm{Sc}\bigl(\breve Q_{2}(\breve Q_{1}^{*}\breve Q_{3})^{*}\bigr)=\mathrm{Sc}(\breve Q_{2} \breve Q_{3}^{*}\breve Q_{1})=\mathrm{Sc}(\breve Q_{1}\breve Q_{2}\breve Q_{3}^{*})$, using $(\breve Q_{1}^{*}\breve Q_{3})^{*}=\breve Q_{3}^{*}\breve Q_{1}$ and the cyclicity $\mathrm{Sc}(XYZ)=\mathrm{Sc}(ZXY)$ of the scalar part, which holds because the scalar part is the trace of the regular representation and the algebra is commutative. The two expressions agree.

**Remark (the layer's involution is the star).** The compatibility identity $\langle \breve Q_{1}\breve Q_{2},\breve Q_{3}\rangle_{*}=\langle \breve Q_{2},\breve Q_{1}^{*}\breve Q_{3}\rangle_{*}$ is the axiom that makes the left multiplications of the algebra the layer's adjointable operators, and it uses the star and no other conjugation: the bar and the tessarine sign produce the two bilinear pairings and the Hermitian form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$, whose adjoint rule is read in *The Multiplication Operators of the Algebra of the Reduced Biquaternions*. This is the sense in which $(\mathbb{B}_{\mathrm{r}},{}^{*},H)$ is an object of the layer of *Sesqualgebras with a Form*, exactly as $(\mathbb{B},{}^{*},h)$ is in the biquaternion category.

## The Unitary Elements

**The elements preserving $\langle\cdot,\cdot\rangle_{*}$ are the solutions of $U^{*}U=1$, they form a group isomorphic to $\mathbb{C}^{\times}$, and they are not the diagonal unitary matrices.**

**Theorem (the unitary elements).** The set
$$
\mathcal U=\{U\in\mathbb{B}_{\mathrm{r}}:U^{*}U=1\}=\{U:U=Q_{+}\Pi_++|Q_{+}|^{-2}Q_{+}\,\Pi_-,\ Q_{+}\in\mathbb{C}^{\times}\}
$$
is a group under the multiplication, isomorphic to $\mathbb{C}^{\times}$ through the first idempotent coordinate; it is the group of elements whose left multiplication is an $\langle\cdot,\cdot\rangle_{*}$-isometry, $\langle U\breve Q_{1},U\breve Q_{2}\rangle_{*}=\langle \breve Q_{1},\breve Q_{2}\rangle_{*}$ for all $\breve Q_{1},\breve Q_{2}$.

*Proof.* In the idempotent coordinates $U=Q_{+}\Pi_++Q_{-}\Pi_-$ one has $U^{*}=\bar Q_{-}\,\Pi_++\bar Q_{+}\,\Pi_-$, since the star swaps the two idempotents and conjugates the scalars. Hence $U^{*}U=\bar Q_{-} Q_{+}\,\Pi_++\bar Q_{+} Q_{-}\,\Pi_-$, and $U^{*}U=1=\Pi_++\Pi_-$ is the single equation $\bar Q_{-} Q_{+}=1$, equivalently $Q_{-}=Q_{+}/|Q_{+}|^{2}$. The parametrisation is a group homomorphism from $\mathbb{C}^{\times}$ because $Q_{+}\mapsto Q_{+}\Pi_++|Q_{+}|^{-2}Q_{+}\Pi_-$ sends $Q_{+} Q_{+}'$ to $Q_{+}Q_{+}'\Pi_++|Q_{+}Q_{+}'|^{-2}Q_{+}Q_{+}'\Pi_-$, which is the product of the images. The isometry property is the compatibility of §*The Compatibility of the Plain Sesquilinear Form* read twice.

**Remark (the slice is not compact).** The unitary elements form the group $\mathbb{C}^{\times}$, of topology that of a circle times a line, so the slice is not compact; this is a genuine specificity of the reduced biquaternion against the biquaternion category, where the slice $U^{*}U=e_t$ is the compact group $\mathrm{U}(2)$. The reason is the factoring of the algebra: the star swaps the two idempotents, so the unitarity couples the two coordinates by one equation and not by two, and the slice acquires the non-compact direction of $|Q_{+}|$.

## The Collapse at the Real Base

**At the real base the star equals the tessarine sign, the four forms collapse to two, and the sesquilinear pair becomes bilinear.**

**Theorem (the collapse).** Let the coefficients be real, $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{R}$. Then $\breve Q^{*}=\breve Q_{\mathrm{ts}}$ and
$$
\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\langle \breve Q_{1},\breve Q_{2}\rangle,\qquad \langle \breve Q_{1},\breve Q_{2}\rangle_{*}=\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}},
$$
so the four forms collapse to the two real symmetric bilinear forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$, of signatures $(2,0)$ and $(1,1)$ on the real basis, and the Hermitian condition becomes the plain symmetry.

*Proof.* At real coefficients the coefficient conjugation is the identity, so the star reduces to the tessarine sign, ${}^{*}={}_{\mathrm{ts}}$. Then $\langle\cdot,\cdot\rangle_{*}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2})=N$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2,\mathrm{ts}})=\mathrm{Sc}(\breve Q_{1}\breve Q_{2})=B$, since $\breve Q_{2,\mathrm{ts}}$ has the same scalar part as $\breve Q_{2}$ up to the sign of the second coordinate, which the product reads twice. The two remaining forms are symmetric because the coefficient conjugation is the identity.

**Remark (which statements are genuinely sesquilinear).** The compatibility, the bridge identity and the adjoint rule hold in both categories and are read at the real base as the self-adjointness of the left multiplications for the symmetric forms; the sesquilinear content of the article is the dichotomy of the two slot maps, the modulus in the Hermitian condition, the definiteness of $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ against the indefiniteness of $\langle\cdot,\cdot\rangle_{*}$, and the non-compactness of the unitary slice — none of which survives the collapse to the real base.

## Summary

The general plain algebra carries four distinguished forms, the scalar parts of the four general products: the **general plain bilinear form** $\langle \breve Q_{1},\breve Q_{2}\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$, the **general tessarine bilinear form** $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown}$, the **general plain sesquilinear form** $\langle \breve Q_{1},\breve Q_{2}\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ and the **general tessarine sesquilinear form** $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$. The tessarine sign is $\mathbb{C}$-linear, so $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ are bilinear; the star is $\mathbb{C}$-antilinear, so $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ are sesquilinear. All four are non-degenerate, with Gram matrices $\mathrm I_{2}$, $\operatorname{diag}(1,-1)$, $\operatorname{diag}(1,-1)$ and $\mathrm I_{2}$ in the basis $1,j$, and signatures $(2,2)$, $(2,2)$, $(2,2)$ and $(4,0)$ over $\mathbb{R}$; $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is positive definite and its square root is the Euclidean norm, and $\langle \breve Q\rangle_{*}$ is indefinite. The two sesquilinear forms are Hermitian, with diagonals the algebraic norms $|Q_{\blacktriangle}|^{2}-|Q_{\blacktriangledown}|^{2}$ and $|Q_{\blacktriangle}|^{2}+|Q_{\blacktriangledown}|^{2}$, and they are tied by the **bridge identity** $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\langle \breve Q_{1,\mathrm{ts}},\breve Q_{2}\rangle_{*}=\langle \breve Q_{1},\breve Q_{2,\mathrm{ts}}\rangle_{*}$, the tessarine sign being an $\langle\cdot,\cdot\rangle_{*}$-self-adjoint involution fixing the scalar line and negating the $j$-line; this is the fundamental symmetry that makes $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ definite and $\langle\cdot,\cdot\rangle_{*}$ indefinite. The general plain sesquilinear form is the one the layer selects: it is **compatible with the product**, $\langle \breve Q_{1}\breve Q_{2},\breve Q_{3}\rangle_{*}=\langle \breve Q_{2},\breve Q_{1}^{*}\breve Q_{3}\rangle_{*}$, equivalently $(L_{\breve Q})^{H}=L_{\breve Q^{*}}$, so $(\mathbb{B}_{\mathrm{r}},{}^{*},H)$ is an object of the layer of *Sesqualgebras with a Form*. Its unitary elements, the solutions of $U^{*}U=1$, form the non-compact group $\mathbb{C}^{\times}$ and not the diagonal unitary group. At the real base the four forms collapse to two, $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\mathrm{ts}}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\breve Q_{1}=Q_{1\blacktriangle}+jQ_{1\blacktriangledown},\ \breve Q_{2}=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$ | the two arguments of a form |
| $\langle \breve Q_{1},\breve Q_{2}\rangle=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | the general plain bilinear form, $\mathrm{Sc}(\breve Q_{1}\breve Q_{2})$ |
| $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}}=Q_{1\blacktriangle}Q_{2\blacktriangle}-Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | the general tessarine bilinear form, $\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2})$ |
| $\langle \breve Q_{1},\breve Q_{2}\rangle_{*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}-Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | the general plain sesquilinear form, $\mathrm{Sc}(\breve Q_{1}\breve Q_{2}^{*})$ |
| $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=Q_{1\blacktriangle}\bar Q_{2\blacktriangle}+Q_{1\blacktriangledown}\bar Q_{2\blacktriangledown}$ | the general tessarine sesquilinear form, $\mathrm{Sc}(\breve Q_{1,\mathrm{ts}}\breve Q_{2}^{*})$ |
| $\langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2},\ \langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ | the diagonals of the two bilinear forms |
| $\langle \breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2},\ \langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$ | the diagonals of the two sesquilinear forms |
| $\langle\cdot,\cdot\rangle_{*}$ | the form of the layer, compatible with the product |
| $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=H\circ(\mathrm{ts},\mathrm{id})$ | the bridge identity, the fundamental symmetry ${}_{\mathrm{ts}}$ |
| $U^{*}U=1$ | the unitary elements, the group $\mathbb{C}^{\times}$ |

## Further Reading

- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the four products, their forms and their norms together.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the norm of the multiplication.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the vanishing sets of the norms.
- [The Multiplication Operators of the Algebra of the Reduced Biquaternions](the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the adjoint rule and the bi-module structure.
- [The Two Involutions and the Group of Involutions of the Reduced Biquaternions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), for the tessarine sign, the star and the bar.
- [The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form](the-form-on-the-biquaternion-algebra-as-a-general-plain-sesquilinear-form.html), for the non-commutative companion of the layer's selection.
