# __The Forms of the General Plain Algebra of the Reduced Biquaternions__

## Introduction

The general plain algebra of the reduced biquaternions carries two distinguished pairings, a **bilinear** one and a **sesquilinear** one, and this article reads them as objects. The pairing is the scalar part of a product with the four slot conventions of *The Four Products, Their Forms and Their Algebraic Norms*: the first slot may be read plain or through the **natural sign** ${}^{\natural}$, and the second slot plain or through the **star** ${}^{*}$. The four combinations give the four forms
$$
\langle T,W\rangle=AC+BD,\qquad \langle T,W\rangle_{\natural}=AC-BD,\qquad \langle T,W\rangle_{*}=A\bar C-B\bar D,\qquad \langle T,W\rangle_{\natural*}=A\bar C+B\bar D,
$$
for $T=A+Bj$ and $W=C+Dj$. The first two are **$\mathbb{C}$-bilinear**, since the natural sign is $\mathbb{C}$-linear; the last two are **$\mathbb{C}$-sesquilinear**, since the star is $\mathbb{C}$-antilinear. Each form is the scalar part of the corresponding general product, $\langle\cdot,\cdot\rangle=\mathrm{Sc}(TW)$, $\langle\cdot,\cdot\rangle_{\natural}=\mathrm{Sc}(T^{\natural}W)$, $\langle\cdot,\cdot\rangle_{*}=\mathrm{Sc}(TW^{*})$ and $\langle\cdot,\cdot\rangle_{\natural*}=\mathrm{Sc}(T^{\natural}W^{*})$, so the four forms are the four products read at their scalar part.

**The results.** The four forms are non-degenerate and independent, with the Gram matrices
$$
B=\mathrm I_{2},\qquad N=\operatorname{diag}(1,-1),\qquad H=\operatorname{diag}(1,-1),\qquad K=\mathrm I_{2}
$$
in the complex basis $1,j$, and the signatures $(2,2)$, $(2,2)$, $(2,2)$ and $(4,0)$ over $\mathbb{R}$. The two sesquilinear forms are **Hermitian**, $\langle W,T\rangle_{*}=\overline{\langle T,W\rangle_{*}}$ and $\langle W,T\rangle_{\natural*}=\overline{\langle T,W\rangle_{\natural*}}$, and their diagonals are the algebraic norms $\langle T\rangle_{*}=|A|^{2}-|B|^{2}$ and $\langle T\rangle_{\natural*}=|A|^{2}+|B|^{2}$; the two bilinear forms are symmetric with complex values. The general plain sesquilinear form $\langle\cdot,\cdot\rangle_{*}$ is the one the layer of sesquialgebras selects: it is **compatible with the product**, $H(TW,R)=\langle W,T^{*}R\rangle_{*}$, equivalently $(L_{T})^{H}=L_{T^{*}}$. The two sesquilinear forms are tied by the **bridge identity** $\langle T,W\rangle_{\natural*}=\langle T^{\natural},W\rangle_{*}=\langle T,W^{\natural}\rangle_{*}$, with the natural sign as the self-adjoint involution, fixing the scalar line and negating the $j$-line; this is why $\langle\cdot,\cdot\rangle_{\natural*}$ is definite and $\langle\cdot,\cdot\rangle_{*}$ indefinite, and why their signatures are $(4,0)$ and $(2,2)$. At the real base the four forms collapse to two, $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural}$, and the sesquilinear pair is bilinear.

**Boundaries.** The four products, their forms and their algebraic norms are stated together in *The Four Products, Their Forms and Their Algebraic Norms*, above this article in this category; the norm of the multiplication and the invertibility criterion are *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*; the vanishing sets of the norms are the zero divisors of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*. The forms read on the remarkable subspaces are *Remarkable Subspaces and the Four General Products*; the operators the forms adjoint are *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions*. The biquaternion counterpart of the layer selection is *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## The Two Slots and the Two Layers

### The Linearity of the Slot Maps

