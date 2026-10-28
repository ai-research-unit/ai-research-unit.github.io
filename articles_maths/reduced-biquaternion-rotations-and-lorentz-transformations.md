# __Reduced Biquaternion Rotations and Lorentz Transformations__

## Introduction

This article studies the orthogonal and the Lorentz-type transformations carried by the reduced biquaternion algebra. The algebra is four-dimensional over the reals, it carries the definite Euclidean form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ of signature $(4,0)$ and the indefinite form $\langle\cdot,\cdot\rangle_{*}$ of signature $(2,2)$, and the elements of the algebra act on it by multiplication, which the commutativity makes the same on the left and on the right. The article records the forms and their signatures, the isometry groups, the versors and their action, the elliptic rotations in the two definite planes, the hyperbolic rotations of the split plane, the group of units preserving the indefinite form, the reading of the polar form as a rotation together with a hyperbolic transformation, and the fact that the conjugation action is trivial. The treatment is purely mathematical; the word rotation is used for the elliptic action on a definite plane and the hyperbolic rotation for the dilation of the two factors reciprocally, with no physical interpretation.

Throughout the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, and $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$. The squared Euclidean norm is $\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$, the indefinite form is $\langle \breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}$, and the algebra norm is $\langle \breve Q\rangle_{\mathrm{ts}}=\breve Q \breve Q_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}$.

## The Quadratic Forms and Their Signatures

**Theorem (the forms).** The two real quadratic forms
$$
\langle \breve Q\rangle_{\mathrm{ts}*}=q_{\blacktriangle}^{2}+q'^{2}_{\blacktriangle}+q_{\blacktriangledown}^{2}+q'^{2}_{\blacktriangledown},\qquad \langle \breve Q\rangle_{*}=q_{\blacktriangle}^{2}+q'^{2}_{\blacktriangle}-q_{\blacktriangledown}^{2}-q'^{2}_{\blacktriangledown}
$$
have signatures $(4,0)$ and $(2,2)$ respectively. They are the scalar parts of the two products with the coefficient conjugation and with the star,
$$
\langle \breve Q\rangle_{\mathrm{ts}*}=\operatorname{Sc}\bigl(\breve Q\bar{\breve Q}\bigr),\qquad \langle \breve Q\rangle_{*}=\operatorname{Sc}\bigl(\breve Q \breve Q^{*}\bigr),
$$
where $\operatorname{Sc}(X+Yj)=X$ is the scalar part, and the algebra norm is complex-valued,
$$
\langle \breve Q\rangle_{\mathrm{ts}}=\breve Q \breve Q_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\bigl(q_{\blacktriangle}^{2}-q'^{2}_{\blacktriangle}-q_{\blacktriangledown}^{2}+q'^{2}_{\blacktriangledown}\bigr)+2i\bigl(q_{\blacktriangle}q'_{\blacktriangle}-q_{\blacktriangledown}q'_{\blacktriangledown}\bigr)=Q_{+}Q_{-},
$$
whose real part and imaginary part are each a form of signature $(2,2)$. The forms $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ and $\langle\cdot,\cdot\rangle_{*}$ are related to the two complex coefficients by $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$ and $\langle\cdot,\cdot\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}$, and in the idempotent coordinates
$$
K=\tfrac12\bigl(\lvert Q_{+}\rvert^{2}+\lvert Q_{-}\rvert^{2}\bigr),\qquad H=\operatorname{Re}(Q_{+}\bar Q_{-}).
$$

*Proof.* The coordinate expressions are the definitions; the signature of $\langle\cdot\rangle_{\mathrm{ts}*}$ is $(4,0)$ because it is a sum of four squares; the form $\langle\cdot,\cdot\rangle_{*}$ is a sum of two squares minus two squares, hence of signature $(2,2)$; multiplying out $\breve Q\bar{\breve Q}$ and $\breve Q \breve Q^{*}$ in the basis $1,j$ and taking the scalar part gives the two displays; the real and the imaginary parts of $\langle\cdot\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}$ are computed directly and are indefinite of type $(2,2)$; and $\lvert Q_{\blacktriangle}\rvert^{2}\pm\lvert Q_{\blacktriangledown}\rvert^{2}=\tfrac12(\lvert Q_{+}\rvert^{2}+\lvert Q_{-}\rvert^{2})\pm\operatorname{Re}(Q_{+}\bar Q_{-})$ from $Q_{\blacktriangle}=\tfrac12(Q_{+}+Q_{-})$, $Q_{\blacktriangledown}=\tfrac12(Q_{+}-Q_{-})$.

**Corollary (the two forms are the natural ones).** The form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is the Euclidean norm used throughout the corpus, and the form $\langle\cdot,\cdot\rangle_{*}$ is the indefinite form whose definite and split parts correspond to the definite generator $i$ and the split generator $j$; the algebra is thus simultaneously a Euclidean and a Lorentz-type object, and both structures are read in the four real coordinates.

*Proof.* The identifications are the coordinate expressions of the theorem, and the definiteness of the $i$-directions against the indefiniteness of the $j$-directions is visible in the signs of $\langle\cdot\rangle_{*}$.

## The Isometry Groups

**Definition.** The **isometry group** of a quadratic form $F$ on the algebra is $O(F)=\{g\in\mathrm{GL}_{4}(\mathbb{R}):F\circ g=F\}$, and the algebra **realises** a subgroup $G\subset O(F)$ when there is a homomorphism $G\to O(F)$ given by the multiplication action of units.

**Theorem (the orthogonal groups and the realised subgroups).** The isometry group of $\langle\cdot\rangle_{\mathrm{ts}*}$ is $O(4)$, of dimension six, with maximal compact subgroup $O(4)$ itself; the isometry group of $\langle\cdot\rangle_{*}$ is $O(2,2)$, of dimension six, with maximal compact subgroup $O(2)\times O(2)$ and identity component $\mathrm{SO}(2,2)_{0}\cong(SL_{2}(\mathbb{R})\times SL_{2}(\mathbb{R}))/\{\pm1\}$. By multiplication the algebra realises inside $O(K)$ the **torus**
$$
T^{2}=\{\breve Q\in\mathbb{B}_{\mathrm{r}}^{\times}:\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1\},
$$
which is a maximal torus of $O(4)$, and inside $O(H)$ the two-real-dimensional group
$$
\{p\,\Pi_++\bar p^{-1}\,\Pi_-:p\in\mathbb{C}^{\times}\}\cong\mathbb{C}^{\times},
$$
whose compact part is the diagonal circle $\{e^{i\theta}\}$.

*Proof.* The orthogonal groups of the two forms are the classical ones, of dimension $n(n-1)/2=6$ for a four-dimensional form, and the maximal compact subgroup of $O(2,2)$ is the product of the two $O(2)$ factors of the diagonalisation. An element $P=p\Pi_++q\Pi_-$ acts on $\langle\cdot\rangle_{\mathrm{ts}*}$ by $\langle P \breve Q\rangle_{\mathrm{ts}*}=\tfrac12(\lvert p\rvert^{2}\lvert Q_{+}\rvert^{2}+\lvert q\rvert^{2}\lvert Q_{-}\rvert^{2})$, which equals $\langle \breve Q\rangle_{\mathrm{ts}*}$ for all $\breve Q$ exactly when $\lvert p\rvert=\lvert q\rvert=1$; it acts on the indefinite form by $\langle P \breve Q\rangle_{*}=\operatorname{Re}\bigl(p\bar q\,Q_{+}\bar Q_{-}\bigr)$, which equals $\langle \breve Q\rangle_{*}=\operatorname{Re}(Q_{+}\bar Q_{-})$ for all $\breve Q$ exactly when $p\bar q=1$, that is $q=\bar p^{-1}$; the two conditions give the two displayed groups, and the compact part of the second is the set of its elements with both moduli equal to one, that is the elements $p=q$ on the unit circle.