**The natural sign is $\mathbb{C}$-linear and the star is $\mathbb{C}$-antilinear; a pairing is bilinear when its second slot is plain and sesquilinear when its second slot carries the star.**

**Proposition (the slot maps).** For $\lambda\in\mathbb{C}$ and $T=A+Bj$,
$$
(\lambda T)^{\natural}=\lambda\,T^{\natural},\qquad (\lambda T)^{*}=\bar\lambda\,T^{*}.
$$

*Proof.* The natural sign negates the second coordinate, $T^{\natural}=A-Bj$, and does not touch the coefficients, so it commutes with the complex scalars; the star is $\bar{\cdot}\circ{}^{\natural}$ (*The Two Involutions and the Group of Involutions of the Reduced Biquaternions*), and the composite of a $\mathbb{C}$-linear and a $\mathbb{C}$-antilinear map is antilinear, so $(\lambda T)^{*}=\overline{\lambda}\,\overline{T}^{\natural}=\bar\lambda\,T^{*}$.

**Proposition (which pairings are sesquilinear).** Of the four pairings $\mathrm{Sc}(X\,T\,Y\,W)$, the two with $\mathrm{id}$ in the second slot, $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, are $\mathbb{C}$-bilinear, and the two with the star there, $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$, are $\mathbb{C}$-sesquilinear, linear in the first slot and antilinear in the second.

*Proof.* The scalar part is $\mathbb{C}$-linear, and the slot maps are the ones of the preceding proposition; a $\mathbb{C}$-antilinear slot map makes the pairing antilinear in that slot, a linear one keeps it linear.

**Remark (the two layers).** The bilinear pairings belong to the bilinear layer of *Bilinear Forms*; the sesquilinear pairings belong to the layer of *Sesqualgebras with a Form*, and the layer's involution is the star, as the next section shows. The dichotomy is not a property of the particular forms but of the two slot maps the algebra carries, exactly as in the biquaternion category.

### The Admissible Involution

**The star is the involution of the layer's form: it is $\mathbb{C}$-antilinear of square one and compatible with the plain sesquilinear form; the natural sign is $\mathbb{C}$-linear, so it pairs with the bilinear forms; and the bar is $\mathbb{C}$-antilinear too but pairs with the quaternionic sesquilinear form, because in the commutative algebra the reversal of the factors is invisible and does not separate the bar from the star.**

**Theorem.** The star satisfies $(TW)^{*}=T^{*}W^{*}$ and is $\mathbb{C}$-antilinear of square one; the bar satisfies $(TW)^{\bar{}}=T^{\bar{}}W^{\bar{}}$ and is $\mathbb{C}$-antilinear of square one as well; the natural sign satisfies $(TW)^{\natural}=T^{\natural}W^{\natural}$ and is $\mathbb{C}$-linear. The natural sign is therefore excluded from the sesquilinear layer, but the bar and the star are not separated by their product type, since in a commutative algebra a product-compatible map is at once an automorphism and an anti-automorphism. What separates them is the form they serve, and the compatibility identity of §*The Compatibility of the Plain Sesquilinear Form* singles out the star for the plain sesquilinear form $\langle\cdot,\cdot\rangle_{*}$; the bar serves the quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$.

*Proof.* All three maps are computed coordinatewise on $T=A+Bj$ and $W=C+Dj$. The star conjugates the coefficients and negates the second slot, and the two operations are compatible with the product because the product is $\mathbb{C}$-bilinear in the coordinates; the same holds for the bar and the natural sign. The star is antilinear by the proposition above, and ${}^{*}\circ{}^{*}=\mathrm{id}$ because ${}^{\natural}\circ{}^{\natural}=\mathrm{id}$ and $\bar{\cdot}\circ\bar{\cdot}=\mathrm{id}$. Of the three, the natural sign is linear, so it is excluded from the sesquilinear layer; the bar and the star are both antilinear and of square one, and in the commutative algebra both are at once automorphisms and anti-automorphisms, so the product type does not separate them. The compatibility identity of §*The Compatibility of the Plain Sesquilinear Form* is what selects the star for the plain sesquilinear form $\langle\cdot,\cdot\rangle_{*}$, the bar serving the quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$.