**Corollary (only the diagonal subgroups are realised).** Because the algebra is commutative, the multiplication acts diagonally on the two idempotent factors and never permutes them, so a realised subgroup never exchanges the two factors and is a proper subgroup of the full orthogonal group. The realised subgroups are the torus $T^{2}$ inside $O(K)$ and the group $\mathbb{C}^{\times}$ inside $O(H)$, and their intersection is the diagonal circle. The torus preserves also the companion form $S=\tfrac12(\lvert Q_{+}\rvert^{2}-\lvert Q_{-}\rvert^{2})$ of signature $(2,2)$, since a versor preserves each modulus separately.

*Proof.* Left multiplication acts on the idempotent coordinates by the diagonal matrix with entries $p,q$, so the image of the unit group in $\mathrm{GL}_{4}(\mathbb{R})$ is diagonal; the conditions of the theorem select the two displayed subgroups, which are diagonal and therefore contain no permutation of the factors; the diagonal circle is the set of the elements with $\lvert p\rvert=\lvert q\rvert=1$ and $q=\bar p^{-1}$, that is $p=q$ on the unit circle; and $S$ is preserved because $\lvert pQ_{+}\rvert^{2}=\lvert Q_{+}\rvert^{2}$ and $\lvert qQ_{-}\rvert^{2}=\lvert Q_{-}\rvert^{2}$ for a versor.

## The Versors and Their Action

**Definition.** A **versor** is a unit $P=p\Pi_++q\Pi_-$ with $\lvert p\rvert=\lvert q\rvert=1$; the versors form the group $T^{2}$.

**Theorem (the action of a versor).** Every versor has the form
$$
\boxed{\;
P=e^{i\theta}\Pi_++e^{i\psi}\Pi_-,\qquad \theta,\psi\in\mathbb{R}
\;},
$$
it preserves the Euclidean form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$, it acts by left multiplication as the diagonal map
$$
\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-\;\longmapsto\;e^{i\theta}Q_{+}\Pi_++e^{i\psi}Q_{-}\Pi_-,
$$
and it scales the algebra norm by $\langle P\rangle_{\mathrm{ts}}=e^{i(\theta+\psi)}$. Among the versors, exactly those with $\theta=\psi$, that is the diagonal circle, preserve the indefinite form $\langle\cdot,\cdot\rangle_{*}$ as well.

*Proof.* A unit with both coordinate moduli equal to one has each coordinate on the unit circle, giving the displayed form; the action is the diagonal multiplication by the two coordinates, which preserves the two moduli, hence $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=\tfrac12(\lvert Q_{+}\rvert^{2}+\lvert Q_{-}\rvert^{2})$ and the companion form $S$, and multiplies the product $Q_{+}Q_{-}$, hence $\langle\cdot,\cdot\rangle_{\mathrm{ts}}$ by $pq=e^{i(\theta+\psi)}$; the indefinite form transforms by $\langle P \breve Q\rangle_{*}=\operatorname{Re}(e^{i(\theta-\psi)}Q_{+}\bar Q_{-})$, which equals $\langle \breve Q\rangle_{*}$ for all $\breve Q$ exactly when $\theta=\psi$.

**Corollary (the kernel and the stabiliser of the forms).** The action of $T^{2}$ is faithful, and the pair $(\theta,\psi)$ is determined modulo $2\pi$ in each entry; the versors act on the algebra as the diagonal $*$-unitary transformations of the two complex factors, and the subgroup fixing $\langle\cdot\rangle_{*}$ is the diagonal circle, which is also the compact part of the realised group $\mathbb{C}^{\times}$ of $O(H)$.

*Proof.* If the action is the identity then $e^{i\theta}=e^{i\psi}=1$, so the representation has trivial kernel, and the phases are determined modulo the full turn; the subgroup fixing $\langle\cdot\rangle_{*}$ is the set $\theta=\psi$ by the theorem, which is the diagonal circle and agrees with the compact part found in the isometry theorem.

## The Elliptic Rotations in the Two Factors

**Theorem (the two definite planes).** The algebra carries the two independent definite directions $i$ and $ij$, both with square $-1$, and the exponentials
$$
e^{i\theta}=\cos\theta+i\sin\theta,\qquad e^{ij\psi}=\cos\psi+ij\sin\psi
$$
generate the two elliptic subgroups in the planes $\mathbb{R}\{1,i\}$ and $\mathbb{R}\{1,ij\}$. Their product is the whole torus $T^{2}$:
$$
e^{i\theta}e^{ij\psi}=e^{i(\theta+\psi)}\Pi_++e^{i(\theta-\psi)}\Pi_-,
$$
so the two elliptic rotations produce the diagonal phases $(\theta+\psi,\theta-\psi)$ of the two idempotent factors.

*Proof.* The closed forms are the Euler formulas in the two definite planes; the coordinates of $ij$ are $(i,-i)$, so $e^{ij\psi}$ has coordinates $(e^{i\psi},e^{-i\psi})$, and multiplying by the coordinates $(e^{i\theta},e^{i\theta})$ of $e^{i\theta}$ gives the displayed pair; as $\theta,\psi$ vary the pair sweeps the whole torus.

**Corollary (the two rotations of the two factors).** Each idempotent factor, $\mathbb{C}\Pi_+$ or $\mathbb{C}\Pi_-$, carries its own complex plane, and the torus acts on it by the rotation of that plane; the two rotations are independent, and their product is the general versor action. This is the precise sense in which the reduced biquaternion algebra carries **two** rotations, one per factor. The two circles act differently on the forms: the diagonal circle $e^{i\theta}$ preserves both $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ and $\langle\cdot,\cdot\rangle_{*}$, while the second circle $e^{ij\psi}$ preserves $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ but not $\langle\cdot,\cdot\rangle_{*}$.

*Proof.* The first coordinate of the algebra is a complex number on which the action is the rotation by the phase $\theta+\psi$, and the second coordinate is a complex number on which the action is the rotation by $\theta-\psi$; the map from the pair of phases to the pair of rotations is invertible; and the two form statements are those of the versor theorem.

## The Hyperbolic Rotations and the Split Plane

**Theorem (the hyperbolic rotation).** The element $j$ has $j^{2}=+1$, so
$$
\boxed{\;
e^{j\phi}=\cosh\phi+j\sinh\phi
\;}
$$
generates a non-compact one-parameter subgroup of hyperbolic rotations, and its action on the split complex plane $S_{j}=\mathbb{R}\{1,j\}$ is
$$
a+bj\;\longmapsto\;(a\cosh\phi+b\sinh\phi)+(a\sinh\phi+b\cosh\phi)\,j ,
$$
which preserves the form $\langle a+bj\rangle_{*}=a^{2}-b^{2}$ and the form $\langle a+bj\rangle_{\mathrm{ts}}=a^{2}-b^{2}$. In the idempotent coordinates the same action dilates the two factors reciprocally,
$$
(Q_{+},Q_{-})\;\longmapsto\;(e^{\phi}Q_{+},\;e^{-\phi}Q_{-}).
$$

*Proof.* The closed form of the exponential is the hyperbolic one; multiplying out $(\cosh\phi+j\sinh\phi)(a+bj)$ and using $j^{2}=1$ gives the displayed transformation; the two invariants are computed from the result; and the coordinates of $e^{j\phi}$ are $(e^{\phi},e^{-\phi})$, which give the reciprocal dilation.

**Corollary (the hyperbolic rotation is not compact, and its two forms).** The hyperbolic rotation preserves the indefinite form $\langle\cdot,\cdot\rangle_{*}$ and the algebra norm $\langle\cdot\rangle_{\mathrm{ts}}$ but not the Euclidean form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$, which it scales; it is the Lorentz-type transformation carried by the split generator $j$. The elliptic rotation $e^{i\theta}$ preserves both $\langle\cdot\rangle_{\mathrm{ts}*}$ and $\langle\cdot\rangle_{*}$ and scales $\langle\cdot\rangle_{\mathrm{ts}}$ by $e^{2i\theta}$, while the elliptic rotation $e^{ij\psi}$ preserves $\langle\cdot\rangle_{\mathrm{ts}*}$ and $\langle\cdot\rangle_{\mathrm{ts}}$ but not $\langle\cdot\rangle_{*}$.