## The Four Forms

**The four forms are the scalar parts of the four general products: $\langle\cdot,\cdot\rangle=\mathrm{Sc}(TW)$, $\langle\cdot,\cdot\rangle_{\natural}=\mathrm{Sc}(T^{\natural}W)$, $\langle\cdot,\cdot\rangle_{*}=\mathrm{Sc}(TW^{*})$, $\langle\cdot,\cdot\rangle_{\natural*}=\mathrm{Sc}(T^{\natural}W^{*})$.**

**Proposition (the four forms on the coordinates).** For $T=A+Bj$ and $W=C+Dj$,
$$
\langle T,W\rangle=AC+BD,\qquad \langle T,W\rangle_{\natural}=AC-BD,
$$
$$
\langle T,W\rangle_{*}=A\bar C-B\bar D,\qquad \langle T,W\rangle_{\natural*}=A\bar C+B\bar D .
$$

*Proof.* Compute each product and take its scalar part. For $\langle\cdot,\cdot\rangle$, $TW=(AC+BD)+(AD+BC)j$, so $\mathrm{Sc}(TW)=AC+BD$. For $\langle\cdot,\cdot\rangle_{\natural}$, $T^{\natural}W=(A-Bj)(C+Dj)=(AC-BD)+(AD-BC)j$. For $\langle\cdot,\cdot\rangle_{*}$, $TW^{*}=(A+Bj)(\bar C-\bar Dj)=(A\bar C-B\bar D)+(B\bar C-A\bar D)j$, using $j^{2}=+1$. For $\langle\cdot,\cdot\rangle_{\natural*}$, $T^{\natural}W^{*}=(A-Bj)(\bar C-\bar Dj)=(A\bar C+B\bar D)-(A\bar D+B\bar C)j$.

**The two bilinear forms.** $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are symmetric and $\mathbb{C}$-valued, with no Hermitian condition; their diagonals are $\langle T\rangle=A^{2}+B^{2}$ and $\langle T\rangle_{\natural}=A^{2}-B^{2}$, the algebraic norms of the general plain and the general quaternionic bilinear products. $\langle\cdot\rangle$ is the **general plain bilinear form**, the form of the multiplication; $\langle\cdot,\cdot\rangle_{\natural}$ is the **general quaternionic bilinear form**, and $\langle\cdot,\cdot\rangle_{\natural}$ alone is multiplicative, which is the mechanism of *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*.

**The two sesquilinear forms.** $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ are Hermitian and real on the diagonal, with $\langle T\rangle_{*}=|A|^{2}-|B|^{2}$ and $\langle T\rangle_{\natural*}=|A|^{2}+|B|^{2}$. $\langle\cdot,\cdot\rangle_{*}$ is the **general plain sesquilinear form** and $\langle\cdot,\cdot\rangle_{\natural*}$ the **general quaternionic sesquilinear form**; $\langle\cdot,\cdot\rangle_{\natural*}$ is positive definite, with square root the Euclidean norm, and $\langle\cdot\rangle_{*}$ is indefinite of signature $(2,2)$.

## The Gram Matrices and the Signatures

**In the complex basis $1,j$ the Gram matrices are $\langle\cdot\rangle=\mathrm I_{2}$, $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}=\operatorname{diag}(1,-1)$ and $\langle\cdot,\cdot\rangle_{\natural*}=\mathrm I_{2}$; over the real basis the signatures are $(2,2)$, $(2,2)$, $(2,2)$ and $(4,0)$.**

**Proposition (the Gram matrices).** In the complex basis $\{1,j\}$,
$$
G_{B}=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
G_{N}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
G_{H}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
G_{K}=\begin{pmatrix}1&0\\0&1\end{pmatrix},
$$
so all four forms are non-degenerate, each with radical $\{0\}$.