*Proof.* For $\breve Q=a+bj$ one has $\langle e^{j\phi}\breve Q\rangle_{\mathrm{ts}*}=a^{2}\cosh2\phi+2ab\sinh2\phi+b^{2}\cosh2\phi$, which differs from $\langle \breve Q\rangle_{\mathrm{ts}*}$ for $b\neq0$, while $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\mathrm{ts}}$ are preserved because the coordinates of $e^{j\phi}$ are $(e^{\phi},e^{-\phi})$ and their product is $1$; the diagonal circle has coordinates $(e^{i\theta},e^{i\theta})$, whose product is $e^{2i\theta}$ and which preserves $\langle\cdot\rangle_{*}$; and $e^{ij\psi}$ has coordinates $(e^{i\psi},e^{-i\psi})$, whose product is $1$, and it changes $\langle\cdot\rangle_{*}$ by the phase $e^{2i\psi}$.

**The split plane in hyperbolic coordinates.** The plane $S_{j}$ is the split complex plane, whose group of units of norm one is the hyperbola $\langle \breve Q\rangle_{*}=1$; the hyperbolic rotation acts on this hyperbola by translation of the hyperbolic parameter, so it is the one-parameter group of the hyperbola, and the Lorentz-type structure of the plane is carried by $j$.

## The Group of Units Preserving the Indefinite Form

**Theorem (the group preserving the indefinite form).** In the idempotent coordinates the indefinite form is $\langle\cdot,\cdot\rangle_{*}=\operatorname{Re}(Q_{+}\bar Q_{-})$, and a unit $P=p\Pi_++q\Pi_-$ acts on it by $\langle P \breve Q\rangle_{*}=\operatorname{Re}\bigl(p\bar q\,Q_{+}\bar Q_{-}\bigr)$. Consequently $P$ preserves $\langle\cdot\rangle_{*}$ exactly when $p\bar q=1$, that is $q=\bar p^{-1}$, and the units preserving $\langle\cdot,\cdot\rangle_{*}$ form the group
$$
\{p\,\Pi_++\bar p^{-1}\,\Pi_-:p\in\mathbb{C}^{\times}\}\cong\mathbb{C}^{\times},
$$
of real dimension two, acting on the pair of coordinates by $(Q_{+},Q_{-})\mapsto(pQ_{+},\bar p^{-1}Q_{-})$. This group contains the hyperbolic one-parameter subgroup $\{e^{j\phi}\}$, corresponding to the real positive values $p=e^{\phi}$, and the diagonal circle $\{e^{i\theta}\}$, corresponding to $\lvert p\rvert=1$.

*Proof.* The transformation of $\langle\cdot\rangle_{*}$ is the multiplication of $Q_{+}\bar Q_{-}$ by $p\bar q$; for the value of $\langle\cdot\rangle_{*}$ to be unchanged for every $\breve Q$ the factor must be $1$, which is the condition $q=\bar p^{-1}$; the parametrisation by $p$ is one-to-one, and the coordinates of $e^{j\phi}$ are $(e^{\phi},e^{-\phi})$ with $e^{-\phi}=\overline{e^{\phi}}^{-1}$, and those of $e^{i\theta}$ are $(e^{i\theta},e^{i\theta})$ with $e^{i\theta}=\overline{e^{i\theta}}^{-1}$.

**Corollary (the Lorentz group of the indefinite form and its realised subgroup).** The full isometry group of $\langle\cdot,\cdot\rangle_{*}$ is the six-dimensional $O(2,2)$, and the algebra realises inside it the two-dimensional group $\mathbb{C}^{\times}$, whose compact part is the circle and whose non-compact part is the hyperbolic line; it is neither the whole of $O(2,2)$ nor a maximal compact subgroup of it. The non-realised part contains, for instance, the exchange $(Q_{+},Q_{-})\mapsto(Q_{-},Q_{+})$ and the simultaneous conjugation $(Q_{+},Q_{-})\mapsto(\bar Q_{+},\bar Q_{-})$, both of which preserve $\langle\cdot\rangle_{*}$ and neither of which is a multiplication by an algebra element.