*Proof.* Evaluate each form on the pairs of basis elements: $\langle 1,1\rangle=\langle 1,1\rangle_{\natural}=\langle 1,1\rangle_{*}=\langle 1,1\rangle_{\natural*}=1$; $\langle j,j\rangle=1$, $\langle j,j\rangle_{\natural}=\langle j,j\rangle_{*}=\langle j,j\rangle_{\natural*}$ is $\pm1$ according to the sign in front of $BD$; and the cross terms $\langle 1,j\rangle=\langle 1,j\rangle_{\natural}=\langle 1,j\rangle_{*}=\langle 1,j\rangle_{\natural*}=0$ because $\langle\cdot,\cdot\rangle=0$ or $D=0$ in each. Non-degeneracy is the non-vanishing of each determinant, $1$, $-1$, $-1$ and $1$.

**Corollary (the signatures over $\mathbb{R}$).** In the real basis $\{1,i,j,ij\}$ the real parts have the diagonal Gram matrices
$$
\operatorname{diag}(1,-1,1,-1),\qquad \operatorname{diag}(1,-1,-1,1),\qquad \operatorname{diag}(1,1,-1,-1),\qquad \mathrm I_{4},
$$
so the signatures are $(2,2)$ for $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{*}$ and $(4,0)$ for $\langle\cdot,\cdot\rangle_{\natural*}$. Over $\mathbb{C}$ the inertia indices are $(1,1,0)$ for $\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{*}$ and $(2,0,0)$ for $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural*}$.

*Proof.* Read the real coordinates $A=a+ia'$, $\langle\cdot,\cdot\rangle=b+ib'$ on each form; the real part of $\langle\cdot,\cdot\rangle$ is $ac-a'c'+bd-b'd'$, whose Gram matrix is the displayed one, and the other three are computed the same way. The signs follow from $\langle T\rangle_{\natural}=A^{2}-B^{2}$, $\langle T\rangle_{*}=|A|^{2}-|B|^{2}$ and $\langle T\rangle_{\natural*}=|A|^{2}+|B|^{2}$ on the real basis.

**Remark (definite and indefinite).** $\langle\cdot,\cdot\rangle_{\natural*}$ is the only definite form of the four, positive definite; $\langle\cdot,\cdot\rangle_{*}$ is indefinite of signature $(2,2)$; and the two bilinear forms are complex-valued, so their "signature" is read on their real parts only. This is the reduced biquaternion instance of the table of *The Four Products, Their Forms and Their Algebraic Norms*, and the four norms are the diagonals of §*The Four Forms*.

## The Bridge Identity and the Fundamental Symmetry

**The two sesquilinear forms are related by the natural sign, which is an $\langle\cdot,\cdot\rangle_{*}$-self-adjoint involution; this is why $\langle\cdot,\cdot\rangle_{\natural*}$ is definite and $\langle\cdot,\cdot\rangle_{*}$ is indefinite.**

**Theorem (the bridge identity).** The natural sign is an $\langle\cdot,\cdot\rangle_{*}$-self-adjoint involution,
$$
\langle T^{\natural},W\rangle_{*}=\langle T,W^{\natural}\rangle_{*}=\langle T,W\rangle_{\natural*},
$$
and it fixes the scalar line $\mathbb{C}$ and negates the $j$-line $\mathbb{C}j$; the two lines are $\langle\cdot,\cdot\rangle_{*}$-orthogonal, and $\langle\cdot,\cdot\rangle_{\natural*}$ restricted to them is $+H$ and $-H$ respectively.

*Proof.* $\langle T^{\natural},W\rangle_{*}=\langle A-Bj,C+Dj\rangle_{*}=A\bar C-(-B)\bar D=A\bar C+B\bar D=\langle T,W\rangle_{\natural*}$; the mirror computation gives $\langle T,W^{\natural}\rangle_{*}=\langle T,W\rangle_{\natural*}$; the two together are the self-adjointness. The natural sign fixes $A$ and negates $\langle\cdot,\cdot\rangle$, hence fixes the scalar line and negates the $j$-line. The orthogonality is $\langle A,Cj\rangle_{*}=A\cdot\bar 0-0\cdot\bar C=0$ for scalar $A$ and for $Cj$ in the $j$-line. The signs of $\langle\cdot,\cdot\rangle_{\natural*}$ on the two lines follow from $\langle\cdot,\cdot\rangle_{\natural*}=H\circ(\natural,\mathrm{id})$ and the eigenvalues $\pm1$ of the natural sign.

**Corollary (the definiteness).** $\langle T\rangle_{\natural*}=\langle T^{\natural},T\rangle_{*}$, so $\langle\cdot,\cdot\rangle_{\natural*}$ is $\langle\cdot,\cdot\rangle_{*}$ read through the involution: on the scalar line $\langle\cdot,\cdot\rangle_{\natural*}=+H>0$ and on the $j$-line $\langle\cdot,\cdot\rangle_{\natural*}=-H>0$, and the two positive contributions give the definiteness of $\langle\cdot,\cdot\rangle_{\natural*}$ and the signature $(2,2)$ of $\langle\cdot,\cdot\rangle_{*}$. The involution is the **fundamental symmetry** of the pair $(H,K)$.

## The Compatibility of the Plain Sesquilinear Form

**The general plain sesquilinear form is compatible with the multiplication, and the general quaternionic one is not.**

**Theorem (the compatibility).** The form $\langle\cdot,\cdot\rangle_{*}$ satisfies
$$
H(TW,R)=\langle W,T^{*}R\rangle_{*}\qquad\text{for all }T,W,R,
$$
equivalently $(L_{T})^{H}=L_{T^{*}}$, so the left multiplication by $T$ is the $\langle\cdot,\cdot\rangle_{*}$-adjoint of the left multiplication by $T^{*}$.

*Proof.* Expand both sides. On the one hand $H(TW,R)=\mathrm{Sc}\bigl((TW)R^{*}\bigr)$. On the other $\langle W,T^{*}R\rangle_{*}=\mathrm{Sc}\bigl(W(T^{*}R)^{*}\bigr)=\mathrm{Sc}(W R^{*}T)=\mathrm{Sc}(TWR^{*})$, using $(T^{*}R)^{*}=R^{*}T$ and the cyclicity $\mathrm{Sc}(XYZ)=\mathrm{Sc}(ZXY)$ of the scalar part, which holds because the scalar part is the trace of the regular representation and the algebra is commutative. The two expressions agree.