*Proof.* The realised group is the one computed in the theorem, of dimension two; the exchange and the conjugation preserve $\operatorname{Re}(Q_{+}\bar Q_{-})$ and are not of the form $(Q_{+},Q_{-})\mapsto(pQ_{+},\bar p^{-1}Q_{-})$, which keeps the two coordinates separate and multiplies them by factors of mutually reciprocal modulus.

## The Triviality of Conjugation

**Theorem (conjugation is the identity).** For any unit $P$ and any $\breve Q$,
$$
P \breve Q P^{-1}=\breve Q ,
$$
since the algebra is commutative. Consequently the conjugation action, the orbit of an element under the unit group, is a single point, and the sandwich actions $\breve Q\mapsto P \breve Q P_{\mathrm{ts}}$ and $\breve Q\mapsto P \breve Q P^{*}$ reduce to multiplications: $P \breve Q P_{\mathrm{ts}}=\langle P\rangle_{\mathrm{ts}}\,\breve Q$ and $P \breve Q P^{*}=\bigl(p\bar q\,\Pi_++q\bar p\,\Pi_-\bigr)\breve Q$ for $P=p\Pi_++q\Pi_-$.

*Proof.* Commutativity gives $P \breve Q P^{-1}=PP^{-1}\breve Q=\breve Q$; multiplying out the two sandwich expressions in the idempotent coordinates gives $\langle P\rangle_{\mathrm{ts}}\breve Q=(pq)\breve Q$ and $(p\bar q,q\bar p)\breve Q$ respectively.

**Corollary (the contrast with the biquaternion case).** In the quaternion and biquaternion cases the conjugation $P \breve Q P^{-1}$ is the rotation action and the sandwich is the proper rotation of the Euclidean three-space; here conjugation is trivial and the only non-trivial action is multiplication. This is the geometric face of the commutativity of the algebra: the rotation group must be realised by the multiplicative action and not by conjugation, and therefore only the diagonal subgroups appear.

*Proof.* The quaternion conjugation action is the double cover of the rotation group, and its non-triviality rests on the anticommutation of the imaginary units; the reduced biquaternion algebra has no anticommutation, so the conjugation collapses and the multiplicative action is the only one.

## The Polar Form as a Rotation and a Hyperbolic Transformation

**Theorem (the factorisation of the polar form).** The polar form of an element, established in *Modulus–Unit Polar Decomposition of Reduced Biquaternions*, is
$$
\boxed{\;
\breve Q=\rho_{1}e^{i\theta_{1}}\Pi_++\rho_{2}e^{i\theta_{2}}\Pi_-,\qquad \rho_{1},\rho_{2}\ge0,\quad \theta_{1},\theta_{2}\in(-\pi,\pi]
\;}.
$$
Setting
$$
\rho=\sqrt{\rho_{1}\rho_{2}},\qquad \phi=\tfrac12\log\frac{\rho_{1}}{\rho_{2}},\qquad
\theta=\tfrac12(\theta_{1}+\theta_{2}),\qquad \psi=\tfrac12(\theta_{1}-\theta_{2}),
$$
it becomes
$$
\breve Q=\rho\;e^{j\phi}\;e^{i\theta}\;e^{ij\psi},
$$
the four factors commuting. For an element of modulus one ($\rho_{1}\rho_{2}=1$) one has $\rho=1$, and it is the product of a hyperbolic rotation and two elliptic rotations,
$$
\breve Q=e^{j\phi}\,e^{i\theta}\,e^{ij\psi};
$$
a general unit is $\breve Q=\rho\,e^{j\phi}e^{i\theta}e^{ij\psi}$ with the scale $\rho=\sqrt{\rho_{1}\rho_{2}}>0$.

*Proof.* The coordinates of the four factors are $(\rho,\rho)$ for the scale, $(e^{\phi},e^{-\phi})$ for $e^{j\phi}$, $(e^{i\theta},e^{i\theta})$ for $e^{i\theta}$ and $(e^{i\psi},e^{-i\psi})$ for $e^{ij\psi}$, since $j$ has coordinates $(1,-1)$ and $ij$ has coordinates $(i,-i)$; multiplying the four coordinate pairs gives $\bigl(\rho e^{\phi}e^{i(\theta+\psi)},\rho e^{-\phi}e^{i(\theta-\psi)}\bigr)$, which is the polar form with $\rho_{1}=\rho e^{\phi}$ and $\theta_{1}=\theta+\psi$, $\rho_{2}=\rho e^{-\phi}$ and $\theta_{2}=\theta-\psi$, and the two pairs are equivalent by the displayed definitions.

**Corollary (the rotation-versus-hyperbolic reading).** The polar form is therefore the product of three commuting factors of distinct types: the **scale** $\rho$, which dilates both coordinates; the **hyperbolic rotation** $e^{j\phi}$, which is the Lorentz-type transformation dilating the two coordinates reciprocally and preserving the indefinite form $\langle\cdot,\cdot\rangle_{*}$; and the **elliptic rotation** $e^{i\theta}e^{ij\psi}$, which is the versor, preserving the Euclidean form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$. The hyperbolic parameter is $\phi=\tfrac12\log(\rho_{1}/\rho_{2})$, read as the logarithm of the ratio of the two scales, and the rotation parameters are the sum and the difference of the two phases.

*Proof.* The types are those of the three factors: the scale multiplies both coordinates by $\rho$; the factor $e^{j\phi}$ preserves $\langle\cdot\rangle_{*}$ by the reciprocal dilation; and the factor $e^{i\theta}e^{ij\psi}$ lies in the torus $T^{2}$ and preserves $\langle\cdot\rangle_{\mathrm{ts}*}$; the parameters are the ones defined in the theorem.

## The Relation to the Biquaternion and Split-Biquaternion Cases

The biquaternion algebra carries the sandwich action $Q\mapsto PQP^{-1}$ with $P$ a versor, which is the double cover of the rotation group of the Euclidean three-space and, in its Lorentz form, of the Lorentz group of the four-dimensional quadratic space; the conjugation is non-trivial and the sandwich is the geometric action. The split biquaternion algebra carries the product of two such rotations, one per quaternion half, with the Lorentz-type transformations distributed over the two halves, and the geometry is the product of the two rotation structures. The reduced biquaternion algebra is the commutative case in which the conjugation collapses to the identity, the multiplicative action is diagonal on the two complex factors, the realised groups are the torus in the orthogonal group of $\langle\cdot\rangle_{\mathrm{ts}*}$ and the group $\mathbb{C}^{\times}$ in the orthogonal group of $\langle\cdot\rangle_{*}$, and the two elliptic rotations of the factors replace the single three-dimensional rotation of the non-commutative cases. What is lost is the three-dimensional rotation group and its Lorentz counterpart; what remains is the diagonal structure of the two factors, which is exact and explicit.

## Summary