**Remark (the layer's involution is the star).** The compatibility identity $H(TW,R)=\langle W,T^{*}R\rangle_{*}$ is the axiom that makes the left multiplications of the algebra the layer's adjointable operators, and it uses the star and no other conjugation: the bar and the natural sign produce the two bilinear pairings and the Hermitian form $\langle\cdot,\cdot\rangle_{\natural*}$, whose adjoint rule is read in *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions*. This is the sense in which $(\mathbb{B}_{\mathrm{r}},{}^{*},H)$ is an object of the layer of *Sesqualgebras with a Form*, exactly as $(\mathbb{B},{}^{*},h)$ is in the biquaternion category.

## The Unitary Elements

**The elements preserving $\langle\cdot,\cdot\rangle_{*}$ are the solutions of $U^{*}U=1$, they form a group isomorphic to $\mathbb{C}^{\times}$, and they are not the diagonal unitary matrices.**

**Theorem (the unitary elements).** The set
$$
\mathcal U=\{U\in\mathbb{B}_{\mathrm{r}}:U^{*}U=1\}=\{U:U=q_1\Pi_{1}+|q_1|^{-2}q_1\,\Pi_{2},\ q_1\in\mathbb{C}^{\times}\}
$$
is a group under the multiplication, isomorphic to $\mathbb{C}^{\times}$ through the first idempotent coordinate; it is the group of elements whose left multiplication is an $\langle\cdot,\cdot\rangle_{*}$-isometry, $\langle UX,UY\rangle_{*}=\langle X,Y\rangle_{*}$ for all $X,Y$.

*Proof.* In the idempotent coordinates $U=q_1\Pi_{1}+q_2\Pi_{2}$ one has $U^{*}=\bar q_2\,\Pi_{1}+\bar q_1\,\Pi_{2}$, since the star swaps the two idempotents and conjugates the scalars. Hence $U^{*}U=\bar q_2 q_1\,\Pi_{1}+\bar q_1 q_2\,\Pi_{2}$, and $U^{*}U=1=\Pi_{1}+\Pi_{2}$ is the single equation $\bar q_2 q_1=1$, equivalently $q_2=q_1/|q_1|^{2}$. The parametrisation is a group homomorphism from $\mathbb{C}^{\times}$ because $q_1\mapsto q_1\Pi_{1}+|q_1|^{-2}q_1\Pi_{2}$ sends $q_1 q_1'$ to $q_1q_1'\Pi_{1}+|q_1q_1'|^{-2}q_1q_1'\Pi_{2}$, which is the product of the images. The isometry property is the compatibility of §*The Compatibility of the Plain Sesquilinear Form* read twice.

**Remark (the slice is not compact).** The unitary elements form the group $\mathbb{C}^{\times}$, of topology that of a circle times a line, so the slice is not compact; this is a genuine specificity of the reduced biquaternion against the biquaternion category, where the slice $U^{*}U=e_{0}$ is the compact group $U(2)$. The reason is the factoring of the algebra: the star swaps the two idempotents, so the unitarity couples the two coordinates by one equation and not by two, and the slice acquires the non-compact direction of $|q_1|$.

## The Collapse at the Real Base

**At the real base the star equals the natural sign, the four forms collapse to two, and the sesquilinear pair becomes bilinear.**

**Theorem (the collapse).** Let the coefficients be real, $A,B\in\mathbb{R}$. Then $T^{*}=T^{\natural}$ and
$$
\langle T,W\rangle_{\natural*}=\langle T,W\rangle,\qquad \langle T,W\rangle_{*}=\langle T,W\rangle_{\natural},
$$
so the four forms collapse to the two real symmetric bilinear forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, of signatures $(2,2)$ each on the real basis, and the Hermitian condition becomes the plain symmetry.

*Proof.* At real coefficients the coefficient conjugation is the identity, so the star reduces to the natural sign, ${}^{*}={}^{\natural}$. Then $\langle\cdot,\cdot\rangle_{*}=\mathrm{Sc}(T^{\natural}W)=N$ and $\langle\cdot,\cdot\rangle_{\natural*}=\mathrm{Sc}(T^{\natural}W^{\natural})=\mathrm{Sc}(TW)=B$, since $W^{\natural}$ has the same scalar part as $W$ up to the sign of the second coordinate, which the product reads twice. The two remaining forms are symmetric because the coefficient conjugation is the identity.

**Remark (which statements are genuinely sesquilinear).** The compatibility, the bridge identity and the adjoint rule hold in both categories and are read at the real base as the self-adjointness of the left multiplications for the symmetric forms; the sesquilinear content of the article is the dichotomy of the two slot maps, the modulus in the Hermitian condition, the definiteness of $\langle\cdot,\cdot\rangle_{\natural*}$ against the indefiniteness of $\langle\cdot,\cdot\rangle_{*}$, and the non-compactness of the unitary slice — none of which survives the collapse to the real base.

## Summary

The general plain algebra carries four distinguished forms, the scalar parts of the four general products: the **general plain bilinear form** $\langle T,W\rangle=AC+BD$, the **general quaternionic bilinear form** $\langle T,W\rangle_{\natural}=AC-BD$, the **general plain sesquilinear form** $\langle T,W\rangle_{*}=A\bar C-B\bar D$ and the **general quaternionic sesquilinear form** $\langle T,W\rangle_{\natural*}=A\bar C+B\bar D$. The natural sign is $\mathbb{C}$-linear, so $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are bilinear; the star is $\mathbb{C}$-antilinear, so $\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural*}$ are sesquilinear. All four are non-degenerate, with Gram matrices $\mathrm I_{2}$, $\operatorname{diag}(1,-1)$, $\operatorname{diag}(1,-1)$ and $\mathrm I_{2}$ in the basis $1,j$, and signatures $(2,2)$, $(2,2)$, $(2,2)$ and $(4,0)$ over $\mathbb{R}$; $\langle\cdot,\cdot\rangle_{\natural*}$ is positive definite and its square root is the Euclidean norm, and $\langle\cdot\rangle_{*}$ is indefinite. The two sesquilinear forms are Hermitian, with diagonals the algebraic norms $|A|^{2}-|B|^{2}$ and $|A|^{2}+|B|^{2}$, and they are tied by the **bridge identity** $\langle T,W\rangle_{\natural*}=\langle T^{\natural},W\rangle_{*}=\langle T,W^{\natural}\rangle_{*}$, the natural sign being an $\langle\cdot,\cdot\rangle_{*}$-self-adjoint involution fixing the scalar line and negating the $j$-line; this is the fundamental symmetry that makes $\langle\cdot,\cdot\rangle_{\natural*}$ definite and $\langle\cdot,\cdot\rangle_{*}$ indefinite. The general plain sesquilinear form is the one the layer selects: it is **compatible with the product**, $\langle TW,R\rangle_{*}=\langle W,T^{*}R\rangle_{*}$, equivalently $(L_{T})^{H}=L_{T^{*}}$, so $(\mathbb{B}_{\mathrm{r}},{}^{*},H)$ is an object of the layer of *Sesqualgebras with a Form*. Its unitary elements, the solutions of $U^{*}U=1$, form the non-compact group $\mathbb{C}^{\times}$ and not the diagonal unitary group. At the real base the four forms collapse to two, $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T=A+Bj,\ W=C+Dj$ | the two arguments of a form |
| $\langle T,W\rangle=AC+BD$ | the general plain bilinear form, $\mathrm{Sc}(TW)$ |
| $\langle T,W\rangle_{\natural}=AC-BD$ | the general quaternionic bilinear form, $\mathrm{Sc}(T^{\natural}W)$ |
| $\langle T,W\rangle_{*}=A\bar C-B\bar D$ | the general plain sesquilinear form, $\mathrm{Sc}(TW^{*})$ |
| $\langle T,W\rangle_{\natural*}=A\bar C+B\bar D$ | the general quaternionic sesquilinear form, $\mathrm{Sc}(T^{\natural}W^{*})$ |
| $\langle T\rangle=A^{2}+B^{2},\ \langle T\rangle_{\natural}=A^{2}-B^{2}$ | the diagonals of the two bilinear forms |
| $\langle T\rangle_{*}=|A|^{2}-|B|^{2},\ \langle T\rangle_{\natural*}=|A|^{2}+|B|^{2}$ | the diagonals of the two sesquilinear forms |
| $\langle\cdot,\cdot\rangle_{*}$ | the form of the layer, compatible with the product |
| $\langle\cdot,\cdot\rangle_{\natural*}=H\circ(\natural,\mathrm{id})$ | the bridge identity, the fundamental symmetry ${}^{\natural}$ |
| $U^{*}U=1$ | the unitary elements, the group $\mathbb{C}^{\times}$ |

## Further Reading

- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the four products, their forms and their norms together.
- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the norm of the multiplication.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the vanishing sets of the norms.
- *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the adjoint rule and the bi-module structure.
- *The Two Involutions and the Group of Involutions of the Reduced Biquaternions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), for the natural sign, the star and the bar.
- *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form* (`articles_maths/the-form-on-the-biquaternion-algebra-as-a-general-plain-sesquilinear-form.md`), for the non-commutative companion of the layer's selection.