The reduced biquaternion algebra carries the definite Euclidean form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ of signature $(4,0)$, the scalar part of $\breve Q\bar{\breve Q}$, and the indefinite form $\langle\cdot,\cdot\rangle_{*}$ of signature $(2,2)$, the scalar part of $\breve Q \breve Q^{*}$; the algebra norm $\langle\cdot\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}$ is complex-valued, with its real and imaginary parts also forms of signature $(2,2)$. The isometry groups of $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ and $\langle\cdot,\cdot\rangle_{*}$ are the six-dimensional $O(4)$ and $O(2,2)$; by multiplication the algebra realises inside $O(K)$ the two-dimensional torus $T^{2}=\{\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1\}$, a maximal torus, and inside $O(H)$ the two-dimensional group $\{p\Pi_++\bar p^{-1}\Pi_-\}\cong\mathbb{C}^{\times}$, whose compact part is the diagonal circle. The versors are the elements of the torus; they preserve $\langle\cdot\rangle_{\mathrm{ts}*}$ and act diagonally on the two idempotent factors, they scale the algebra norm, and among them exactly the diagonal circle preserves $\langle\cdot\rangle_{*}$. The elliptic rotations are the exponentials of the two definite directions $i$ and $ij$, whose product generates the whole torus and acts by the pair of phases $(\theta+\psi,\theta-\psi)$ on the two factors, so that the algebra carries exactly two independent rotations, one per factor. The hyperbolic rotation is the exponential of the split direction $j$, $e^{j\phi}=\cosh\phi+j\sinh\phi$, which preserves $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\mathrm{ts}}$ but not $\langle\cdot\rangle_{\mathrm{ts}*}$, and which acts on the split complex plane as the ordinary hyperbolic rotation and on the two factors as the reciprocal dilation $(e^{\phi}Q_{+},e^{-\phi}Q_{-})$. The units preserving $\langle\cdot\rangle_{*}$ are exactly the elements $\{p\Pi_++\bar p^{-1}\Pi_-\}$, a two-dimensional subgroup of the six-dimensional $O(2,2)$ containing the hyperbolic line and the diagonal circle, the remaining isometries, such as the exchange and the conjugation of the two coordinates, being unavailable because the multiplication is diagonal. Conjugation is the identity, since the algebra is commutative, and the sandwich actions reduce to multiplications by the algebra norm and by a diagonal element. The polar form reads as the product of a scale, a hyperbolic rotation and two elliptic rotations, $\breve Q=\rho\,e^{j\phi}\,e^{i\theta}\,e^{ij\psi}$, with the hyperbolic parameter the logarithm of the ratio of the two scales and the rotation parameters the sum and the difference of the two phases, which is the precise sense in which the polar form is a rotation together with a hyperbolic Lorentz-type transformation. Against the biquaternion and split biquaternion cases, whose conjugation and sandwich give the three-dimensional rotation group and its Lorentz counterpart, the reduced biquaternion algebra realises only the diagonal subgroups, the torus of the Euclidean form and the group $\mathbb{C}^{\times}$ of the indefinite one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}=q_{\blacktriangle}^{2}+q'^{2}_{\blacktriangle}+q_{\blacktriangledown}^{2}+q'^{2}_{\blacktriangledown}$ | Euclidean form, signature $(4,0)$ |
| $\langle\cdot,\cdot\rangle_{*}=q_{\blacktriangle}^{2}+q'^{2}_{\blacktriangle}-q_{\blacktriangledown}^{2}-q'^{2}_{\blacktriangledown}$ | Indefinite form, signature $(2,2)$ |
| $\langle\cdot,\cdot\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}$ | Algebra norm, complex-valued |
| $O(K)=O(4)$, $O(H)=O(2,2)$ | Isometry groups, dimension six |
| $T^{2}=\{\lvert Q_{+}\rvert=\lvert Q_{-}\rvert=1\}$ | Realised torus of versors, a maximal torus of $O(4)$ |
| $\{p\Pi_++\bar p^{-1}\Pi_-\}\cong\mathbb{C}^{\times}$ | Realised group of the indefinite form |
| $e^{i\theta}$, $e^{ij\psi}$ | Elliptic rotations of the two definite planes |
| $e^{j\phi}=\cosh\phi+j\sinh\phi$ | Hyperbolic rotation |
| $\breve Q=\rho\,e^{j\phi}\,e^{i\theta}\,e^{ij\psi}$ | Polar form as scale, hyperbolic rotation and elliptic rotations |
| $P \breve Q P^{-1}=\breve Q$ | Triviality of conjugation |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the orthogonal and Lorentz-type groups of a quadratic space and the versor action.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (Academic Press, 1978), for the orthogonal groups, their maximal compact subgroups and the symmetric space structure.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the rotation and Lorentz actions of the hypercomplex algebras.
- G. Baley Price, *An Introduction to Multicomplex Spaces and Functions* (Marcel Dekker, 1991), for the quadratic forms and the multiplicative action of the multicomplex algebra.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the diagonal action on the two idempotent factors.
